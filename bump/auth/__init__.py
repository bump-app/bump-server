from flask import render_template
from datetime import datetime, timedelta
from bump import APP as app, DB as db, oauth2
from bump.users.model import User
from bump.auth.client import Client
from bump.auth.grant import Grant
from bump.auth.token import Token


@oauth2.usergetter
def get_user(email, password, *args, **kwargs):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return user
    return None

def current_user():
    if 'id' in db.session:
        uid = db.session['id']
        return User.query.get(uid)
    return None

# client
@oauth2.clientgetter
def load_client(client_id):
    return Client.query.filter_by(client_id=client_id).first()

# grant
@oauth2.grantgetter
def load_grant(client_id, code):
    return Grant.query.filter_by(client_id=client_id, code=code).first()

@oauth2.grantsetter
def save_grant(client_id, code, request, *args, **kwargs):
    return Grant.query.filter_by(client_id=client_id, code=code).first()
    expires = datetime.utcnow() + timedelta(seconds=120)
    grant = Grant(client_id=client_id,
                  code=code['code'],
                  redirect_uri=request.redirect_uri,
                  _scopes=' '.join(request.scopes),
                  user=current_user,
                  expires=expires)
    db.session.add(grant)
    db.session.commit()
    return grant

# token
@oauth2.tokengetter
def load_token(access_token=None, refresh_token=None):
    if access_token:
        return Token.query.filter_by(access_token=access_token).first()
    elif refresh_token:
        return Token.query.filter_by(refresh_token=refresh_token).first()

@oauth2.tokensetter
def save_token(token, request, *args, **kwargs):
    tokens = Token.query.filter_by(client_id=request.client.client_id, user_id=request.user.id)
    for t in tokens:
        db.session.delete(t)
    expires_in = token.get('expires_in')
    expires = datetime.utcnow() + timedelta(seconds=expires_in)
    tok = Token(access_token=token['access_token'],
                refresh_token=token['refresh_token'],
                token_type=token['token_type'],
                _scopes=token['scope'],
                expires=expires,
                client_id=request.client.client_id,
                user_id=request.user.id)
    db.session.add(tok)
    db.session.commit()
    return tok

@app.route('/oauth/token', methods=['GET', 'POST'])
@oauth2.token_handler
def access_token():
    return None

@app.route('/oauth/revoke', methods=['POST'])
@oauth2.revoke_handler
def revoke_token():
    pass

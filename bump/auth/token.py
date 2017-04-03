from bump import DB as db, oauth2
from datetime import datetime, timedelta

class Token(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	token_type = db.Column(db.String(40))
	access_token = db.Column(db.String(255), unique=True)
	refresh_token = db.Column(db.String(255), unique=True)
	expires = db.Column(db.DateTime)
	_scopes = db.Column(db.Text)
	client_id = db.Column(db.String(40), db.ForeignKey('clients.id'), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def delete(self):
		db.session.delete(self)
		db.session.commit()
		return self

	@property
	def scopes(self):
		if self._scopes:
			return self._scopes.split()
		return []

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

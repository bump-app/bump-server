from flask import render_template
from bump import APP as app, oauth2
from bump.users.model import User

# user
@oauth2.usergetter
def get_user(username, password, *args, **kwargs):
	user = User.query.filter_by(username=username).first()
	if user.check_password(password):
		return user
	return None

# routes
@app.route('/oauth/authorize', methods=['GET', 'POST'])
# @require_login
@oauth2.authorize_handler
def authorize(*args, **kwargs):
	if request.method == 'GET':
		client_id = kwargs.get('client_id')
		client = Client.query.filter_by(client_id=client_id).first()
		kwargs['client'] = client
		# return render_template('oauthorize.html', **kwargs)

	confirm = request.form.get('confirm', 'no')
	return confirm == 'yes'

@app.route('/oauth/token')
@oauth2.token_handler
def access_token():
	return None

@app.route('/oauth/revoke', methods=['POST'])
@oauth2.revoke_handler
def revoke_token():
	pass

from bump import DB as db, oauth2
from datetime import datetime, timedelta

class Grant(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(255), index=True, nullable=False)
	redirect_uri=db.Column(db.String(255))
	expires = db.Column(db.DateTime)
	_scopes = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
	client_id = db.Column(db.String(40), db.ForeignKey('clients.id'), nullable=False)

	def delete(self):
		db.session.delete(self)
		db.session.commit()
		return self

	@property
	def scopes(self):
		if self._scopes:
			return self._scopes.split()
		return []

@oauth2.grantgetter
def load_grant(client_id, code):
	return Grant.query.filter_by(client_id=client_id, code=code).first()

@oauth2.grantsetter
def save_grant(client_id, code, request, *args, **kwargs):
	expires = datetime.utcnow() + timedelta(seconds=120)
	grant = Grant(	client_id=client_id,
					code=code['code'],
					redirect_uri=request.redirect_uri,
					_scopes=' '.join(request.scopes),
					# user=asdf,
					expires=expires)
	db.session.add(grant)
	db.session.commit()
	return grant

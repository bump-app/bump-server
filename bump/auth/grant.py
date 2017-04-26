from bump import DB as db

class Grant(db.Model):
	__tablename__ = 'grants'
	id = db.Column(db.Integer, primary_key=True)
	code = db.Column(db.String(255), index=True, nullable=False)
	redirect_uri=db.Column(db.String(255))
	expires = db.Column(db.DateTime)
	_scopes = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'))
	client_id = db.Column(db.String(40), db.ForeignKey('clients.client_id'), nullable=False)

	def delete(self):
		db.session.delete(self)
		db.session.commit()
		return self

	@property
	def scopes(self):
		if self._scopes:
			return self._scopes.split()
		return []

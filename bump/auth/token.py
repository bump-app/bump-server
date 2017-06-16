from bump import DB as db

class Token(db.Model):
    __tablename__ = 'tokens'
    id = db.Column(db.Integer, primary_key=True)
    token_type = db.Column(db.String(40))
    access_token = db.Column(db.String(255), unique=True)
    refresh_token = db.Column(db.String(255), unique=True)
    expires = db.Column(db.DateTime)
    _scopes = db.Column(db.Text)
    client_id = db.Column(db.String(40), db.ForeignKey('clients.client_id'), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

        @property
        def scopes(self):
            if self._scopes:
                return self._scopes.split()
                return []

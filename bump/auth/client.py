from bump import DB as db

class Client(db.Model):
    __tablename__ = 'clients'
    client_id = db.Column(db.String(40), primary_key=True)
    secret = db.Column(db.String(55), unique=True, index=True, nullable=False)
    name = db.Column(db.String(40))
    is_confidential = db.Column(db.Boolean)
    _redirect_uris = db.Column(db.Text)
    _default_scopes = db.Column(db.Text)
    user_id = db.Column(db.ForeignKey('users.id'))
    grants = db.relationship('Grant', backref='client')
    tokens = db.relationship('Token', backref='client')

    @property
    def client_type(self):
        if self.is_confidential:
            return 'confidential'
        return 'public'

    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        return self.redirect_uris[0]

    @property
    def default_scopes(self):
        if self._default_scopes:
            return self._default_scopes.split()
        return []

    @property
    def allowed_grant_types(self):
        return ['authorization_code', 'password', 'client_credentials', 'refresh_token']

    # FIXME
    # this methods gets called if it exists
    # right now all scopes are just passed through
    def validate_scopes(self, scopes):
        return scopes


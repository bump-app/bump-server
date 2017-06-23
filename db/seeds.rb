Doorkeeper::Application.create(
  name: 'bump-development',
  uid: 'dev',
  secret: '1234',
  redirect_uri: 'urn:ietf:wg:oauth:2.0:oob',
  scopes: 'public'
)

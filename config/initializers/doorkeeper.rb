Doorkeeper.configure do
  realm 'Bump'
  orm :active_record
  base_controller 'ApplicationController'
  force_ssl_in_redirect_uri !Rails.env.development?

  resource_owner_authenticator do
    User.find(doorkeeper_token.resource_owner_id) || error!
  end

  resource_owner_from_credentials do
    user = User.find_by(email: params[:username])
    user if user&.authenticate(params[:password])
  end

  # admin_authenticator do
  # end

  # Under some circumstances you might want to have applications auto-approved,
  # so that the user skips the authorization step.
  # For example if dealing with a trusted application.
  # skip_authorization do |resource_owner, client|
  #   client.superapp? or resource_owner.admin?
  # end

  # authorization_code_expires_in 10.minutes
  access_token_expires_in 10.days
  reuse_access_token
  use_refresh_token

  # enable_application_owner confirmation: true
  # native_redirect_uri 'urn:ietf:wg:oauth:2.0:oob'

  default_scopes  :public
  optional_scopes :everything

  grant_flows %w[
    authorization_code client_credentials implicit password assertion
  ]
end

Doorkeeper::AccessToken.class_eval do
  belongs_to :resource_owner, class_name: 'User'
end

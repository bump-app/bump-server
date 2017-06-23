class ApplicationController < JSONAPI::ResourceController
  before_action :validate_token!
  # before_action :doorkeeper_authorize!
  force_ssl if Rails.env.production?

  def base_url
    super + '/api'
  end

  def current_user
    doorkeeper_token
  end

  def signed_in?
    current_user.present?
  end

  def validate_token!
    return unless doorkeeper_token && !doorkeeper_token.accessible?
    render json: {
      errors: [
        { title: 'Invalid token', status: '403' }
      ]
    }, status: 403
  end

  def context
    { current_user: current_user }
  end
end

class ApplicationController < JSONAPI::ResourceController
  include Pundit
  include Pundit::ResourceController

  before_action :validate_token!
  # before_action :doorkeeper_authorize!
  skip_after_action :enforce_policy_use
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

  def policy_for(model)
    Pundit.policy!(current_user, model)
  end

  def scope_for(model)
    Pundit.policy_scope!(current_user, model)
  end

  def show?(model)
    scope = model.class.where(id: model.id)
    scope_for(scope).exists?
  end

  def user
    doorkeeper_token&.resource_owner
  end

  def authenticate_user!
    unless user
      render_jsonapi serialize_error(403, 'Must be logged in'), status: 403
    end
  end

  def render_jsonapi(data, opts = {})
    render opts.merge(json: data, content_type: JSONAPI::MEDIA_TYPE)
  end
end

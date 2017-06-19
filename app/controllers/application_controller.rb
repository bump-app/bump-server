class ApplicationController < JSONAPI::ResourceController
  def base_url
    super + '/api'
  end

  force_ssl if Rails.env.production?
end

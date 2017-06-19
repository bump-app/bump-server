require_relative 'boot'

require 'rails'
# Pick the frameworks you want:
require 'active_model/railtie'
require 'active_job/railtie'
require 'active_record/railtie'
require 'action_controller/railtie'
require 'action_mailer/railtie'
require 'action_view/railtie'
require 'action_cable/engine'
# require 'sprockets/railtie'
require 'rails/test_unit/railtie'

# Require the gems listed in Gemfile, including any gems
# you've limited to :test, :development, or :production.
Bundler.require(*Rails.groups)

module Bump
  class Application < Rails::Application
    config.api_only = true

    config.time_zone = 'UTC'

    concern_dirs = Dir['app/*/concerns'].map { |d| File.expand_path(d) }
    config.eager_load_paths += concern_dirs
    config.eager_load_paths.uniq!

    config.autoload_paths << "#{Rails.root}/lib"

    config.log_level = ENV['LOG_LEVEL'] || :info

    config.middleware.insert_before 0, Rack::Cors do
      allow do
        origins '*'
        resource '*', headers: :any,
                      methods: :any,
                      credentials: false,
                      max_age: 1.hour
      end
    end

    config.generators do |g|
      g.authorization :policy
      g.serialization :jsonapi_resource
      g.resource_controller :resource_controller
    end
  end
end

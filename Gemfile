source 'https://rubygems.org'
ruby '2.3.1'

# core
gem 'puma'
gem 'rails', '~> 5.0.1'

# db
gem 'pg'
# gem 'redis', '~> 3.0'

# auth
gem 'bcrypt'
gem 'doorkeeper'
gem 'doorkeeper-grants_assertion', git: 'https://github.com/doorkeeper-gem/doorkeeper-grants_assertion'
gem 'pundit'
gem 'pundit-resources'
gem 'rolify'

# utils
gem 'counter_culture'
gem 'fast_blank'
gem 'friendly_id'
gem 'jsonapi-resources'
gem 'lograge'
gem 'oj'
gem 'oj_mimic_json'
gem 'paranoia', '~> 2.2'

# rack
gem 'rack-attack'
gem 'rack-cors'

group :development, :test do
  gem 'annotate'
  gem 'dotenv-rails'
  gem 'pry-rails'
  gem 'spring'

  gem 'database_cleaner'
  gem 'factory_girl_rails'
  gem 'rspec-rails'

  gem 'guard'
  gem 'guard-rspec', require: false
end

group :test do
  gem 'faker'
  gem 'json_expressions'
  gem 'oauth2'
  gem 'shoulda-matchers'
  gem 'timecop'
  gem 'webmock'
end

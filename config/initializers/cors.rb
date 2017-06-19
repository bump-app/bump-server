Rails.application.config.middleware.insert_before 0, Rack::Cors do
  allow do
    origins '*'
    resource '*', headers: :any,
                  methods: :any,
                  credentials: false,
                  max_age: 1.hour
  end
end

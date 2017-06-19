JSONAPI.configure do |config|
  # keying
  config.json_key_format = :camelized_key

  # pagination
  config.default_paginator = :offset
  config.top_level_links_include_pagination = true

  # caching
  config.resource_cache = Rails.cache

  # metadata
  config.top_level_meta_include_record_count = true
  config.top_level_meta_record_count_key = :count

  # errors
  config.raise_if_parameters_not_allowed = true
end

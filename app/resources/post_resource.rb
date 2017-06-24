class PostResource < ApplicationResource
  attributes :link, :link_formatted, :text, :created_at

  has_one :user
  has_one :channel

  has_many :comments

  filters :user_id, :channel_id
end

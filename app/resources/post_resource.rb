class PostResource < ApplicationResource
  attributes :link, :link_formatted, :text

  has_one :user
  has_one :channel

  has_many :comments

  filters :user_id, :channel_id
end

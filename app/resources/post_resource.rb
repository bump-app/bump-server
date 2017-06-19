class PostResource < BaseResource
  attributes :link, :link_formatted, :text

  has_one :user
  has_one :channel

  filters :user_id, :channel_id
end

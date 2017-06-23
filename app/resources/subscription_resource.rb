class SubscriptionResource < ApplicationResource
  has_one :user
  has_one :channel

  filters :user_id, :channel_id
end

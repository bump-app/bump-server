class FriendshipResource < ApplicationResource
  has_one :user
  has_one :friend

  filters :user_id
end

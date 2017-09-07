class FriendshipResource < ApplicationResource
  attribute :confirmed

  has_one :user
  has_one :friend

  has_one :friendship_setting

  filters :user_id, :friend_id

  # probably should pass user_id in instead of using options
  filter :confirmed_friends, apply: ->(records, value, options) {
    current_user = options[:context][:current_user]&.resource_owner
    Friendship.by_status(value)
  }
  filter :sent, apply: ->(records, _v, options) {
    current_user = options[:context][:current_user]&.resource_owner
    Friendship.sent(current_user&.id)
  }
  filter :received, apply: ->(records, _v, options) {
    current_user = options[:context][:current_user]&.resource_owner
    Friendship.received(current_user&.id)
  }
  filter :friends, apply: ->(records, _v, options) {
    current_user = options[:context][:current_user]&.resource_owner
    Friendship.friends(current_user&.id)
  }
end

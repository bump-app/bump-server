class FriendshipSettingResource < ApplicationResource
  attribute :confirmed

  has_many :friendships
end

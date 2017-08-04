class UserResource < ApplicationResource
  attributes :email, :password, :first_name, :last_name

  has_many :posts
  has_many :comments
  has_many :user_roles
  has_many :friendships
  has_many :friends
  has_many :confirmed_friends
  has_many :received_friendships
  has_many :sent_friendships

  filter :email
  filter :self, apply: ->(records, _v, options) {
    current_user = options[:context][:current_user]&.resource_owner
    records.where(id: current_user&.id) || User.none
  }
  filter :available_users_to_friend, apply: ->(records, _v, options) {
    current_user = options[:context][:current_user]&.resource_owner
    User.available_users_to_friend(current_user)
  }
end

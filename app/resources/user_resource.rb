class UserResource < ApplicationResource
  attributes :email, :password, :first_name, :last_name

  has_many :posts
  has_many :comments
  has_many :user_roles
  has_many :friendships

  filter :email
  filter :self, apply: ->(records, _v, options) {
    current_user = options[:context][:current_user]&.resource_owner
    records.where(id: current_user&.id) || User.none
  }
end

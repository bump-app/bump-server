class UserResource < ApplicationResource
  attributes :email, :password, :first_name, :last_name

  has_many :posts
  has_many :comments
  has_many :user_roles
  has_many :friendships

  filter :email
end

class UserResource < ApplicationResource
  attributes :email, :password, :name_first, :name_last

  has_many :posts
  has_many :comments
  has_many :user_roles

  filter :email
end

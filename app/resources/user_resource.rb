class UserResource < BaseResource
  attributes :email, :password, :name_first, :name_last

  has_many :posts

  filter :email
end

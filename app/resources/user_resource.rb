class UserResource < BaseResource
  attributes :email, :password, :name_first, :name_last

  filter :email
end

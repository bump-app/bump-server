class UserRoleResource < ApplicationResource
  has_one :user
  has_one :role
end

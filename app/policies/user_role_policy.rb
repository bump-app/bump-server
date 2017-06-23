class UserRolePolicy < ApplicationPolicy
  def update?
    false
  end

  def create?
    admin?
  end
  alias_method :destroy?, :create?
end

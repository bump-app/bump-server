class FriendshipSettingPolicy < ApplicationPolicy
  def create?
    owner?
  end

  def update?
    return true if owner?
    true
  end
  alias_method :destroy?, :update?



end

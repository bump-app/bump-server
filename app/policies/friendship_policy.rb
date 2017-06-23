class FriendshipPolicy < ApplicationPolicy
  def create?
    owner?
  end

  def update?
    return true if owner?
    return false unless user
    return false unless record.friend_id == user.id
    return false if record.friend_id_was && record.friend_id_was != user.id
  end
  alias_method :destroy?, :update?
end

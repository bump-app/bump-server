class SubscriptionPolicy < ApplicationPolicy
  def update?
    false
  end

  def create?
    owner?
  end
  alias_method :destroy?, :create?
end

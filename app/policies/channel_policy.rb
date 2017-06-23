class ChannelPolicy < ApplicationPolicy
  def create?
    true
  end

  def update?
    owner? || admin?
  end
  alias_method :destroy?, :update?
end

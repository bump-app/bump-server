class PostPolicy < ApplicationPolicy
  def create?
    true
  end

  def update?
    owner? || admin?
  end
  alias_method :destroy?, :update?

  def editable_attributes(all)
    all - [:link_formatted]
  end
end

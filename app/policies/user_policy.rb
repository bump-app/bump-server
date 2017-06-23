class UserPolicy < ApplicationPolicy
  def create?
    true
  end

  def update?
    user == record || admin?
  end
  alias_method :destroy?, :update?

  def visible_attributes(all)
    if record == user
      all
    else
      all - %i[email password]
    end
  end
end

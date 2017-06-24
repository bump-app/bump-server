class ApplicationPolicy
  attr_reader :user, :record, :token

  def initialize(token, record)
    @token = token
    @record = record
    @user = token&.resource_owner
  end

  def index?
    true
  end

  def show?
    record_scope = record.class.where(id: record.id)
    scope(record_scope).exists?
  end

  def new?
    admin?
  end
  alias_method :create?, :new?
  alias_method :update?, :new?
  alias_method :edit?, :new?
  alias_method :destroy?, :new?

  def scope
    Pundit.policy_scope!(token, record.class)
  end

  def has_scope?(*scopes, accept_all: true)
    acceptable = scopes
    acceptable += [:all] if accept_all
    token&.acceptable?(acceptable)
  end

  def require_scope!(*scopes)
    unless has_scope?(*scopes)
      raise OAuth::ForbiddenTokenError.for_scopes(scopes)
    end
  end

  def admin?(scope = record)
    user&.has_role?(:admin, scope)
  end

  def owner?
    return false unless user && record.respond_to?(:user)
    return false unless record.user_id == user.id
    return false if record.user_id_was && record.user_id_was != user.id
    true
  end

  def policy_for(model)
    Pundit.policy!(token, model)
  end

  class Scope
    attr_reader :user, :scope, :token

    def initialize(token, scope)
      @token = token
      @scope = scope
      @user = token&.resource_owner
    end

    def resolve
      scope
    end

    def admin?
      admin_scope = scope.respond_to?(:model) ? scope.model : scope
      user&.has_role?(:admin, admin_scope)
    end
  end
end

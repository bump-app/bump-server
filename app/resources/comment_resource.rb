class CommentResource < ApplicationResource
  attributes :text, :created_at

  has_one :user
  has_one :post

  filters :user_id, :post_id
end

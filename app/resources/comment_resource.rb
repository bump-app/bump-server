class CommentResource < ApplicationResource
  attribute :text

  has_one :user
  has_one :post

  filters :user_id, :post_id
end

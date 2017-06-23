# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: comments
#
#  id         :integer          not null, primary key
#  text       :text
#  created_at :datetime         not null
#  updated_at :datetime         not null
#  post_id    :integer          not null, indexed
#  user_id    :integer          not null, indexed
#
# Indexes
#
#  index_comments_on_post_id  (post_id)
#  index_comments_on_user_id  (user_id)
#
# rubocop:enable Metrics/LineLength

class Comment < ApplicationRecord
  belongs_to :user, required: true
  belongs_to :post, required: true

  validates :text, length: { maximum: 9_000 }
end

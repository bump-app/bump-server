# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: posts
#
#  id             :integer          not null, primary key
#  link           :string
#  link_formatted :string
#  text           :text
#  created_at     :datetime         not null
#  updated_at     :datetime         not null
#  channel_id     :integer          not null, indexed
#  user_id        :integer          not null, indexed
#
# Indexes
#
#  index_posts_on_channel_id  (channel_id)
#  index_posts_on_user_id     (user_id)
#
# rubocop:enable Metrics/LineLength

class Post < ApplicationRecord
  belongs_to :user, required: true
  belongs_to :channel, required: true

  has_many :comments, dependent: :destroy

  validates :link, :link_formatted, presence: true,
                                    unless: ->(post) { post.text.present? }
  validates :text, presence: true, unless: ->(post) { post.link.present? },
                   length: { maximum: 40_000 }
end

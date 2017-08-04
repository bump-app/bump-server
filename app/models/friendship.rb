# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: friendships
#
#  id         :integer          not null, primary key
#  confirmed  :boolean          default(FALSE), not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#  friend_id  :integer          not null
#  user_id    :integer          not null, indexed
#
# Indexes
#
#  index_friendships_on_user_id  (user_id)
#
# rubocop:enable Metrics/LineLength

class Friendship < ApplicationRecord
  belongs_to :user, required: true
  belongs_to :friend, required: true, class_name: 'User'

  def check_friend_is_different
    if self.user_id == self.friend_id
      errors.add_to_base("Can't add yourself as friend")
    end
  end

  validate :check_friend_is_different
  validates :confirmed, :inclusion => { :in => [true, false] }
  validates_uniqueness_of :user_id, :scope => :friend_id

  scope :by_status, ->(confirmed) { where(confirmed: confirmed) }
  scope :sent, ->(user_id) { where(user_id: user_id).where(confirmed: false) }
  scope :received, ->(user_id) { where(friend_id: user_id).where(confirmed: false) }
  scope :friends, ->(user_id) { where(user_id: user_id).or(where(friend_id: user_id)).where(confirmed: true) }
end

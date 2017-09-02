# == Schema Information
#
# Table name: friendships
#
#  id         :integer          not null, primary key
#  confirmed  :boolean          default(FALSE), not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#  friend_id  :integer          indexed, indexed => [user_id]
#  user_id    :integer          indexed, indexed => [friend_id]
#
# Indexes
#
#  index_friendships_on_friend_id              (friend_id)
#  index_friendships_on_user_id                (user_id)
#  index_friendships_on_user_id_and_friend_id  (user_id,friend_id) UNIQUE
#
# Foreign Keys
#
#  fk_rails_...  (friend_id => users.id)
#  fk_rails_...  (user_id => users.id)
#

class Friendship < ApplicationRecord
  belongs_to :user, required: true
  belongs_to :friend, required: true, class_name: 'User'

  #after_create :create_inverse, unless: :has_inverse?
  #after_destroy :destroy_inverses, if: :has_inverse?

  def create_inverse
    self.class.create(inverse_friendship_options)
  end
  
  def destroy_inverses
    inverses.destroy_all
  end

  def has_inverse?
    self.class.exists?(inverse_friendship_options)
  end

  def inverses
    self.class.where(inverse_friendship_options)
  end

  def inverse_friendship_options
    { friend_id: user_id, user_id: friend_id }
  end

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

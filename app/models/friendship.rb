# == Schema Information
#
# Table name: friendships
#
#  id                    :integer          not null, primary key
#  confirmed             :boolean          default(FALSE), not null
#  created_at            :datetime         not null
#  updated_at            :datetime         not null
#  friend_id             :integer          not null
#  friendship_setting_id :integer
#  user_id               :integer          not null, indexed
#
# Indexes
#
#  index_friendships_on_user_id  (user_id)
#

class Friendship < ApplicationRecord
  belongs_to :user, required: true
  belongs_to :friend, required: true, class_name: 'User'

  belongs_to :friendship_setting, required: false

  #before_create do
    ## need to create the underlying friendship_setting model that describes the
    ## friendship
    #setting = FriendshipSetting.create
    #self.friendship_setting = setting
    #puts "ASDASDASDASDAAAAAAAAAAAAAAAAAAA"
    #puts setting.id
    ##self.save
    #puts setting.id
  #end


  after_create do
    unless has_inverse?
      # need to create the underlying friendship_setting model that describes the
      # friendship.
      # we only create a new friendship_setting for a new pair of records.
        
      setting = FriendshipSetting.create
      self.friendship_setting = setting
      self.save

      create_inverse(self.friendship_setting)
    end
  end
  after_destroy :destroy_inverses, if: :has_inverse?

  def create_inverse(setting)
    inverse = self.class.create(inverse_friendship_options)
    inverse.friendship_setting = setting
    inverse.save
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
  #validates :confirmed, :inclusion => { :in => [true, false] }
  validates_uniqueness_of :user_id, :scope => :friend_id

  scope :by_status, ->(confirmed) { where(confirmed: confirmed) }
  scope :sent, ->(user_id) { where(user_id: user_id).where(confirmed: false) }
  scope :received, ->(user_id) { where(friend_id: user_id).where(confirmed: false) }
  scope :friends, ->(user_id) { where(user_id: user_id).or(where(friend_id: user_id)).where(confirmed: true) }
end

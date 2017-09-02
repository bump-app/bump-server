# == Schema Information
#
# Table name: users
#
#  id              :integer          not null, primary key
#  email           :string           not null, indexed
#  first_name      :string           not null
#  last_name       :string           not null
#  password_digest :string           not null
#  created_at      :datetime         not null
#  updated_at      :datetime         not null
#
# Indexes
#
#  index_users_on_email  (email)
#

class User < ApplicationRecord
  rolify
  has_secure_password

  has_many :user_roles, dependent: :destroy
  has_many :posts, dependent: :destroy
  has_many :comments, dependent: :destroy
  has_many :friendships
  has_many :friends, :through => :friendships, dependent: :destroy
  # not in use and doesn't work
  has_many :sent_friendships, -> (user) { Friendship.sent(user.id) }, class_name: 'Friendship'
  # not in use and doesn't work
  has_many :received_friendships, -> (user) { Friendship.received(user.id) }, class_name: 'Friendship'

  # not in use but works
  has_many :inverse_friendships, :class_name => "Friendship", :foreign_key => "friend_id"
  has_many :inverse_friends,# -> { Friendship.by_status(true) },
    :through => :inverse_friendships, :source => :user

  has_many :confirmed_friends, -> { Friendship.by_status(true) },
    :through => :friendships, 
    :source => :user

  validates :email, presence: true,
                    uniqueness: { case_sensitive: false }, if: :email_changed?
  validates :first_name, :last_name, :password_digest, presence: true

  scope :available_users_to_friend, ->(user) {
    #where.not(id: user.id).where.not(id: user.received_friends.map{ |u| u.id } | user.sent_friends.map{|u| u.id})
  }

  scope :all_friends, ->(user) {
    user.friends#.or( user.inverse_friends )
  }
end

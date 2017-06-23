# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: users
#
#  id              :integer          not null, primary key
#  email           :string           not null, indexed
#  name_first      :string           not null
#  name_last       :string           not null
#  password_digest :string           not null
#  created_at      :datetime         not null
#  updated_at      :datetime         not null
#
# Indexes
#
#  index_users_on_email  (email)
#
# rubocop:enable Metrics/LineLength

class User < ApplicationRecord
  rolify
  has_secure_password

  has_many :user_roles, dependent: :destroy
  has_many :posts, dependent: :destroy
  has_many :comments, dependent: :destroy
  has_many :friendships, dependent: :destroy

  validates :email, presence: true,
                    uniqueness: { case_sensitive: false }, if: :email_changed?
  validates :name_first, :name_last, :password_digest, presence: true
end

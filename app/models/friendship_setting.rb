# == Schema Information
#
# Table name: friendship_settings
#
#  id         :integer          not null, primary key
#  confirmed  :boolean          default(FALSE), not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

class FriendshipSetting < ApplicationRecord
  has_many :friendships
  validates :confirmed, :inclusion => { :in => [true, false] }

  scope :by_status, ->(confirmed) { where(confirmed: confirmed) }
end

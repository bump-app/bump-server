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

FactoryGirl.define do
  factory :friendship do
    friend_id 1
    user
    confirmed { Faker::Boolean.boolean }
  end
end

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

FactoryGirl.define do
  factory :friendship do
    friend_id 1
    user
    confirmed { Faker::Boolean.boolean }
  end
end

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

FactoryGirl.define do
  factory :friendship do
    friend_id 1
    user
    confirmed { Faker::Boolean.boolean }
  end
end

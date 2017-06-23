# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: user_roles
#
#  id         :integer          not null, primary key
#  created_at :datetime         not null
#  updated_at :datetime         not null
#  role_id    :integer          indexed => [user_id]
#  user_id    :integer          indexed => [role_id]
#
# Indexes
#
#  index_user_roles_on_user_id_and_role_id  (user_id,role_id)
#
# rubocop:enable Metrics/LineLength

FactoryGirl.define do
  factory :user_role do
    role_id 1
    user_id 1
  end
end

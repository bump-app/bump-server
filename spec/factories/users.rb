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

FactoryGirl.define do
  factory :user do
    email { Faker::Internet.email }
    password { Faker::Internet.password }
    name_first { Faker::Name.first_name }
    name_last { Faker::Name.last_name }
  end
end

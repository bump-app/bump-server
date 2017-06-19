# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: channels
#
#  id          :integer          not null, primary key
#  description :string           default(""), not null
#  name        :string           not null
#  slug        :string           not null, indexed
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#
# Indexes
#
#  index_channels_on_slug  (slug)
#
# rubocop:enable Metrics/LineLength

FactoryGirl.define do
  factory :channel do
    name { Faker::University.name }
    description { Faker::RickAndMorty.quote }
  end
end

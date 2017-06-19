# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: posts
#
#  id             :integer          not null, primary key
#  link           :string
#  link_formatted :string
#  text           :text
#  created_at     :datetime         not null
#  updated_at     :datetime         not null
#  channel_id     :integer          not null, indexed
#  user_id        :integer          not null, indexed
#
# Indexes
#
#  index_posts_on_channel_id  (channel_id)
#  index_posts_on_user_id     (user_id)
#
# rubocop:enable Metrics/LineLength

FactoryGirl.define do
  factory :post do
    link { Faker::Internet.url }
    link_formatted { Faker::Markdown.random }
    text { Faker::Hipster.paragraph }
    user
    channel
  end
end

# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: subscriptions
#
#  id         :integer          not null, primary key
#  created_at :datetime         not null
#  updated_at :datetime         not null
#  channel_id :integer          not null, indexed
#  user_id    :integer          not null, indexed
#
# Indexes
#
#  index_subscriptions_on_channel_id  (channel_id)
#  index_subscriptions_on_user_id     (user_id)
#
# rubocop:enable Metrics/LineLength

FactoryGirl.define do
  factory :subscription do
    user
    channel
  end
end

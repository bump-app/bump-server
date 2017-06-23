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

require 'rails_helper'

RSpec.describe Subscription do
  pending "add some examples to (or delete) #{__FILE__}"
end

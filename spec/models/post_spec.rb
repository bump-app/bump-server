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

require 'rails_helper'

RSpec.describe Post, type: :model do
  pending "add some examples to (or delete) #{__FILE__}"
end

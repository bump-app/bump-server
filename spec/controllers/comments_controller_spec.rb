# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: comments
#
#  id         :integer          not null, primary key
#  text       :text
#  created_at :datetime         not null
#  updated_at :datetime         not null
#  post_id    :integer          not null, indexed
#  user_id    :integer          not null, indexed
#
# Indexes
#
#  index_comments_on_post_id  (post_id)
#  index_comments_on_user_id  (user_id)
#
# rubocop:enable Metrics/LineLength

require 'rails_helper'

RSpec.describe CommentsController do
end

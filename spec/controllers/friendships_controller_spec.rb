# == Schema Information
#
# Table name: friendships
#
#  id                    :integer          not null, primary key
#  confirmed             :boolean          default(FALSE), not null
#  created_at            :datetime         not null
#  updated_at            :datetime         not null
#  friend_id             :integer          not null
#  friendship_setting_id :integer
#  user_id               :integer          not null, indexed
#
# Indexes
#
#  index_friendships_on_user_id  (user_id)
#

require 'rails_helper'

RSpec.describe FriendshipsController do
end

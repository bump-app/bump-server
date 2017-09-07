# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: friendship_settings
#
#  id         :integer          not null, primary key
#  confirmed  :boolean          default(FALSE), not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#
# rubocop:enable Metrics/LineLength

require 'rails_helper'

RSpec.describe FriendshipSettingsController, type: :controller do

end

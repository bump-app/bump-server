# == Schema Information
#
# Table name: friendship_settings
#
#  id         :integer          not null, primary key
#  confirmed  :boolean          default(FALSE), not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#

require 'rails_helper'

RSpec.describe FriendshipSetting, type: :model do
  pending "add some examples to (or delete) #{__FILE__}"
end

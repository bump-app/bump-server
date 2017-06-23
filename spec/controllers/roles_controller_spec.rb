# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: roles
#
#  id            :integer          not null, primary key
#  name          :string           indexed, indexed => [resource_type, resource_id]
#  resource_type :string           indexed => [name, resource_id]
#  created_at    :datetime
#  updated_at    :datetime
#  resource_id   :integer          indexed => [name, resource_type]
#
# Indexes
#
#  index_roles_on_name                                    (name)
#  index_roles_on_name_and_resource_type_and_resource_id  (name,resource_type,resource_id)
#
# rubocop:enable Metrics/LineLength

require 'rails_helper'

RSpec.describe RolesController do
end

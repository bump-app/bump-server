# == Schema Information
#
# Table name: user_roles
#
#  id         :integer          not null, primary key
#  created_at :datetime         not null
#  updated_at :datetime         not null
#  role_id    :integer          not null, indexed => [user_id]
#  user_id    :integer          not null, indexed => [role_id]
#
# Indexes
#
#  index_user_roles_on_user_id_and_role_id  (user_id,role_id)
#

class UserRole < ApplicationRecord
  belongs_to :user, required: true
  belongs_to :role, required: true
end

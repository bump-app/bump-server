# rubocop:disable Metrics/LineLength
# == Schema Information
#
# Table name: channels
#
#  id          :integer          not null, primary key
#  description :string           default(""), not null
#  name        :string           not null
#  slug        :string           not null, indexed
#  created_at  :datetime         not null
#  updated_at  :datetime         not null
#
# Indexes
#
#  index_channels_on_slug  (slug)
#
# rubocop:enable Metrics/LineLength

class Channel < ApplicationRecord
  include Sluggable

  friendly_id :name, use: %i[slugged finders history]

  has_many :posts, dependent: :destroy

  validates :name, :description, presence: true
end

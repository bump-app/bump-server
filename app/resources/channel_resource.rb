class ChannelResource < ApplicationResource
  include SluggableResource

  attributes :name, :description

  has_many :posts
  has_many :subscribers
end

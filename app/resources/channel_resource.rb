class ChannelResource < BaseResource
  include SluggableResource

  attributes :name, :description

  has_many :posts
end

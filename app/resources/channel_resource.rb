class ChannelResource < BaseResource
  include SluggableResource

  attributes :name, :description
end

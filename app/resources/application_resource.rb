class ApplicationResource < JSONAPI::Resource
  abstract
  include Pundit::Resource
  include AuthenticatedResource

  def self.apply_sort(records, order_options, context = {})
    return records unless order_options.any?

    order_options = order_options.map { |key, direction|
      [key, "#{direction} nulls last"]
    }.to_h

    order_options.each_pair do |field, direction|
      records = if field.to_s.include?('.')
                  super(records, { field => direction }, context)
                else
                  table = records.table_name
                  records.order("#{table}.#{field} #{direction}")
                end
    end
    records
  end
end

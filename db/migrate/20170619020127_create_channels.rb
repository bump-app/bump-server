class CreateChannels < ActiveRecord::Migration[5.0]
  def change
    create_table :channels do |t|
      t.string :slug,         null: false, unique: true, index: true
      t.string :name,         null: false
      t.string :description,  null: false, default: ''

      t.timestamps
    end
  end
end

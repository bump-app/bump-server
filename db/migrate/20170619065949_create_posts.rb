class CreatePosts < ActiveRecord::Migration[5.0]
  def change
    create_table :posts do |t|
      t.string :link
      t.string :link_formatted
      t.text :text
      t.integer :user_id,     null: false, index: true
      t.integer :channel_id,  null: false, index: true

      t.timestamps
    end
  end
end
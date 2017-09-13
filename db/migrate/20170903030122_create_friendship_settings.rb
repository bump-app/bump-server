class CreateFriendshipSettings < ActiveRecord::Migration[5.0]
  def change
      #t.integer :friendship_id
    create_table :friendship_settings do |t|
      t.boolean :confirmed, null: false, default: false
      t.timestamps
    end
  end
end

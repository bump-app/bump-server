class CreateFriendships < ActiveRecord::Migration[5.0]
  def change
    create_table :friendships do |t|
      t.integer :friend_id, null: false
      t.integer :user_id,   null: false, index: true

      t.integer :friendship_setting_id
      t.boolean :confirmed, null: false, default: false

      t.timestamps
    end
  end
end

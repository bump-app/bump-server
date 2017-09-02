class CreateFriendships < ActiveRecord::Migration[5.0]
  def change
    create_table :friendships do |t|
      t.references :user,   index: true, foreign_key: true
      t.references :friend, index: true

      #t.integer :friend_id, null: false
      #t.integer :user_id,   null: false, index: true
      t.boolean :confirmed, null: false, default: false

      t.timestamps
    end

    add_foreign_key :friendships, :users, column: :friend_id
    add_index :friendships, [:user_id, :friend_id], unique: true
  end
end

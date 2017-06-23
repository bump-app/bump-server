class CreateUserRoles < ActiveRecord::Migration[5.0]
  def change
    create_table :user_roles do |t|
      t.integer :role_id, null: false
      t.integer :user_id, null: false

      t.timestamps
    end

    add_index "user_roles", ["user_id", "role_id"], name: "index_user_roles_on_user_id_and_role_id", using: :btree
  end
end

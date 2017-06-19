class CreateUsers < ActiveRecord::Migration[5.0]
  def change
    create_table :users do |t|
      t.string :email,            null: false, index: true
      t.string :name_first,       null: false
      t.string :name_last,        null: false
      t.string :password_digest,  null: false

      t.timestamps
    end
  end
end

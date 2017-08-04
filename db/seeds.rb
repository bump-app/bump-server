Doorkeeper::Application.create(
  name: 'bump-development',
  uid: 'dev',
  secret: '1234',
  redirect_uri: 'urn:ietf:wg:oauth:2.0:oob',
  scopes: 'public'
)

user_list = [
  [ "Will", "Lin", "wlsaidhi@gmail.com", "1234" ],
  [ "Matt", "Dias", "matt@gmail.com", "1234" ],
  [ "Wes", "W", "wes@gmail.com", "1234"],
  [ "A", "A", "a@gmail.com", "1234"],
  [ "B", "B", "b@gmail.com", "1234"],
  [ "C", "C", "c@gmail.com", "1234"]
]

channel_list = [
  "overwatch",
  "funny",
  "pad",
  "music"
]

# user_id, channel_id
subscription_list = [
  [ 1, 1 ],
  [ 1, 2 ],
  [ 2, 1 ],
  [ 2, 3 ],
  [ 3, 1 ]
]

temp_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
post_list = [
  [ "https://www.youtube.com/watch?v=Qt5vWqSFC48", temp_text, 1, 1 ],
  [ "https://www.youtube.com/watch?v=gdx8meu46EE", temp_text, 1, 2 ],
  [ "http://imgur.com/H6kfgP7", temp_text, 2, 1 ]
]

# users
user_list.each do |first_name, last_name, email, password|
  user = User.create(first_name: first_name, 
                  last_name: last_name, 
                  email: email, 
                  password: password,
                  password_confirmation: password)
  #user.save!
end

# channels
channel_list.each do |name|
  Channel.create(name: name, description: "temp")
end

# channel subscriptions
subscription_list.each do |user_id, channel_id|
  Subscription.create(user_id: user_id, channel_id: channel_id)
end

# posts
post_list.each do |link, text, user_id, channel_id|
  Post.create(link: link, text: text, user_id: user_id, channel_id: channel_id)
end

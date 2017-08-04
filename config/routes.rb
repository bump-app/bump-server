Rails.application.routes.draw do
  scope '/api' do
    use_doorkeeper
    jsonapi_resources :users
    jsonapi_resources :roles
    jsonapi_resources :user_roles
    jsonapi_resources :friendships
    jsonapi_resources :channels
    jsonapi_resources :subscriptions
    jsonapi_resources :posts
    jsonapi_resources :comments
  end
end

# == Route Map
#
#                                  Prefix Verb      URI Pattern                                                         Controller#Action
#                                         GET       /api/oauth/authorize/:code(.:format)                                doorkeeper/authorizations#show
#                     oauth_authorization GET       /api/oauth/authorize(.:format)                                      doorkeeper/authorizations#new
#                                         DELETE    /api/oauth/authorize(.:format)                                      doorkeeper/authorizations#destroy
#                                         POST      /api/oauth/authorize(.:format)                                      doorkeeper/authorizations#create
#                             oauth_token POST      /api/oauth/token(.:format)                                          doorkeeper/tokens#create
#                            oauth_revoke POST      /api/oauth/revoke(.:format)                                         doorkeeper/tokens#revoke
#                      oauth_applications GET       /api/oauth/applications(.:format)                                   doorkeeper/applications#index
#                                         POST      /api/oauth/applications(.:format)                                   doorkeeper/applications#create
#                       oauth_application GET       /api/oauth/applications/:id(.:format)                               doorkeeper/applications#show
#                                         PATCH     /api/oauth/applications/:id(.:format)                               doorkeeper/applications#update
#                                         PUT       /api/oauth/applications/:id(.:format)                               doorkeeper/applications#update
#                                         DELETE    /api/oauth/applications/:id(.:format)                               doorkeeper/applications#destroy
#           oauth_authorized_applications GET       /api/oauth/authorized_applications(.:format)                        doorkeeper/authorized_applications#index
#            oauth_authorized_application DELETE    /api/oauth/authorized_applications/:id(.:format)                    doorkeeper/authorized_applications#destroy
#                        oauth_token_info GET       /api/oauth/token/info(.:format)                                     doorkeeper/token_info#show
#                user_relationships_posts GET       /api/users/:user_id/relationships/posts(.:format)                   users#show_relationship {:relationship=>"posts"}
#                                         POST      /api/users/:user_id/relationships/posts(.:format)                   users#create_relationship {:relationship=>"posts"}
#                                         PUT|PATCH /api/users/:user_id/relationships/posts(.:format)                   users#update_relationship {:relationship=>"posts"}
#                                         DELETE    /api/users/:user_id/relationships/posts(.:format)                   users#destroy_relationship {:relationship=>"posts"}
#                              user_posts GET       /api/users/:user_id/posts(.:format)                                 posts#get_related_resources {:relationship=>"posts", :source=>"users"}
#             user_relationships_comments GET       /api/users/:user_id/relationships/comments(.:format)                users#show_relationship {:relationship=>"comments"}
#                                         POST      /api/users/:user_id/relationships/comments(.:format)                users#create_relationship {:relationship=>"comments"}
#                                         PUT|PATCH /api/users/:user_id/relationships/comments(.:format)                users#update_relationship {:relationship=>"comments"}
#                                         DELETE    /api/users/:user_id/relationships/comments(.:format)                users#destroy_relationship {:relationship=>"comments"}
#                           user_comments GET       /api/users/:user_id/comments(.:format)                              comments#get_related_resources {:relationship=>"comments", :source=>"users"}
#           user_relationships_user_roles GET       /api/users/:user_id/relationships/user-roles(.:format)              users#show_relationship {:relationship=>"user_roles"}
#                                         POST      /api/users/:user_id/relationships/user-roles(.:format)              users#create_relationship {:relationship=>"user_roles"}
#                                         PUT|PATCH /api/users/:user_id/relationships/user-roles(.:format)              users#update_relationship {:relationship=>"user_roles"}
#                                         DELETE    /api/users/:user_id/relationships/user-roles(.:format)              users#destroy_relationship {:relationship=>"user_roles"}
#                         user_user_roles GET       /api/users/:user_id/user-roles(.:format)                            user_roles#get_related_resources {:relationship=>"user_roles", :source=>"users"}
#          user_relationships_friendships GET       /api/users/:user_id/relationships/friendships(.:format)             users#show_relationship {:relationship=>"friendships"}
#                                         POST      /api/users/:user_id/relationships/friendships(.:format)             users#create_relationship {:relationship=>"friendships"}
#                                         PUT|PATCH /api/users/:user_id/relationships/friendships(.:format)             users#update_relationship {:relationship=>"friendships"}
#                                         DELETE    /api/users/:user_id/relationships/friendships(.:format)             users#destroy_relationship {:relationship=>"friendships"}
#                        user_friendships GET       /api/users/:user_id/friendships(.:format)                           friendships#get_related_resources {:relationship=>"friendships", :source=>"users"}
#              user_relationships_friends GET       /api/users/:user_id/relationships/friends(.:format)                 users#show_relationship {:relationship=>"friends"}
#                                         POST      /api/users/:user_id/relationships/friends(.:format)                 users#create_relationship {:relationship=>"friends"}
#                                         PUT|PATCH /api/users/:user_id/relationships/friends(.:format)                 users#update_relationship {:relationship=>"friends"}
#                                         DELETE    /api/users/:user_id/relationships/friends(.:format)                 users#destroy_relationship {:relationship=>"friends"}
#                            user_friends GET       /api/users/:user_id/friends(.:format)                               users#get_related_resources {:relationship=>"friends", :source=>"users"}
#    user_relationships_confirmed_friends GET       /api/users/:user_id/relationships/confirmed-friends(.:format)       users#show_relationship {:relationship=>"confirmed_friends"}
#                                         POST      /api/users/:user_id/relationships/confirmed-friends(.:format)       users#create_relationship {:relationship=>"confirmed_friends"}
#                                         PUT|PATCH /api/users/:user_id/relationships/confirmed-friends(.:format)       users#update_relationship {:relationship=>"confirmed_friends"}
#                                         DELETE    /api/users/:user_id/relationships/confirmed-friends(.:format)       users#destroy_relationship {:relationship=>"confirmed_friends"}
#                  user_confirmed_friends GET       /api/users/:user_id/confirmed-friends(.:format)                     users#get_related_resources {:relationship=>"confirmed_friends", :source=>"users"}
# user_relationships_received_friendships GET       /api/users/:user_id/relationships/received-friendships(.:format)    users#show_relationship {:relationship=>"received_friendships"}
#                                         POST      /api/users/:user_id/relationships/received-friendships(.:format)    users#create_relationship {:relationship=>"received_friendships"}
#                                         PUT|PATCH /api/users/:user_id/relationships/received-friendships(.:format)    users#update_relationship {:relationship=>"received_friendships"}
#                                         DELETE    /api/users/:user_id/relationships/received-friendships(.:format)    users#destroy_relationship {:relationship=>"received_friendships"}
#               user_received_friendships GET       /api/users/:user_id/received-friendships(.:format)                  friendships#get_related_resources {:relationship=>"received_friendships", :source=>"users"}
#     user_relationships_sent_friendships GET       /api/users/:user_id/relationships/sent-friendships(.:format)        users#show_relationship {:relationship=>"sent_friendships"}
#                                         POST      /api/users/:user_id/relationships/sent-friendships(.:format)        users#create_relationship {:relationship=>"sent_friendships"}
#                                         PUT|PATCH /api/users/:user_id/relationships/sent-friendships(.:format)        users#update_relationship {:relationship=>"sent_friendships"}
#                                         DELETE    /api/users/:user_id/relationships/sent-friendships(.:format)        users#destroy_relationship {:relationship=>"sent_friendships"}
#                   user_sent_friendships GET       /api/users/:user_id/sent-friendships(.:format)                      friendships#get_related_resources {:relationship=>"sent_friendships", :source=>"users"}
#                                   users GET       /api/users(.:format)                                                users#index
#                                         POST      /api/users(.:format)                                                users#create
#                                    user GET       /api/users/:id(.:format)                                            users#show
#                                         PATCH     /api/users/:id(.:format)                                            users#update
#                                         PUT       /api/users/:id(.:format)                                            users#update
#                                         DELETE    /api/users/:id(.:format)                                            users#destroy
#           role_relationships_user_roles GET       /api/roles/:role_id/relationships/user-roles(.:format)              roles#show_relationship {:relationship=>"user_roles"}
#                                         POST      /api/roles/:role_id/relationships/user-roles(.:format)              roles#create_relationship {:relationship=>"user_roles"}
#                                         PUT|PATCH /api/roles/:role_id/relationships/user-roles(.:format)              roles#update_relationship {:relationship=>"user_roles"}
#                                         DELETE    /api/roles/:role_id/relationships/user-roles(.:format)              roles#destroy_relationship {:relationship=>"user_roles"}
#                         role_user_roles GET       /api/roles/:role_id/user-roles(.:format)                            user_roles#get_related_resources {:relationship=>"user_roles", :source=>"roles"}
#             role_relationships_resource GET       /api/roles/:role_id/relationships/resource(.:format)                roles#show_relationship {:relationship=>"resource"}
#                                         PUT|PATCH /api/roles/:role_id/relationships/resource(.:format)                roles#update_relationship {:relationship=>"resource"}
#                                         DELETE    /api/roles/:role_id/relationships/resource(.:format)                roles#destroy_relationship {:relationship=>"resource"}
#                           role_resource GET       /api/roles/:role_id/resource(.:format)                              resources#get_related_resource {:relationship=>"resource", :source=>"roles"}
#                                   roles GET       /api/roles(.:format)                                                roles#index
#                                         POST      /api/roles(.:format)                                                roles#create
#                                    role GET       /api/roles/:id(.:format)                                            roles#show
#                                         PATCH     /api/roles/:id(.:format)                                            roles#update
#                                         PUT       /api/roles/:id(.:format)                                            roles#update
#                                         DELETE    /api/roles/:id(.:format)                                            roles#destroy
#            user_role_relationships_user GET       /api/user-roles/:user_role_id/relationships/user(.:format)          user_roles#show_relationship {:relationship=>"user"}
#                                         PUT|PATCH /api/user-roles/:user_role_id/relationships/user(.:format)          user_roles#update_relationship {:relationship=>"user"}
#                                         DELETE    /api/user-roles/:user_role_id/relationships/user(.:format)          user_roles#destroy_relationship {:relationship=>"user"}
#                          user_role_user GET       /api/user-roles/:user_role_id/user(.:format)                        users#get_related_resource {:relationship=>"user", :source=>"user_roles"}
#            user_role_relationships_role GET       /api/user-roles/:user_role_id/relationships/role(.:format)          user_roles#show_relationship {:relationship=>"role"}
#                                         PUT|PATCH /api/user-roles/:user_role_id/relationships/role(.:format)          user_roles#update_relationship {:relationship=>"role"}
#                                         DELETE    /api/user-roles/:user_role_id/relationships/role(.:format)          user_roles#destroy_relationship {:relationship=>"role"}
#                          user_role_role GET       /api/user-roles/:user_role_id/role(.:format)                        roles#get_related_resource {:relationship=>"role", :source=>"user_roles"}
#                              user_roles GET       /api/user-roles(.:format)                                           user_roles#index
#                                         POST      /api/user-roles(.:format)                                           user_roles#create
#                               user_role GET       /api/user-roles/:id(.:format)                                       user_roles#show
#                                         PATCH     /api/user-roles/:id(.:format)                                       user_roles#update
#                                         PUT       /api/user-roles/:id(.:format)                                       user_roles#update
#                                         DELETE    /api/user-roles/:id(.:format)                                       user_roles#destroy
#           friendship_relationships_user GET       /api/friendships/:friendship_id/relationships/user(.:format)        friendships#show_relationship {:relationship=>"user"}
#                                         PUT|PATCH /api/friendships/:friendship_id/relationships/user(.:format)        friendships#update_relationship {:relationship=>"user"}
#                                         DELETE    /api/friendships/:friendship_id/relationships/user(.:format)        friendships#destroy_relationship {:relationship=>"user"}
#                         friendship_user GET       /api/friendships/:friendship_id/user(.:format)                      users#get_related_resource {:relationship=>"user", :source=>"friendships"}
#         friendship_relationships_friend GET       /api/friendships/:friendship_id/relationships/friend(.:format)      friendships#show_relationship {:relationship=>"friend"}
#                                         PUT|PATCH /api/friendships/:friendship_id/relationships/friend(.:format)      friendships#update_relationship {:relationship=>"friend"}
#                                         DELETE    /api/friendships/:friendship_id/relationships/friend(.:format)      friendships#destroy_relationship {:relationship=>"friend"}
#                       friendship_friend GET       /api/friendships/:friendship_id/friend(.:format)                    users#get_related_resource {:relationship=>"friend", :source=>"friendships"}
#                             friendships GET       /api/friendships(.:format)                                          friendships#index
#                                         POST      /api/friendships(.:format)                                          friendships#create
#                              friendship GET       /api/friendships/:id(.:format)                                      friendships#show
#                                         PATCH     /api/friendships/:id(.:format)                                      friendships#update
#                                         PUT       /api/friendships/:id(.:format)                                      friendships#update
#                                         DELETE    /api/friendships/:id(.:format)                                      friendships#destroy
#             channel_relationships_posts GET       /api/channels/:channel_id/relationships/posts(.:format)             channels#show_relationship {:relationship=>"posts"}
#                                         POST      /api/channels/:channel_id/relationships/posts(.:format)             channels#create_relationship {:relationship=>"posts"}
#                                         PUT|PATCH /api/channels/:channel_id/relationships/posts(.:format)             channels#update_relationship {:relationship=>"posts"}
#                                         DELETE    /api/channels/:channel_id/relationships/posts(.:format)             channels#destroy_relationship {:relationship=>"posts"}
#                           channel_posts GET       /api/channels/:channel_id/posts(.:format)                           posts#get_related_resources {:relationship=>"posts", :source=>"channels"}
#       channel_relationships_subscribers GET       /api/channels/:channel_id/relationships/subscribers(.:format)       channels#show_relationship {:relationship=>"subscribers"}
#                                         POST      /api/channels/:channel_id/relationships/subscribers(.:format)       channels#create_relationship {:relationship=>"subscribers"}
#                                         PUT|PATCH /api/channels/:channel_id/relationships/subscribers(.:format)       channels#update_relationship {:relationship=>"subscribers"}
#                                         DELETE    /api/channels/:channel_id/relationships/subscribers(.:format)       channels#destroy_relationship {:relationship=>"subscribers"}
#                     channel_subscribers GET       /api/channels/:channel_id/subscribers(.:format)                     subscriptions#get_related_resources {:relationship=>"subscribers", :source=>"channels"}
#                                channels GET       /api/channels(.:format)                                             channels#index
#                                         POST      /api/channels(.:format)                                             channels#create
#                                 channel GET       /api/channels/:id(.:format)                                         channels#show
#                                         PATCH     /api/channels/:id(.:format)                                         channels#update
#                                         PUT       /api/channels/:id(.:format)                                         channels#update
#                                         DELETE    /api/channels/:id(.:format)                                         channels#destroy
#         subscription_relationships_user GET       /api/subscriptions/:subscription_id/relationships/user(.:format)    subscriptions#show_relationship {:relationship=>"user"}
#                                         PUT|PATCH /api/subscriptions/:subscription_id/relationships/user(.:format)    subscriptions#update_relationship {:relationship=>"user"}
#                                         DELETE    /api/subscriptions/:subscription_id/relationships/user(.:format)    subscriptions#destroy_relationship {:relationship=>"user"}
#                       subscription_user GET       /api/subscriptions/:subscription_id/user(.:format)                  users#get_related_resource {:relationship=>"user", :source=>"subscriptions"}
#      subscription_relationships_channel GET       /api/subscriptions/:subscription_id/relationships/channel(.:format) subscriptions#show_relationship {:relationship=>"channel"}
#                                         PUT|PATCH /api/subscriptions/:subscription_id/relationships/channel(.:format) subscriptions#update_relationship {:relationship=>"channel"}
#                                         DELETE    /api/subscriptions/:subscription_id/relationships/channel(.:format) subscriptions#destroy_relationship {:relationship=>"channel"}
#                    subscription_channel GET       /api/subscriptions/:subscription_id/channel(.:format)               channels#get_related_resource {:relationship=>"channel", :source=>"subscriptions"}
#                           subscriptions GET       /api/subscriptions(.:format)                                        subscriptions#index
#                                         POST      /api/subscriptions(.:format)                                        subscriptions#create
#                            subscription GET       /api/subscriptions/:id(.:format)                                    subscriptions#show
#                                         PATCH     /api/subscriptions/:id(.:format)                                    subscriptions#update
#                                         PUT       /api/subscriptions/:id(.:format)                                    subscriptions#update
#                                         DELETE    /api/subscriptions/:id(.:format)                                    subscriptions#destroy
#                 post_relationships_user GET       /api/posts/:post_id/relationships/user(.:format)                    posts#show_relationship {:relationship=>"user"}
#                                         PUT|PATCH /api/posts/:post_id/relationships/user(.:format)                    posts#update_relationship {:relationship=>"user"}
#                                         DELETE    /api/posts/:post_id/relationships/user(.:format)                    posts#destroy_relationship {:relationship=>"user"}
#                               post_user GET       /api/posts/:post_id/user(.:format)                                  users#get_related_resource {:relationship=>"user", :source=>"posts"}
#              post_relationships_channel GET       /api/posts/:post_id/relationships/channel(.:format)                 posts#show_relationship {:relationship=>"channel"}
#                                         PUT|PATCH /api/posts/:post_id/relationships/channel(.:format)                 posts#update_relationship {:relationship=>"channel"}
#                                         DELETE    /api/posts/:post_id/relationships/channel(.:format)                 posts#destroy_relationship {:relationship=>"channel"}
#                            post_channel GET       /api/posts/:post_id/channel(.:format)                               channels#get_related_resource {:relationship=>"channel", :source=>"posts"}
#             post_relationships_comments GET       /api/posts/:post_id/relationships/comments(.:format)                posts#show_relationship {:relationship=>"comments"}
#                                         POST      /api/posts/:post_id/relationships/comments(.:format)                posts#create_relationship {:relationship=>"comments"}
#                                         PUT|PATCH /api/posts/:post_id/relationships/comments(.:format)                posts#update_relationship {:relationship=>"comments"}
#                                         DELETE    /api/posts/:post_id/relationships/comments(.:format)                posts#destroy_relationship {:relationship=>"comments"}
#                           post_comments GET       /api/posts/:post_id/comments(.:format)                              comments#get_related_resources {:relationship=>"comments", :source=>"posts"}
#                                   posts GET       /api/posts(.:format)                                                posts#index
#                                         POST      /api/posts(.:format)                                                posts#create
#                                    post GET       /api/posts/:id(.:format)                                            posts#show
#                                         PATCH     /api/posts/:id(.:format)                                            posts#update
#                                         PUT       /api/posts/:id(.:format)                                            posts#update
#                                         DELETE    /api/posts/:id(.:format)                                            posts#destroy
#              comment_relationships_user GET       /api/comments/:comment_id/relationships/user(.:format)              comments#show_relationship {:relationship=>"user"}
#                                         PUT|PATCH /api/comments/:comment_id/relationships/user(.:format)              comments#update_relationship {:relationship=>"user"}
#                                         DELETE    /api/comments/:comment_id/relationships/user(.:format)              comments#destroy_relationship {:relationship=>"user"}
#                            comment_user GET       /api/comments/:comment_id/user(.:format)                            users#get_related_resource {:relationship=>"user", :source=>"comments"}
#              comment_relationships_post GET       /api/comments/:comment_id/relationships/post(.:format)              comments#show_relationship {:relationship=>"post"}
#                                         PUT|PATCH /api/comments/:comment_id/relationships/post(.:format)              comments#update_relationship {:relationship=>"post"}
#                                         DELETE    /api/comments/:comment_id/relationships/post(.:format)              comments#destroy_relationship {:relationship=>"post"}
#                            comment_post GET       /api/comments/:comment_id/post(.:format)                            posts#get_related_resource {:relationship=>"post", :source=>"comments"}
#                                comments GET       /api/comments(.:format)                                             comments#index
#                                         POST      /api/comments(.:format)                                             comments#create
#                                 comment GET       /api/comments/:id(.:format)                                         comments#show
#                                         PATCH     /api/comments/:id(.:format)                                         comments#update
#                                         PUT       /api/comments/:id(.:format)                                         comments#update
#                                         DELETE    /api/comments/:id(.:format)                                         comments#destroy
# 

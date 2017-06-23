Rails.application.routes.draw do
  scope '/api' do
    use_doorkeeper
    jsonapi_resources :users
    jsonapi_resources :roles
    jsonapi_resources :user_roles
    jsonapi_resources :channels
    jsonapi_resources :posts
  end
end

# == Route Map
#
#                        Prefix Verb      URI Pattern                                                Controller#Action
#                               GET       /api/oauth/authorize/:code(.:format)                       doorkeeper/authorizations#show
#           oauth_authorization GET       /api/oauth/authorize(.:format)                             doorkeeper/authorizations#new
#                               DELETE    /api/oauth/authorize(.:format)                             doorkeeper/authorizations#destroy
#                               POST      /api/oauth/authorize(.:format)                             doorkeeper/authorizations#create
#                   oauth_token POST      /api/oauth/token(.:format)                                 doorkeeper/tokens#create
#                  oauth_revoke POST      /api/oauth/revoke(.:format)                                doorkeeper/tokens#revoke
#            oauth_applications GET       /api/oauth/applications(.:format)                          doorkeeper/applications#index
#                               POST      /api/oauth/applications(.:format)                          doorkeeper/applications#create
#             oauth_application GET       /api/oauth/applications/:id(.:format)                      doorkeeper/applications#show
#                               PATCH     /api/oauth/applications/:id(.:format)                      doorkeeper/applications#update
#                               PUT       /api/oauth/applications/:id(.:format)                      doorkeeper/applications#update
#                               DELETE    /api/oauth/applications/:id(.:format)                      doorkeeper/applications#destroy
# oauth_authorized_applications GET       /api/oauth/authorized_applications(.:format)               doorkeeper/authorized_applications#index
#  oauth_authorized_application DELETE    /api/oauth/authorized_applications/:id(.:format)           doorkeeper/authorized_applications#destroy
#              oauth_token_info GET       /api/oauth/token/info(.:format)                            doorkeeper/token_info#show
#      user_relationships_posts GET       /api/users/:user_id/relationships/posts(.:format)          users#show_relationship {:relationship=>"posts"}
#                               POST      /api/users/:user_id/relationships/posts(.:format)          users#create_relationship {:relationship=>"posts"}
#                               PUT|PATCH /api/users/:user_id/relationships/posts(.:format)          users#update_relationship {:relationship=>"posts"}
#                               DELETE    /api/users/:user_id/relationships/posts(.:format)          users#destroy_relationship {:relationship=>"posts"}
#                    user_posts GET       /api/users/:user_id/posts(.:format)                        posts#get_related_resources {:relationship=>"posts", :source=>"users"}
# user_relationships_user_roles GET       /api/users/:user_id/relationships/user-roles(.:format)     users#show_relationship {:relationship=>"user_roles"}
#                               POST      /api/users/:user_id/relationships/user-roles(.:format)     users#create_relationship {:relationship=>"user_roles"}
#                               PUT|PATCH /api/users/:user_id/relationships/user-roles(.:format)     users#update_relationship {:relationship=>"user_roles"}
#                               DELETE    /api/users/:user_id/relationships/user-roles(.:format)     users#destroy_relationship {:relationship=>"user_roles"}
#               user_user_roles GET       /api/users/:user_id/user-roles(.:format)                   user_roles#get_related_resources {:relationship=>"user_roles", :source=>"users"}
#                         users GET       /api/users(.:format)                                       users#index
#                               POST      /api/users(.:format)                                       users#create
#                          user GET       /api/users/:id(.:format)                                   users#show
#                               PATCH     /api/users/:id(.:format)                                   users#update
#                               PUT       /api/users/:id(.:format)                                   users#update
#                               DELETE    /api/users/:id(.:format)                                   users#destroy
# role_relationships_user_roles GET       /api/roles/:role_id/relationships/user-roles(.:format)     roles#show_relationship {:relationship=>"user_roles"}
#                               POST      /api/roles/:role_id/relationships/user-roles(.:format)     roles#create_relationship {:relationship=>"user_roles"}
#                               PUT|PATCH /api/roles/:role_id/relationships/user-roles(.:format)     roles#update_relationship {:relationship=>"user_roles"}
#                               DELETE    /api/roles/:role_id/relationships/user-roles(.:format)     roles#destroy_relationship {:relationship=>"user_roles"}
#               role_user_roles GET       /api/roles/:role_id/user-roles(.:format)                   user_roles#get_related_resources {:relationship=>"user_roles", :source=>"roles"}
#   role_relationships_resource GET       /api/roles/:role_id/relationships/resource(.:format)       roles#show_relationship {:relationship=>"resource"}
#                               PUT|PATCH /api/roles/:role_id/relationships/resource(.:format)       roles#update_relationship {:relationship=>"resource"}
#                               DELETE    /api/roles/:role_id/relationships/resource(.:format)       roles#destroy_relationship {:relationship=>"resource"}
#                 role_resource GET       /api/roles/:role_id/resource(.:format)                     resources#get_related_resource {:relationship=>"resource", :source=>"roles"}
#                         roles GET       /api/roles(.:format)                                       roles#index
#                               POST      /api/roles(.:format)                                       roles#create
#                          role GET       /api/roles/:id(.:format)                                   roles#show
#                               PATCH     /api/roles/:id(.:format)                                   roles#update
#                               PUT       /api/roles/:id(.:format)                                   roles#update
#                               DELETE    /api/roles/:id(.:format)                                   roles#destroy
#  user_role_relationships_user GET       /api/user-roles/:user_role_id/relationships/user(.:format) user_roles#show_relationship {:relationship=>"user"}
#                               PUT|PATCH /api/user-roles/:user_role_id/relationships/user(.:format) user_roles#update_relationship {:relationship=>"user"}
#                               DELETE    /api/user-roles/:user_role_id/relationships/user(.:format) user_roles#destroy_relationship {:relationship=>"user"}
#                user_role_user GET       /api/user-roles/:user_role_id/user(.:format)               users#get_related_resource {:relationship=>"user", :source=>"user_roles"}
#  user_role_relationships_role GET       /api/user-roles/:user_role_id/relationships/role(.:format) user_roles#show_relationship {:relationship=>"role"}
#                               PUT|PATCH /api/user-roles/:user_role_id/relationships/role(.:format) user_roles#update_relationship {:relationship=>"role"}
#                               DELETE    /api/user-roles/:user_role_id/relationships/role(.:format) user_roles#destroy_relationship {:relationship=>"role"}
#                user_role_role GET       /api/user-roles/:user_role_id/role(.:format)               roles#get_related_resource {:relationship=>"role", :source=>"user_roles"}
#                    user_roles GET       /api/user-roles(.:format)                                  user_roles#index
#                               POST      /api/user-roles(.:format)                                  user_roles#create
#                     user_role GET       /api/user-roles/:id(.:format)                              user_roles#show
#                               PATCH     /api/user-roles/:id(.:format)                              user_roles#update
#                               PUT       /api/user-roles/:id(.:format)                              user_roles#update
#                               DELETE    /api/user-roles/:id(.:format)                              user_roles#destroy
#   channel_relationships_posts GET       /api/channels/:channel_id/relationships/posts(.:format)    channels#show_relationship {:relationship=>"posts"}
#                               POST      /api/channels/:channel_id/relationships/posts(.:format)    channels#create_relationship {:relationship=>"posts"}
#                               PUT|PATCH /api/channels/:channel_id/relationships/posts(.:format)    channels#update_relationship {:relationship=>"posts"}
#                               DELETE    /api/channels/:channel_id/relationships/posts(.:format)    channels#destroy_relationship {:relationship=>"posts"}
#                 channel_posts GET       /api/channels/:channel_id/posts(.:format)                  posts#get_related_resources {:relationship=>"posts", :source=>"channels"}
#                      channels GET       /api/channels(.:format)                                    channels#index
#                               POST      /api/channels(.:format)                                    channels#create
#                       channel GET       /api/channels/:id(.:format)                                channels#show
#                               PATCH     /api/channels/:id(.:format)                                channels#update
#                               PUT       /api/channels/:id(.:format)                                channels#update
#                               DELETE    /api/channels/:id(.:format)                                channels#destroy
#       post_relationships_user GET       /api/posts/:post_id/relationships/user(.:format)           posts#show_relationship {:relationship=>"user"}
#                               PUT|PATCH /api/posts/:post_id/relationships/user(.:format)           posts#update_relationship {:relationship=>"user"}
#                               DELETE    /api/posts/:post_id/relationships/user(.:format)           posts#destroy_relationship {:relationship=>"user"}
#                     post_user GET       /api/posts/:post_id/user(.:format)                         users#get_related_resource {:relationship=>"user", :source=>"posts"}
#    post_relationships_channel GET       /api/posts/:post_id/relationships/channel(.:format)        posts#show_relationship {:relationship=>"channel"}
#                               PUT|PATCH /api/posts/:post_id/relationships/channel(.:format)        posts#update_relationship {:relationship=>"channel"}
#                               DELETE    /api/posts/:post_id/relationships/channel(.:format)        posts#destroy_relationship {:relationship=>"channel"}
#                  post_channel GET       /api/posts/:post_id/channel(.:format)                      channels#get_related_resource {:relationship=>"channel", :source=>"posts"}
#                         posts GET       /api/posts(.:format)                                       posts#index
#                               POST      /api/posts(.:format)                                       posts#create
#                          post GET       /api/posts/:id(.:format)                                   posts#show
#                               PATCH     /api/posts/:id(.:format)                                   posts#update
#                               PUT       /api/posts/:id(.:format)                                   posts#update
#                               DELETE    /api/posts/:id(.:format)                                   posts#destroy
#

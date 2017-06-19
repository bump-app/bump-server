Rails.application.routes.draw do
  scope '/api' do
    jsonapi_resources :users
    jsonapi_resources :channels
  end
end

# == Route Map
#
#   Prefix Verb   URI Pattern                 Controller#Action
#    users GET    /api/users(.:format)        users#index
#          POST   /api/users(.:format)        users#create
#     user GET    /api/users/:id(.:format)    users#show
#          PATCH  /api/users/:id(.:format)    users#update
#          PUT    /api/users/:id(.:format)    users#update
#          DELETE /api/users/:id(.:format)    users#destroy
# channels GET    /api/channels(.:format)     channels#index
#          POST   /api/channels(.:format)     channels#create
#  channel GET    /api/channels/:id(.:format) channels#show
#          PATCH  /api/channels/:id(.:format) channels#update
#          PUT    /api/channels/:id(.:format) channels#update
#          DELETE /api/channels/:id(.:format) channels#destroy
#

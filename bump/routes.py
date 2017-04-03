from bump.users.resource import UserList, UserDetail, UserRelationship
from bump.channels.resource import ChannelList, ChannelDetail, ChannelRelationship
from bump.subscriptions.resource import SubscriptionList, SubscriptionDetail, SubscriptionRelationship
from bump.posts.resource import PostList, PostDetail, PostRelationship
from bump.comments.resource import CommentList, CommentDetail, CommentRelationship

def Route(api):
	# users
	api.route(UserList, 'user_list', '/users')
	api.route(UserDetail, 'user_detail', '/users/<int:id>')
	api.route(UserRelationship, 'user_subscriptions', '/users/<int:id>/relationships/subscriptions')
	api.route(UserRelationship, 'user_posts', '/users/<int:id>/relationships/posts')
	api.route(UserRelationship, 'user_comments', '/users/<int:id>/relationships/comments')

	# channels
	api.route(ChannelList, 'channel_list', '/channels')
	api.route(ChannelDetail, 'channel_detail', '/channels/<int:id>')
	api.route(ChannelRelationship, 'channel_subscribers', '/channels/<int:id>/relationships/subscribers')
	api.route(ChannelRelationship, 'channel_posts', '/channels/<int:id>/relationships/posts')

	# subscriptions
	api.route(SubscriptionList, 'subscription_list', '/subscriptions')
	api.route(SubscriptionDetail, 'subscription_detail', '/subscriptions/<int:id>')
	api.route(SubscriptionRelationship, 'subscription_user', '/subscriptions/<int:id>/relationships/user')
	api.route(SubscriptionRelationship, 'subscription_channel', '/subscriptions/<int:id>/relationships/channel')

	# posts
	api.route(PostList, 'post_list', '/posts')
	api.route(PostDetail, 'post_detail', '/posts/<int:id>')
	api.route(PostRelationship, 'post_user', '/posts/<int:id>/relationships/user')
	api.route(PostRelationship, 'post_channel', '/posts/<int:id>/relationships/channel')
	api.route(PostRelationship, 'post_comments', '/posts/<int:id>/relationships/comments')

	# comments
	api.route(CommentList, 'comment_list', '/comments')
	api.route(CommentDetail, 'comment_detail', '/comments/<int:id>')
	api.route(CommentRelationship, 'comment_user', '/comments/<int:id>/relationships/user')
	api.route(CommentRelationship, 'comment_post', '/comments/<int:id>/relationships/post')

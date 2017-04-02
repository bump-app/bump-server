from bump.users.resource import UserList, UserDetail, UserRelationship
from bump.posts.resource import PostList, PostDetail, PostRelationship
from bump.comments.resource import CommentList, CommentDetail, CommentRelationship
from bump.channels.resource import ChannelList, ChannelDetail, ChannelRelationship

def Route(api):
	# users
	api.route(UserList, 'user_list', '/users')
	api.route(UserDetail, 'user_detail', '/users/<int:id>')
	api.route(UserRelationship, 'user_posts', '/users/<int:id>/relationships/posts')
	api.route(UserRelationship, 'user_comments', '/users/<int:id>/relationships/comments')

	# posts
	api.route(PostList, 'post_list', '/posts')
	api.route(PostDetail, 'post_detail', '/posts/<int:id>')
	api.route(PostRelationship, 'post_user', '/posts/<int:id>/relationships/user')
	api.route(PostRelationship, 'post_comments', '/posts/<int:id>/relationships/comments')

	# comments
	api.route(CommentList, 'comment_list', '/comments')
	api.route(CommentDetail, 'comment_detail', '/comments/<int:id>')
	api.route(CommentRelationship, 'comment_user', '/comments/<int:id>/relationships/user')
	api.route(CommentRelationship, 'comment_post', '/comments/<int:id>/relationships/post')

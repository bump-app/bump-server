from bump import DB as db
# from bump.auth.client import Client
from bump.users.model import User
from bump.channels.model import Channel
from bump.posts.model import Post

def seed():
	# test client
	# test_client = Client(	id="test",
	# 						secret="fWT4BneGtcENqNRgRQRujouX",
	# 						name="test",
	# 						is_confidential="false")
	# db.session.add(test_client)

	# users
	matt = User(name="matthewdias",
				email="matthewdias@asdf.com",
				password="totallysecurepassword",
				_role=1,
				status=2)

	# channels
	overwatch = Channel(name="overwatch",
						description="overwatch description")

	pad = Channel(name="pad",
						description="pad description")

	# posts
	p1 = Post(	link="https://www.youtube.com/watch?v=Qt5vWqSFC48",
				text="1text",
				user=matt,
				channel=overwatch)

	try:
		db.session.add(matt)
		db.session.add(overwatch)
		db.session.add(pad)
		db.session.add(p1)
		db.session.commit()
	except:
		db.session.rollback()

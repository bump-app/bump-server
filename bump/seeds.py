from bump import DB as db
# from bump.auth.client import Client
from bump.users.model import User

def seed():
	# test_client = Client(	id="test",
	# 						secret="fWT4BneGtcENqNRgRQRujouX",
	# 						name="test",
	# 						is_confidential="false")
	# db.session.add(test_client)

	matt = User(name="matthewdias",
				email="matthewdias@asdf.com",
				password="totallysecurepassword",
				_role=1,
				status=2)
	db.session.add(matt)

	try:
		db.session.commit()
	except:
		db.session.rollback()

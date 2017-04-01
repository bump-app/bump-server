from bump import DB as db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(POST.COMMENT_LENGTH))
    rating = db.Column(db.Integer)
    time_posted = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, db.ForeignKey('post_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user_id'))

    def __init__(self, text=None, post_id=None, user_id=None):
        self.text = text
        self.post_id = post_id
        self.user_id = user_id

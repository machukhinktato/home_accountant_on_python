class User:
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())


class Account():
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(140), unique=True)
    income = db.Column(db.String())
    created = db.Column(db.DateTime, default=datetime.now())

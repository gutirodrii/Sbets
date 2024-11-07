from . import db

class Odds(db.Model):
    __tablename__ = 'odds'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    bookmaker_id = db.Column(db.Integer, db.ForeignKey('bookmakers.id'), nullable=False)
    market = db.Column(db.String(50))
    odds_home_win = db.Column(db.Float)
    odds_draw = db.Column(db.Float)
    odds_away_win = db.Column(db.Float)
    last_update = db.Column(db.DateTime)

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    sport = db.Column(db.String(50))
    league = db.Column(db.String(100))
    home_team = db.Column(db.String(100))
    away_team = db.Column(db.String(100))
    event_date = db.Column(db.DateTime)
    # odds = db.Column(db.relationship('Odds', backref='event', lazy=True))

class Bookmaker(db.Model):
    __tablename__ = 'bookmakers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    # odds = db.Column(db.relationship('Odds', backref='bookmaker', lazy=True))
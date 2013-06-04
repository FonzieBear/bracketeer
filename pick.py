import contestant
import gambler

class Pick(db.Model):
  gambler_id = db.ReferenceProperty(gambler.Gambler)
  contestant_id = db.ReferenceProperty(contestant.Contestant)
  position = db.IntegerProperty()


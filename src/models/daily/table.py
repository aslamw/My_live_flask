from .. import db, ma, User
import datetime

class Daily(db.Model):
    __tablename__ = "my_daily"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    annotation = db.Column(db.Text)
    date_created = db.Column(db.DateTime, default=datetime.datetime.now())
    
    def __init__(self, id_user, annotation):
        
        self.id_user :int = id_user
        self.annotation :str = annotation

class DailySchema(ma.Schema):
    class Meta:
        fields = ("id", "id_user", "annotation", "date_created")
        
daily_shema = DailySchema()
dailys_shema = DailySchema(many=True)
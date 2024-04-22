from ext import db, app
from datetime import datetime


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.String)
    img = db.Column(db.String)
    


    def validate(self):
        if not super().validate():
            return False

        # If img field is provided or it's a new product, return True
        if self.img.data or not self.data.get('id'):
            return True
        
        # If img field is not provided and it's an existing product, return True
        return False


class AddPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    
    img = db.Column(db.String)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.now)


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    file = db.Column(db.String)
    
    


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
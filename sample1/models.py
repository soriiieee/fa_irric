from sample1 import db , login_manager
from flask_bcrypt import generate_password_hash,check_password_hash
from flask_login import UserMixin


@login_manager.user_loader #セッションに保存されたユーザを返す
def load_user(user_id):
    return User.query.get(user_id)


class User(UserMixin,db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64), index=True)
    password = db.Column(db.String(128))

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password = generate_password_hash(password)
    
    ##ココから個別に設定した内容
    def validate_password(self,password):
        ##暗号化済みのpasswordとasciiのパスワードの整合性を比較する
        return check_password_hash(self.password , password)
    
    def add_user(self):
        with db.session.begin(subtransactions = True):
            db.session.add(self)
        db.session.commit()

    @classmethod
    def select_by_email(cls,email):
        return cls.query.filter_by(email = email).first()
    

    

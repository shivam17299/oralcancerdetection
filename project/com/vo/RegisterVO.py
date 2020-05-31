from project import db
from project.com.vo.LoginVO import LoginVO


class RegisterVO(db.Model):
    pass
    __tablename__ = 'registermaster'
    registerId = db.Column('registerId', db.Integer, primary_key=True, autoincrement=True)
    registerName = db.Column('registerName', db.String(100), nullable=False)
    # registerUsername = db.Column('registerUsername', db.String(100), nullable=False)
    registerGender = db.Column('registerGender', db.String(100), nullable=False)
    registerNumber = db.Column('registerNumber', db.String(100), nullable=False)

    register_LoginId = db.Column('register_LoginId', db.Integer, db.ForeignKey(LoginVO.loginId))

    def as_dict(self):
        return {
            'registerId': self.registerId,
            'registerName': self.registerName,
            # 'registerUsername': self.registerUsername,
            'registerGender': self.registerGender,
            'registerNumber': self.registerNumber,
            'loginPassword': self.loginPassword,
            'register_LoginId': self.register_LoginId
        }


db.create_all()

from project import db
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO


class RegisterDAO:

    def insertRegister(self, registerVO):
        db.session.add(registerVO)
        db.session.commit()

    def viewRegister(self):
        registerList = db.session.query(RegisterVO, LoginVO) \
            .join(LoginVO, RegisterVO.register_LoginId == LoginVO.loginId).all()
        return registerList

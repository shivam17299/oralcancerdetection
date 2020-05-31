import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import request, render_template

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.LoginVO import LoginVO
from project.com.vo.RegisterVO import RegisterVO


@app.route('/user/insertRegister', methods=['POST'])
def userInsertRegister():
    error = None
    # try:
    loginVO = LoginVO()
    loginDAO = LoginDAO()

    registerVO = RegisterVO()
    registerDAO = RegisterDAO()

    loginUsername = request.form['loginUsername']

    registerName = request.form['registerName']
    # registerLastname = request.form['registerLastname']
    registerGender = request.form['registerGender']

    registerNumber = request.form['registerNumber']

    loginPassword = request.form['loginPassword']
    #     ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
    #
    # print("loginPassword=" + loginPassword)

    try:

        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginRole = "user"
        loginVO.loginStatus = "active"
        loginDAO.insertLogin(loginVO)

        # registerVO.registerFirstname = registerFirstname
        registerVO.registerName = registerName
        registerVO.registerGender = registerGender
        registerVO.registerNumber = registerNumber
        registerVO.register_LoginId = loginVO.loginId

        registerDAO.insertRegister(registerVO)

    except:
        msg = "Username already exist"

    # if (error == None):
    #     sender = "oralcancerdetection@gmail.com"
    #
    #     receiver = loginUsername
    #
    #     msg = MIMEMultipart()
    #
    #     msg['From'] = sender
    #
    #     msg['To'] = receiver
    #
    #     msg['Subject'] = "PYTHON PASSWORD"
    #
    #     msg.attach(MIMEText(loginPassword, 'plain'))
    #
    #     server = smtplib.SMTP('smtp.gmail.com', 587)
    #
    #     server.starttls()
    #
    #     server.login(sender, "ocd@1234")
    #
    #     text = msg.as_string()
    #
    #     server.sendmail(sender, receiver, text)
    #
    #     server.quit()

    return render_template("admin/Login.html", error=error)


# except Exception as e:
# print(e)


@app.route('/admin/viewUser', methods=['get'])
def adminViewUser():
    try:

        if adminLoginSession() == 'admin':
            registerDAO = RegisterDAO()

            registerVOList = registerDAO.viewRegister()
            return render_template('admin/viewUser.html', registerVOList=registerVOList)
        else:
            adminLogoutSession()
            return render_template('admin/login.html')

    except Exception as e:
        print(e)

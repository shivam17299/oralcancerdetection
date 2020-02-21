import os
from datetime import datetime

from flask import render_template, redirect, url_for, request, session
from werkzeug.utils import secure_filename

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.ComplainDAO import ComplainDAO
from project.com.vo.ComplainVO import ComplainVO


# Admin side app routes

@app.route('/admin/viewComplain')
def adminViewComplain():
    try:
        if adminLoginSession() == "admin":
            complainVO = ComplainVO()
            complainVO.complainStatus = 'pending'
            complainDAO = ComplainDAO()
            complainVOList = complainDAO.adminViewComplain(complainVO)
            return render_template("admin/viewComplain.html", complainVOList=complainVOList)
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route("/admin/loadComplainReply")
def adminLoadComplainReply():
    try:
        if adminLoginSession() == "admin":
            complainVO = ComplainVO()
            complainId = request.args.get("complainId")
            return render_template('admin/addComplainReply.html', complainId=complainId)
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route("/admin/insertComplainReply", methods=['POST'])
def adminInsertComplainReply():
    try:
        if adminLoginSession() == "admin":

            now = datetime.now()
            UPLOAD_FOLDER = "project/static/adminResource/reply/"
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            complainId = request.form['complainId']
            replySubject = request.form['replySubject']
            replyMessage = request.form['replyMessage']
            replyFile = request.files['replyFile']

            replyFileName = secure_filename(replyFile.filename)

            replyFilePath = os.path.join(app.config['UPLOAD_FOLDER'])

            replyFile.save(os.path.join(replyFilePath, replyFileName))

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainVO.complainId = complainId
            complainVO.replySubject = replySubject
            complainVO.replyMessage = replyMessage
            complainVO.replyDate = now.strftime("%d/%m/%Y")
            complainVO.replyTime = now.strftime("%H:%M:%S")
            complainVO.replyFileName = replyFileName
            complainVO.replyFilePath = replyFilePath.replace("project", "..")
            complainVO.complainStatus = 'replied'
            complainVO.complainTo_LoginId = session['session_loginId']

            complainDAO.insertComplainReply(complainVO)

            return redirect('/admin/viewComplain')
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


# User side app routes

@app.route("/user/loadComplain")
def userLoadComplain():
    try:
        if adminLoginSession() == "user":
            return render_template('user/addComplain.html')
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route("/user/insertComplain", methods=['POST'])
def userInsertComplain():
    try:
        if adminLoginSession() == "user":
            print("inside insert complain")
            now = datetime.now()
            UPLOAD_FOLDER = "project/static/adminResource/complain/"
            app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

            complainSubject = request.form['complainSubject']
            print(complainSubject)
            complainDescription = request.form['complainDescription']
            print(complainDescription)
            complainFile = request.files['complainFile']
            print(complainFile)

            complainFileName = secure_filename(complainFile.filename)

            complainFilePath = os.path.join(app.config['UPLOAD_FOLDER'])

            complainFile.save(os.path.join(complainFilePath, complainFileName))

            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainVO.complainSubject = complainSubject
            complainVO.complainDescription = complainDescription
            complainVO.complainDate = now.strftime("%d/%m/%Y")
            complainVO.complainTime = now.strftime("%H:%M:%S")
            complainVO.complainStatus = "pending"
            complainVO.complainFileName = complainFileName
            complainVO.complainFilePath = complainFilePath.replace("project", "..")
            complainVO.complainFrom_LoginId = session['session_loginId']

            complainDAO.userInsertComplain(complainVO)

            return redirect(url_for("userViewComplain"))
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route("/user/viewComplain", methods=['GET'])
def userViewComplain():
    try:
        if adminLoginSession() == 'user':
            complainVO = ComplainVO()
            complainDAO = ComplainDAO()
            complainVO.complainFrom_LoginId = session['session_loginId']
            complainVOList = complainDAO.userViewComplain(complainVO)
            return render_template("user/viewComplain.html", complainVOList=complainVOList)
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route("/user/deleteComplain")
def userDeleteComplain():
    try:
        if adminLoginSession() == "user":
            complainDAO = ComplainDAO()
            complainVO = ComplainVO()

            complainId = request.args.get("complainId")

            complainVO.complainId = complainId
            complainList = complainDAO.deleteComplain(complainVO)

            if complainList.complainFileName is not None:
                complainFile = complainList.complainFilePath.replace("..", "project") + complainList.complainFileName
                os.remove(complainFile)

            if complainList.replyFileName is not None:
                replyFile = complainList.replyFilePath.replace("..", "project") + complainList.replyFileName
                os.remove(replyFile)

            return redirect(url_for("userViewComplain"))
        else:
            return redirect(url_for("adminLogoutSession"))

    except Exception as ex:
        print(ex)


@app.route("/user/viewComplainReply")
def userViewComplainReply():
    try:
        if adminLoginSession() == "user":
            complainVO = ComplainVO()
            complainDAO = ComplainDAO()

            complainId = request.args.get("complainId")

            complainVO.complainId = complainId

            complainReplyList = complainDAO.viewComplainReply(complainVO)
            return render_template("user/viewComplainReply.html", complainReplyList=complainReplyList)
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)

from datetime import datetime

from flask import render_template, url_for, redirect, request, session

from project import app
from project.com.controller.LoginController import adminLoginSession
from project.com.dao.FeedbackDAO import FeedbackDAO
from project.com.vo.FeedbackVO import FeedbackVO


# USER SIDE URL PATTERNS

@app.route("/user/loadFeedback")
def userLoadFeedback():
    try:
        if adminLoginSession() == "user":
            return render_template('user/addFeedback.html')
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route("/user/insertFeedback", methods=['GET', 'POST'])
def userInsertFeedback():
    try:
        if adminLoginSession() == "user":
            now = datetime.now()

            feedbackSubject = request.form['feedbackSubject']
            print(feedbackSubject)
            feedbackDescription = request.form['feedbackDescription']
            feedbackRating = request.form['rate']

            feedbackDate = now.strftime("%d/%m/%Y")
            feedbackTime = now.strftime("%H:%M:%S")
            feedbackFrom_LoginId = session['session_loginId']

            feedbackVO = FeedbackVO()
            feedbackDAO = FeedbackDAO()

            feedbackVO.feedbackSubject = feedbackSubject
            feedbackVO.feedbackDescription = feedbackDescription
            feedbackVO.feedbackRating = feedbackRating
            feedbackVO.feedbackDate = feedbackDate
            feedbackVO.feedbackTime = feedbackTime
            feedbackVO.feedbackFrom_LoginId = feedbackFrom_LoginId

            feedbackDAO.insertFeedback(feedbackVO)

            return redirect(url_for("userViewFeedback"))
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route("/user/viewFeedback", methods=['GET'])
def userViewFeedback():
    try:
        if adminLoginSession() == 'user':
            feedbackDAO = FeedbackDAO()
            feedbackVO = FeedbackVO()

            feedbackFrom_LoginId = session['session_loginId']
            feedbackVO.feedbackFrom_LoginId = feedbackFrom_LoginId

            feedbackVOList = feedbackDAO.userViewFeedback(feedbackVO)
            return render_template("user/viewFeedback.html", feedbackVOList=feedbackVOList)
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route("/user/deleteFeedback")
def userDeleteFeedback():
    try:
        if adminLoginSession() == "user":
            feedbackDAO = FeedbackDAO()
            feedbackVO = FeedbackVO()

            feedbackId = request.args.get("feedbackId")

            feedbackVO.feedbackId = feedbackId
            feedbackDAO.deleteFeedback(feedbackVO)

            return redirect(url_for("userViewFeedback"))
        else:
            return redirect(url_for("adminLogoutSession"))

    except Exception as ex:
        print(ex)


# ADMIN SIDE URL PATTERNS

@app.route('/admin/viewFeedback')
def adminViewFeedback():
    try:
        if adminLoginSession() == "admin":
            feedbackDAO = FeedbackDAO()
            FeedbackVOList = feedbackDAO.adminViewFeedback()
            return render_template("admin/viewFeedback.html", FeedbackVOList=FeedbackVOList)
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)


@app.route('/admin/reviewFeedback')
def adminReviewFeedback():
    try:
        if adminLoginSession() == "admin":
            feedbackVO = FeedbackVO()
            feedbackDAO = FeedbackDAO()

            feedbackId = request.args.get("feedbackId")
            feedbackTo_LoginId = session['session_loginId']

            feedbackVO.feedbackTo_LoginId = feedbackTo_LoginId
            feedbackVO.feedbackId = feedbackId

            feedbackDAO.adminReviewFeedback(feedbackVO)

            return redirect(url_for('adminViewFeedback'))
        else:
            return redirect(url_for("adminLogoutSession"))
    except Exception as ex:
        print(ex)

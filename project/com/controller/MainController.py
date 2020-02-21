from flask import render_template

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession


@app.route('/')
def adminLogin():
    try:
        return render_template('admin/login.html')
    except Exception as ex:
        print(ex)


@app.route('/admin/loadDataset')
def adminLoadDataset():
    try:

        if adminLoginSession() == 'admin':
            return render_template('admin/addDataset.html')
        else:
            adminLogoutSession()
            return render_template('admin/login.html')

    except Exception as e:
        print(e)


@app.route('/admin/viewImage')
def adminViewImage():
    try:
        if adminLoginSession() == 'admin':
            return render_template('admin/viewImage.html')
        else:
            adminLogoutSession()
            return render_template('admin/login.html')

    except Exception as e:
        print(e)


#
# @app.route('/admin/viewComplain')
# def adminViewComplain():
#     try:
#
#         if adminLoginSession() == 'admin':
#             return render_template('admin/viewComplain.html')
#         else:
#             adminLogoutSession()
#             return render_template('admin/login.html')
#
#     except Exception as e:
#         print(e)
#
#
# @app.route('/admin/viewFeedback')
# def adminViewFeedback():
#     try:
#         if adminLoginSession() == 'admin':
#             return render_template('admin/viewFeedback.html')
#         else:
#             adminLogoutSession()
#             return render_template('admin/login.html')
#
#     except Exception as e:
#         print(e)
#
#
@app.route('/user/addComplain')
def userAddComplain():
    try:

        if adminLoginSession() == 'user':
            return render_template('user/addComplain.html')
        else:
            adminLogoutSession()
            return render_template('user/login.html')

    except Exception as e:
        print(e)


#
# @app.route('/user/viewComplain')
# def userViewComplain():
#     try:
#
#         if adminLoginSession() == 'user':
#             return render_template('user/viewComplain.html')
#         else:
#             adminLogoutSession()
#             return render_template('user/login.html')
#
#     except Exception as e:
#         print(e)
#
#
@app.route('/user/addFeedback')
def userAddFeedback():
    try:
        if adminLoginSession() == 'user':
            return render_template('user/addFeedback.html')
        else:
            adminLogoutSession()
            return render_template('user/login.html')

    except Exception as e:
        print(e)


#
#
# @app.route('/user/viewFeedback')
# def userViewFeedback():
#     try:
#         if adminLoginSession() == 'user':
#             return render_template('user/viewFeedback.html')
#         else:
#             adminLogoutSession()
#             return render_template('user/login.html')
#
#     except Exception as e:
#         print(e)


@app.route('/user/viewDetection')
def userViewDetection():
    try:
        if adminLoginSession() == 'user':
            return render_template('user/viewDetection.html')
        else:
            adminLogoutSession()
            return render_template('user/login.html')

    except Exception as e:
        print(e)


@app.route('/user/addImage')
def userAddImage():
    try:
        if adminLoginSession() == 'user':
            return render_template('user/addImage.html')
        else:
            adminLogoutSession()
            return render_template('user/login.html')

    except Exception as e:
        print(e)


@app.route('/user/viewImage')
def userViewImage():
    try:
        if adminLoginSession() == 'user':
            return render_template('user/viewImage.html')
        else:
            adminLogoutSession()
            return render_template('user/login.html')

    except Exception as e:
        print(e)


@app.route('/user/registration')
def userRegistration():
    try:
        # if adminLoginSession()=='user':
        return render_template('user/register.html')
    # else:
    #     adminLogoutSession()
    #     return render_template('user/login.html')

    except Exception as e:
        print(e)


@app.route('/user/viewReply')
def userViewReply():
    try:
        if adminLoginSession() == 'user':
            return render_template('user/viewComplainReply.html')
        else:
            adminLogoutSession()
            return render_template('user/login.html')

    except Exception as e:
        print(e)

#
# @app.route('/admin/registration' , )
# def adminRegistration():
#     try:
#         # if adminLoginSession()=='user':
#             return render_template('admin/register.html')
#         # else:
#         #     adminLogoutSession()
#         #     return render_template('user/login.html')
#
#     except Exception as e:
#         print(e)

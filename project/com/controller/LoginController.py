from flask import request, render_template, redirect, url_for, session

from project import app
from project.com.dao.LoginDAO import LoginDAO
from project.com.dao.RegisterDAO import RegisterDAO
from project.com.vo.LoginVO import LoginVO


@app.route('/', methods=['get'])
def adminLoadLogin():
    try:
        return render_template('admin/login.html')
    except Exception as ex:
        print(ex)


@app.route('/admin/validateLogin', methods=['post'])
def adminValidateLogin():
    try:

        loginUsername = request.form['loginUsername']
        loginPassword = request.form['loginPassword']

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginStatus = "active"

        loginVOList = loginDAO.validateLogin(loginVO)

        loginDictList = [i.as_dict() for i in loginVOList]

        print(loginDictList)

        lenLoginDictList = len(loginDictList)

        if lenLoginDictList == 0:

            msg = 'Username Or Password is Incorrect !'

            return render_template('admin/login.html', error=msg)

        elif loginDictList[0]['loginStatus'] == 'inactive':
            msg = 'You are temporarily blocked by admin !'

            return render_template('admin/login.html', error=msg)


        else:

            for row1 in loginDictList:

                loginId = row1['loginId']

                loginUsername = row1['loginUsername']

                loginRole = row1['loginRole']

                session['session_loginId'] = loginId

                session['session_loginUsername'] = loginUsername

                session['session_loginRole'] = loginRole

                session.permanent = True

                if loginRole == 'admin':
                    return redirect(url_for('adminLoadDashboard'))
                elif loginRole == 'user':
                    return redirect(url_for('userLoadDashboard'))

    except Exception as ex:
        print(ex)


@app.route('/admin/loadDashboard')
def adminLoadDashboard():
    try:
        if adminLoginSession() == 'admin':

            return render_template('admin/index.html')
        else:
            adminLogoutSession()
            return render_template('admin/login.html')

    except Exception as ex:
        print(ex)


@app.route('/admin/loginSession')
def adminLoginSession():
    try:
        if 'session_loginId' and 'session_loginRole' in session:

            if session['session_loginRole'] == 'admin':

                return 'admin'
            elif session['session_loginRole'] == 'user':

                return 'user'

            print("<<<<<<<<<<<<<<<<True>>>>>>>>>>>>>>>>>>>>")

        else:

            print("<<<<<<<<<<<<<<<<False>>>>>>>>>>>>>>>>>>>>")

            return False
    except Exception as ex:
        print(ex)


@app.route('/admin/logoutSession')
def adminLogoutSession():
    try:
        session.clear()
        return redirect(url_for('adminLoadLogin'))
    except Exception as ex:
        print(ex)


@app.route('/user/loadDashboard')
def userLoadDashboard():
    try:
        if adminLoginSession() == 'user':

            return render_template('user/index.html')
        else:
            adminLogoutSession()
            return render_template('user/login.html')

    except Exception as ex:
        print(ex)


@app.route('/user/validateLogin', methods=['post'])
def userValidateLogin():
    try:

        loginUsername = request.form['loginUsername']
        loginPassword = request.form['loginPassword']

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginVO.loginUsername = loginUsername
        loginVO.loginPassword = loginPassword
        loginVO.loginStatus = "active"

        loginVOList = loginDAO.validateLogin(loginVO)

        loginDictList = [i.as_dict() for i in loginVOList]

        print(loginDictList)

        lenLoginDictList = len(loginDictList)

        if lenLoginDictList == 0:

            msg = 'Username Or Password is Incorrect !'

            return render_template('user/login.html', error=msg)

        else:

            for row1 in loginDictList:

                loginId = row1['loginId']

                loginUsername = row1['loginUsername']

                loginRole = row1['loginRole']

                session['session_loginId'] = loginId

                session['session_loginUsername'] = loginUsername

                session['session_loginRole'] = loginRole

                session.permanent = True

                if loginRole == 'admin':
                    return redirect(url_for('adminLoadDashboard'))
                elif loginRole == 'user':
                    return redirect(url_for('userLoadDashboard'))

    except Exception as ex:
        print(ex)


@app.route('/user/loginSession')
def userLoginSession():
    try:
        if 'session_loginId' and 'session_loginRole' in session:

            if session['session_loginRole'] == 'admin':

                return 'admin'
            elif session['session_loginRole'] == 'user':

                return 'user'

            print("<<<<<<<<<<<<<<<<True>>>>>>>>>>>>>>>>>>>>")

        else:

            print("<<<<<<<<<<<<<<<<False>>>>>>>>>>>>>>>>>>>>")

            return False
    except Exception as ex:
        print(ex)


@app.route('/user/logoutSession')
def userLogoutSession():
    try:
        session.clear()
        return redirect(url_for('adminLoadLogin'))
    except Exception as ex:
        print(ex)


@app.route('/admin/unblockUser', methods=['get'])
def adminunblockUser():
    try:

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginId = request.args.get('loginId')

        print('loginId::', loginId)

        loginVO.loginId = loginId

        registerDAO = RegisterDAO()

        loginVO.loginRole = 'user'
        loginVO.loginStatus = 'active'

        loginDAO.validateLogin(loginVO)
        registerDAO.viewRegister()
        loginDAO.unblockUser(loginVO)

        return redirect(url_for('adminViewUser'))


    except Exception as ex:
        print(ex)


@app.route('/admin/blockUser', methods=['get'])
def adminblockUser():
    try:

        loginVO = LoginVO()
        loginDAO = LoginDAO()

        loginId = request.args.get('loginId')

        print('loginId::', loginId)

        loginVO.loginId = loginId

        registerDAO = RegisterDAO()

        loginVO.loginRole = 'user'
        loginVO.loginStatus = 'inactive'

        loginDAO.validateLogin(loginVO)
        registerDAO.viewRegister()
        loginDAO.blockUser(loginVO)

        return redirect(url_for('adminViewUser'))


    except Exception as ex:
        print(ex)

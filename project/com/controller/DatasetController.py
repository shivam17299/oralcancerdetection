import os
from datetime import datetime

from flask import *
from werkzeug.utils import secure_filename

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.DatasetVO import DatasetVO
from project.static.adminResource.dataset.check_model import main

UPLOAD_FOLDER = 'project/static/adminResource/dataset/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/admin/insertDataset', methods=['POST'])
def adminInsertDataset():
    try:
        if adminLoginSession() == 'admin':
            datasetVO = DatasetVO()
            datasetDAO = DatasetDAO()

            now = datetime.now()
            print("now=", now)
            date = now.strftime("%d/%m/%Y")
            time = now.strftime("%H:%M:%S")

            dataset = request.files['dataset']
            print(dataset)

            datasetFileName = secure_filename(dataset.filename)
            print(datasetFileName)

            datasetpath = os.path.join(app.config['UPLOAD_FOLDER'])
            print(datasetpath)

            dataset.save(os.path.join(app.config['UPLOAD_FOLDER'], datasetFileName))

            datasetVO.datasetFileName = datasetFileName

            datasetVO.datasetFilePath = datasetpath
            datasetVO.datasetUploadDate = date
            datasetVO.datasetUploadTime = time

            datasetDAO.insertDataset(datasetVO)

            return redirect(url_for('adminViewDataset'))
        else:
            adminLogoutSession()
            return render_template('admin/login.html')
    except Exception as ex:
        print(ex)


@app.route('/admin/viewDataset', methods=['GET'])
def adminViewDataset():
    try:
        if adminLoginSession() == 'admin':
            datasetDAO = DatasetDAO()
            datasetVOList = datasetDAO.viewDataset()
            print("__________________", datasetVOList)
            return render_template('/admin/viewDataset.html', datasetVOList=datasetVOList)
        else:
            adminLogoutSession()
            return render_template('admin/login.html')


    except Exception as ex:
        print(ex)


@app.route('/admin/deleteDataset', methods=['GET'])
def adminDeleteDataset():
    try:
        if adminLoginSession() == 'admin':

            datasetVO = DatasetVO()

            datasetDAO = DatasetDAO()

            datasetId = request.args.get('datasetId')

            datasetVO.datasetId = datasetId

            datasetFileList = datasetDAO.deleteDataset(datasetVO)

            path = datasetFileList.datasetFilePath + datasetFileList.datasetFileName

            os.remove(path)

            return redirect(url_for('adminViewDataset'))
        else:
            adminLogoutSession()
            return render_template('admin/login.html')

    except Exception as ex:
        print(ex)


@app.route('/user/insertDataset', methods=['POST'])
def userInsertDataset():
    # try:
    if adminLoginSession() == 'user':
        datasetVO = DatasetVO()
        datasetDAO = DatasetDAO()

        now = datetime.now()
        print("now=", now)
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")

        dataset = request.files['image']
        print(dataset)

        datasetFileName = secure_filename(dataset.filename)
        print(datasetFileName)

        datasetpath = os.path.join(app.config['UPLOAD_FOLDER'])
        print(datasetpath)

        dataset.save(os.path.join(app.config['UPLOAD_FOLDER'], datasetFileName))

        datasetVO.datasetFileName = datasetFileName

        datasetVO.datasetFilePath = datasetpath
        datasetVO.datasetUploadDate = date
        datasetVO.datasetUploadTime = time

        datasetDAO.insertDataset(datasetVO)
        result = main(os.path.join(datasetpath, datasetFileName))
        print(result)
        return render_template('user/viewDetection.html', imagepath=os.path.join( "../static/adminResource/dataset", datasetFileName),
                               result=result)
    else:
        adminLogoutSession()
        return render_template('admin/login.html')


# except Exception as ex:
#   print(ex)


@app.route('/user/viewDataset', methods=['GET'])
def userViewDataset():
    try:
        if adminLoginSession() == 'user':
            datasetDAO = DatasetDAO()
            datasetVOList = datasetDAO.viewDataset()
            print("__________________", datasetVOList)
            return render_template('/user/viewImage.html', datasetVOList=datasetVOList)
        else:
            adminLogoutSession()
            return render_template('admin/login.html')


    except Exception as ex:
        print(ex)

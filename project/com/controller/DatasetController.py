import os
from datetime import datetime

from flask import *
from werkzeug.utils import secure_filename

from project import app
from project.com.controller.LoginController import adminLoginSession, adminLogoutSession
from project.com.dao.DatasetDAO import DatasetDAO
from project.com.vo.DatasetVO import DatasetVO

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

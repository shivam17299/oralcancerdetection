from project import db
from project.com.vo.DatasetVO import DatasetVO


class DatasetDAO:

    def insertDataset(self, datasetVO):
        db.session.add(datasetVO)
        db.session.commit()

    def viewDataset(self):
        datasetList = DatasetVO.query.all()

        return datasetList

    def deleteDataset(self, datasetVO):
        datasetFileList = DatasetVO.query.get(datasetVO.datasetId)

        db.session.delete(datasetFileList)

        db.session.commit()

        return datasetFileList

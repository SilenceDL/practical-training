from sklearn.externals import joblib
class lrModel():

    def __init__(self):
        self.le= joblib.load("G:\practical-training-main\machine_learning\model\le.model")
        self.model = joblib.load("G:\practical-training-main\machine_learning\model\lr.model")

    def wage_pred(self,area, exp, xueli):
        area_index = list(self.le.classes_).index(area)
        xueli_index = list(('中专', '高中', '大专', '本科', "硕士")).index(xueli)
        wage_pred = self.model.predict([[area_index, exp, xueli_index]])
        return '%.2f'%wage_pred[0]

if __name__ == '__main__':
    lm =lrModel()
    print(lm.wage_pred('保定',2,'本科'))
from sklearn.preprocessing import LabelEncoder as LE
from sklearn.linear_model import LinearRegression as LR
import pandas as pd
from sklearn.externals import joblib
# 将各字符分类变量重编码为数值分类变量
class jobsModel():



    def train_model(self):
        le = LE()
        jobs = pd.read_excel("train.xls")
        jobs['Location'] = le.fit_transform(jobs['Location'].values)  # 城市重编码

        jobs['Education'] = jobs['Education'].replace('中专', 0)  # 学历重编码
        jobs['Education'] = jobs['Education'].replace('高中', 1)
        jobs['Education'] = jobs['Education'].replace('大专', 2)
        jobs['Education'] = jobs['Education'].replace('本科', 3)
        jobs['Education'] = jobs['Education'].replace('硕士', 4)
        ## 特征选择
        X = jobs[['Location', 'Education', 'Experience']]
        ## 结果集
        y = jobs['Salary']

        ## 模型学习
        model = LR()
        model.fit(X, y)
        joblib.dump(le, "G:\practical-training-main\machine_learning\model\le.model")
        joblib.dump(model, "G:\practical-training-main\machine_learning\model\lr.model")


##构建预测函数


    def load_model(self):
        le = joblib.load("G:\practical-training-main\machine_learning\model\le.model")
        model = joblib.load("G:\practical-training-main\machine_learning\model\lr.model")
        return le, model


## 测试代码
if __name__ == '__main__':
    jm= jobsModel()
    # jm.train_model()
    le, model = jm.load_model()




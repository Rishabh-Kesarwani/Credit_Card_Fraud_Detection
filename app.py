from types import MethodType
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data1= request.form['Limit_Balance']
        data2= request.form['Sex']
        data3= request.form['education']
        data4= request.form['marriage']
        data5= request.form['age']
        data6= request.form['pay1']
        data7= request.form['pay2']
        data8= request.form['pay3']
        data9= request.form['pay4']
        data10= request.form['pay5']
        data11= request.form['pay6']
        data12= request.form['bill1']
        data13= request.form['bill2']
        data14= request.form['bill3']
        data15= request.form['bill4']
        data16= request.form['bill5']
        data17= request.form['bill6']
        data18= request.form['PrevPay1']
        data19= request.form['PrevPay2']
        data20= request.form['PrevPay3']
        data21= request.form['PrevPay4']
        data22= request.form['PrevPay5']
        data23= request.form['PrevPay6']

        arr=np.array([[data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16,data17,data18,data19,data20,data21,data22,data23]])
        # arr=[np.array(int_features)]
        val1=pd.DataFrame(data=arr,index=None,columns=None)
        res=model.predict(val1)
        return render_template('after.html', data=res[0])

if __name__=="__main__" :
    app.run(debug=True)
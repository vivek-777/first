from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#bussiness logics here
def hello(request):
    return HttpResponse("hello ji")
#print html contents
def myhtml(request):
    return HttpResponse("<h1>this is my web page</h1>")
#reciving parameters from GET request

#how to call--->>>http://127.0.0.1:2221/demo1?name=shubham&age=21&mobile=9453625122
def predict_marks(request):
#recive hrs studied
    hrs=int(request.GET["hours"])
#implement machine learning
#stage1-read data into data frame
    import pandas as pd
    df=pd.read_csv("/home/users/vvs/desktop/first/first_app/Grade_Set.csv")
#stage 2-->>>selection
    import numpy as np
    x=df.Hours_Studied[:,np.newaxis]#independent
    y=df.Test_Grade.values#dependent
    #stage --5 Data mining
   #linear regression
    import sklearn.linear_model as lm
    from sklearn.metrics import r2_score
#create linear regression equation
    model=lm.LinearRegression()
    #fit the model
    model.fit(x,y)#train th equation
    marks=model.predict(hrs)#retur the exams
    marks=int(marks[0])
#accuracy 
    accuracy=r2_score(y,model.predict(x))
    response="<h1>student who studey for "+str(hrs)+ " hours will socore= " +str(marks)+ " accuracy of the output is " +str(accuracy)+ "<h1"
    return HttpResponse(response)


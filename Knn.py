import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
#this algorithm is so easy with sklearn
class Knn :
    def __init__(self) -> None:
        data = datasets.load_iris().data
        target = datasets.load_iris().target
        self.train_x,self.test_x,self.train_y,self.test_y=train_test_split(data,target,test_size=0.2)
        self.trainer = KNeighborsClassifier()
        self.trainer.fit(self.train_x,self.train_y)
#Now we can predit by the trainer

#But can we realize it with numpy? Of course sure
#in this part, we also get dataset by sklearn
x = datasets.load_iris().data
y = datasets.load_iris().target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1)


# this function refers to the KNN 
def predict(x_pre,x_train,y_train):
    x_tmp = []

    #caculate the distance 
    for items in x_train:
        distance = 0.0
        for i in range(4):
            distance+=(items[i]-x_pre[i])**2
        x_tmp.append(distance)
    temp = []

    # sort
    for i in range(len(x_tmp)):
        temp.append([x_tmp[i],y_train[i]])
    judge1 = np.array(temp)
    index = np.argsort(temp,axis=0)
    judge = judge1[index[:,0]]
    
    #establish a dict to help us make dicision
    judge_dict = {}
    for i in range(5):
        if judge[i][1] not in judge_dict.keys():
            judge_dict[judge[i][1]]=0
        else:
            judge_dict[judge[i][1]]+=1
    
    #make decision
    target = 0
    max = judge_dict[judge[0][1]]
    for i in judge_dict.keys():
        if max < judge_dict[i]:
            max = judge_dict[i]
            target = i
    return target   
    
#test

if __name__=='__main__':
    predict([1,1,1,1],x_train=x_train,y_train=y_train)

import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import shape
from scipy.sparse import data
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from Linear import Myerror
#Sigmod: 1/(1+e^(-z))
# z = WT*X
def Sigmod(w,x):
    try:
        if np.shape(w)[1]!=np.shape(x)[1]:
            raise Myerror
    except Myerror:
        Myerror.__printmessage__()
    wt = np.transpose(w)
    z = np.dot(x,wt)
    # print(z)
    return 1.0/(1.0+np.exp((-1)*z))



class Logistics:
    def __init__(self) -> None:
        data = datasets.load_breast_cancer()
        featrue_data = data.data
        target= data.target 
        self.train_x,self.test_x,self.train_y,self.test_y = train_test_split(featrue_data,target,test_size=0.2)
        sc = StandardScaler()
        self.train_x =sc.fit_transform(self.train_x)
        self.test_x = sc.transform(self.test_x)
        self.feature_size = np.shape(featrue_data)[1]
        # print(self.test_x)
        # print(self.train_y)
        self.w = np.ones((1,30),dtype=np.float32)*-0.03
        # print(self.w)
        self.train_y = np.reshape(self.train_y,(455,1))
        
    def forward(self):
        self.y = Sigmod(self.w,self.train_x)
        self.loss = np.sum((self.train_y-self.y)**2)
        print(self.loss)
    def backward(self):
        grad = []
        # print(self.y[0])
        for i in range(len(self.w[0])):
            grad.append(np.sum(self.y-self.y**2)*self.w[0][i])
            self.w[0][i]+=grad[i]*0.00002        
a = Logistics()
for i in range(2000):
    a.forward()
    a.backward()
print(a.w)
# plt.scatter(a.train_x[:,0],a.y)
plt.plot(a.train_x[:,0],Sigmod(a.w,a.train_x))
# plt.scatter(a.train_x[:,0],a.train_y)
plt.show()
# w = np.zeros((1,30),dtype=np.float32)
# print(np.shape(Sigmod(w,a.train_x)))
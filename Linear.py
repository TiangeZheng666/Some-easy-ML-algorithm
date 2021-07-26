#Linear reegression

#Three main steps

#TODO:1 prepare dataset

#TODO:2 estblish Model and train

#TODO:3 test

import numpy as np
import matplotlib.pyplot as plt

# function: y = w * x ^ 2 + b 

def forward(x,w,b):
    y_pre = w*(x**2)+b
    return y_pre


def loss(y_pre,y):
    return (y_pre-y)**2

def get_gradient_w(x,w,b,y):
    gw = 0.0
    for i in range(len(x)):
        gw+=2*(x[i]**2)*((x[i]**2)*w+b-y[i])
    gw/=len(x)
    return gw

def get_gradient_b(x,w,b,y):
    gb = 0.0
    for i in range(len(x)):
        gb+=2*((x[i]**2)*w+b-y[i])
    gb/=len(x)
    return gb



# According to these, we can get the function
# By the way, this function can only take one para for x^2
# so if you want use it, you can change the model
def Linear(x,y,iters):
    length_x = len(x)
    length_y = len(y)
    try:
        if length_y!=length_x:
            raise Myerror
    except Myerror:
        Myerror.__printmessage__()
    w = 0.0
    b = 0.0
    for iteration in range(iters):
        y_pre = forward(x,y)
        lost = loss(y_pre=y_pre,y=y)
        w-=0.0005*get_gradient_w(x,w,b,y)
        b-=0.0005*get_gradient_b(x,w,b,y)
    plt.plot(x,y)
    plt.plot(x,(x**2)*w+b)
    plt.show()
    return (w,b)

#well, it is a good way to make a CLASS to do this work
#but for the new hands, I think it's enough
    
        
class Myerror(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def __printmessage__():
        print("length are not equal")


if __name__=='__main__':
    x = np.arange(0,10,1,dtype=float)
    y = x**2+0.1

    w = 13.0
    b = 9.1
    for interation in range(10000):
        y_pre = forward(x=x,w=w,b=0.1)
        lost = loss(y_pre=y_pre,y=y)
        w-=0.0005*get_gradient_w(x,w,b,y)
        b-=0.0005*get_gradient_b(x,w,b,y)
        print("inter: {}  w = {}, b= {}".format(interation,w,b))    
    plt.plot(x,y)
    plt.plot(x,(x**2)*w+b)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
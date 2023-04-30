# 最终在main函数中传入一个维度为6的numpy数组，输出预测值

import os

try:
    import numpy as np
except ImportError as e:
    os.system("sudo pip3 install numpy")
    import numpy as np

def ridge(data):
    x,y = read_data()
    a = 5
    w =  np.matmul(np.linalg.inv(np.matmul(x.T,x)+a*np.eye(x.shape[1])),np.matmul(x.T,y))
    return w@data
    
def lasso(data):
    x,y = read_data()
    dw = np.dot(X.T, (y_hat - y)) / m + alpha * w

def read_data(path='./data/exp02/'):
    x = np.load(path + 'X_train.npy')
    y = np.load(path + 'y_train.npy')
    return x, y

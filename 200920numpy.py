# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 13:55:58 2020

@author: angus
"""
import datetime 
print(datetime.date.today())

from datetime import date
print(date.today())

import numpy as np

a = np.arange(0,60,5.0).reshape(3,4)
b = np.array([1,2,3,4],dtype=int)

for x,y in np.nditer([a,b]):
    print(x,y)

# 一 、修改维度的函数
# broadcast_to()将数组广播到新形状
a = np.arange(4).reshape(1,4)
a #维数相同，有一个轴长为1
np.broadcast_to(a,(4,4))

# expand_dims()指定位置插入新轴扩展数组形状

x = np.array([[1,2],[3,4]])
x.shape
np.expand_dims(x,axis=0).shape
y = np.expand_dims(x,axis=1)
y.shape
# squeeze()从给定数组形状中，删除长度为1的那个维度。
np.squeeze(y).shape
a = np.arange(3).reshape(1,3,1)
np.squeeze(a)
a.size
# 二、数组形状修改的函数
# 1. reshape()参数必须是分解因子
# 2. flat属性
a = np.arange(8).reshape(2,4) 
a
list(a.flat)#数组上一个迭代器
# [0, 1, 2, 3, 4, 5, 6, 7]
# 3. ndarray.flatten() 
a.flatten(order='F')#按列取
help(a.flatten)

# 三、数组连接操作
# 1.stack会增加新的维度
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
np.stack((a,b),axis=0).shape

np.stack((a,b),axis=1).shape

# 水平堆叠
np.hstack((a,b))
np.c_[a,b]
np.r_['1',a,b]
# 垂直堆叠
np.vstack((a,b))
# 等同于 r_是一个实例
np.r_[a,b]
np.c_['0',a,b]

#拼接
np.r_[np.array([1,10]),5,np.arange(10,100,10)]
## array([ 1, 10,  5, 10, 20, 30, 40, 50, 60, 70, 80, 90])


# 查看路径 np.vstack?
np.concatenate((a,b),1)

np.concatenate((a,b),0)


# 四、数组元素操作
## 1. np.resize()
a = np.arange(4)
a.size## 4

np.resize(a,(2,2))

np.resize(a,(2,4))

np.resize(a,(3,3))

a = np.arange(4).reshape(2,2)

np.resize(a,(3,3))
# ndarray内存中存储一样，包装呈现不一样

## 2. np.append()
a
np.append(a,[[4,5]],axis=0) 
np.append(a,[[4,5],[6,7]],axis=1) 

## 3. np.insert()

a = np.arange(6).reshape(3,2)
np.insert(a,4,[6,7])
np.insert(a,1,[6,7],axis=0)
x = np.insert(a,2,[6],axis=1)
np.append(a,[[0,1]],axis=1)
## 4. np。delete
np.delete(x,1,1)

## 5.np.unique()去重
a = np.array([[8,3,3,5,1],[4,3,4,8,5]])
np.unique(a,return_counts=True)
np.unique(a,return_inverse=True)
##The indices to reconstruct the original array from the unique array. Only
##provided if return_inverse is True.
np.unique(a,return_index = True)
##The indices of the first occurrences of the unique values in the original array.
##Only provided if return_index is True.



#与算术有关的函数
a = np.array([1.0, 3, 1.15, 8.7, 20.53])
np.around(a,decimals=1)
np.floor(a)
np.ceil(a)

a = np.array([10, 20, 30])
b = np.array([3, 5, 7])
np.mod(a,b) # 取余
a % b

np.power(a,2) # 求幂 
a ** 2

a = np.arange(9).reshape(3,3)
np.min(a)
np.min(a,1)
np.max(a,1)

np.ptp(a) # 差值
##Range of values (maximum - minimum) along an axis.


np.percentile(a,50)# 百分位数
np.percentile(a,25)

np.median(a)

np.mean(a,1)
np.mean(a,0)

np.std(a,0)##标准差
np.var(a)##方差


#排序相关功能
#获取非零元素
np.nonzero(a)#非零元素的下标
# =============================================================================
# (array([0, 0, 1, 1, 1, 2, 2, 2], dtype=int64),
#  array([1, 2, 0, 1, 2, 0, 1, 2], dtype=int64))
# (0,1),(0,2,)...
# =============================================================================
a = np.ones((3,3))
a[[0, 2, 1, 1, 0],[0, 2, 0, 1, 2]] = 0
np.nonzero(a)
#等同于
a[np.where(a != 0)]

np.where(a == 0)


# 使用循环与向量化两种不同方法来计算100以内质数和

def checkprime(x):
    if x <= 1:
        return False
    prime=True
    for i in range(2,1+x//2):
        if x%i==0:
            prime = False
            break
    return True
def sumprimebyiter(n=100):
    primesum=0
    for i in range(1, n+1):
        if(True == checkprime(i)):
            primesum += i
    return primesum



sumprimebyiter()

import numpy as np
def sumprimebyarr(n=100):
    a = np.arange(1,n+1)
    # return sum(a[np.array(map(CheckPrime,a))])
    #此处用python自带的map函数应用到向量的每个元素
    check_prime_vec = np.vectorize(checkprime)
    #此处用np.vectorize,可以将外置函数应用到向量的每个元素
    return np.sum(a[check_prime_vec(a)])
sumprimebyarr()


#随机生成10个坐标，计算两两之间距离
Z = np.random.randint(10,size=(10,2))
X,Y = np.atleast_2d(Z[:,0]),np.atleast_2d(Z[:,1])
D = np.sqrt((X-X.T)**2 + (Y-Y.T)**2)
print(D)

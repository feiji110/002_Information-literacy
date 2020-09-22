# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 14:34:44 2020

@author: angus
"""
import operator #标准库
import numpy as np#第三方库

# 准备数据
def file_to_matrix(filename):
    '''读取文件
    
    参数：filename文件名
    
    返回值：
         dataX 特征矩阵
         dataY 标签
    '''
    with open(filename,'r') as fr:
        lines = fr.readlines()
        
        n = len(lines)
        dataX = np.zeros((n,3)) #(n,3)作为第一个参数，形状。
        dataY = []
        
        for index,line in enumerate(lines):
            line = line.strip()
            list_of_line = line.split('\t')
            dataX[index,:] = [float(i) for i in list_of_line[:-1]]
            if list_of_line[-1] == "didntLike":
                dataY.append(1)
            if list_of_line[-1] == "smallDoses":
                dataY.append(2)
            if list_of_line[-1] == "largeDoses":
                dataY.append(3)
        return dataX,np.array(dataY)
# 最大最小规范化
# (x - min) / (max - min)
def auto_norm(x):
    '''规范化处理
    
    参数：
        dataX:特征矩阵
    返回值：
        normX 标准化后的特征矩阵
    '''
    max_vector = dataX.max(0)#保留行，算列的最大值
    min_vector = dataX.min(0)
    #不要用循环
    #python与numpy只交流一次，将一行min与max变成一个矩阵
    n = len(dataX)
    max_mat = np.tile(max_vector,(n,1))#行变为N倍，列为1倍
    min_mat = np.tile(min_vector,(n,1))
    normX = (dataX - min_mat) / (max_mat - min_mat)
    return normX
    


def classify(x,trainX,trainY,k):
    '''找x的k个近邻，并预测x的类别
    
    参数：
        x 要预测的样本
        trainX训练集的特征矩阵
        trainY训练集的标签向量
        k 近邻个数
    返回值:
        y_hat:x的预测类别
    '''
    n = len(trainX)
    x_mat = np.tile(x,(n,1))
    d_vector = (((x_mat - trainX) ** 2).sum(1))**0.5
    idxs = d_vector.argsort()#从小到大排序，返回对应下标
    #统计k个样本的类别
    class_count = {}
    for i in range(k):
        i_class = trainY[idxs[i]]
        # {class:count}
        class_count[i_class] = class_count.get(i_class,0) + 1
        #字典中的get函数，有的话返回键值，没有返回0
    class_count = sorted(class_count.items(),key = operator.itemgetter(1),reverse = True)
    #返回一个新的按个数排序,从大到小的字典列表
# =============================================================================
#     print(class_count)
# =============================================================================
    return class_count[0][0]


def test(normX,dataY,k):
    '''测试并评价模型
    参数:
        normX 标准化后的特征矩阵
        dataY 标签
        k k近邻
    返回值：
        error_rate 错误率        
    '''
    n = len(normX)
    test_n = int(n * 0.1)
    testX = normX[:test_n]
    testY = dataY[:test_n]
    trainX = normX[test_n:]
    trainY = dataY[test_n:]
    error_count = 0
    for x,y in zip(testX,testY):
        y_hat = classify(x,trainX,trainY,k)
        if y_hat != y :
            error_count += 1
    error_rate = error_count / test_n
    return error_rate

def cross_validuation(normX,dataY,k):
    '''
    返回值：
        mean_error_rate 平均错误率
    '''
    n = len(normX)
    test_n = int(n * 0.1)
    error_rate_list = []
    for i in range(10):
        test_start = i * test_n
        test_end = (i + 1) * test_n
        testX = normX[test_start:test_end]
        testY = dataY[test_start:test_end]
        if i == 0:
            trainX = normX[test_end:]
            trainY = dataY[test_end:]
        elif i == 9:
            trainX = normX[:test_start,:]
            trainY = dataY[:test_start]
        else:
            trainX1 = normX[:test_start]  
            trainX2 = normX[test_end:]
            trainX = np.r_[trainX1,trainX2]#row增多 c_ : col增多 
            trainY1 = dataY[:test_start]
            trainY2 = dataY[test_end:]
            trainY =np.r_[trainY1,trainY2]
        error_count = 0
        for x,y in zip(testX,testY):
            y_hat = classify(x,trainX,trainY,k)
            if y_hat != y:
                error_count += 1
        error_rate = error_count / test_n
        error_rate_list.append(error_rate)
    
    mean_error_list = sum(error_rate_list)/10
    
# =============================================================================
#     error_rate_list = np.array(error_rate_list)
#     mean_error_list = error_rate_list(0) / len(error_rate_list)
# =============================================================================
    return mean_error_list
            
    
            
            

if __name__ =='__main__':
    dataX,dataY = file_to_matrix("datingTestSet.txt")
    normX = auto_norm(dataX)
    print("错误率：%.2f%%" %(test(normX,dataY,10)*100))
    print("错误率：%.2f%%" %(cross_validuation(normX,dataY,5)*100))
# =============================================================================
#     x = [0.44832535, 0.39805139 ,0.56233353]
#     x2 = [0.158733,0.341955,0.987244]
#     print(classify(x,normX,dataY,30))
#     print(classify(x2,normX,dataY,1))
# =============================================================================
    
            
            
        
        
        
        
        
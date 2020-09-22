# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:56:31 2020

@author: angus
"""
import numpy as np
data = np.loadtxt('testSet.txt')

def euclDistance(v1,v2):
    return np.sqrt( np.sum( np.power(v2-v1,2) ) )
    
def kMeans(dataSet,k):
    #创建K个点作为初始的质心点
    numSamples = dataSet.shape[0]
    clusterAssment = np.empty((numSamples,2))#[j,dist]
    n = dataSet.shape[1]
    centroids = np.empty((k,n))  
    #np.ptp(dataSet,axis = 1)
    #dataSet[:,0].min()+dataSet[:,0].ptp()*np.random.random()
        #一列特征一列特征填充
    for i in range(n):
        centroids[:,i] = dataSet[:,i].min()+dataSet[:,i].ptp()*np.random.rand(k)
    
    #当任意一个点的簇分配结果发生改变时，进入循环体
    clusterChanger = True
    while clusterChanger:
        clusterChanger = False
        #对数据集中每一个数据点
        for i in range(numSamples):
            minDist = 1000000
            minIndex = 0
            #对每一个质心
            for j in range(k):
                #计算质心与数据点的距离，找到距离最近质心
                distance = euclDistance( centroids[j,:],dataSet[i,:] )
                #判断该质心与样本的距离是不是所有质心中最近的
                if minDist > distance:
                    minDist = distance
                    minIndex = j
                #将数据点分配到距离最近的簇
            if clusterAssment[i,0] != minIndex:
                clusterAssment[i,:] = minIndex,minDist
                clusterChanger = True
        #对每一个簇，计算簇中所有点的均值，并将均值作为质心
# =============================================================================
#         for j in range(k):
#             centroids[j,:] = np.mean( dataSet[np.where(  clusterAssment[:,0]==j)],    axis=0 )
#     return centroids,clusterAssment 
# =============================================================================
        for j in range(k):
            tmp = np.zeros((1,n))
            for i in range(numSamples):
                if clusterAssment[i,0] == j:
                    #print(dataSet[i])
                    #tmp = np.concatenate()
                    tmp = np.r_[tmp,np.expand_dims(dataSet[i],0)]
            centroids[j,:] = np.mean(tmp,axis=0) 
    return centroids,clusterAssment 
                    
centroids,clusterAssment = kMeans(data,3)

            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        





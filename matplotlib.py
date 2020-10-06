import matplotlib.pyplot as plt
import numpy as np

#plt.plot([1,2,3,4])

#折线图
x = np.arange(1,10,0.2)

plt.xlim(0,6)
plt.ylim(-1,0)

plt.title("plot sin(x)\cos(x)")
plt.ylabel('sin(x),cos(x)')
plt.xlabel('x')

plt.plot(x,np.cos(x),'r-.',label='cos(x)')
plt.plot(x,np.sin(x),'g',label='sin(x)')

plt.grid(True)
plt.legend()#loc=1右上角

#散点图
x = np.random.normal(0, 1, 100)
y = np.random.normal(0, 1, 100)
#随机生成均值为0标准差为1的符合正态分布的数据
x1 = np.random.normal(0, 2, 100)
y1 = np.random.normal(0, 2, 100)


plt.scatter(x,y,s = 50,c = 'r',marker='+',label='scale=1')
plt.scatter(x1,y1,s = 30,c = 'b',marker='o',label='scale=2')
plt.ylabel('y')
plt.xlabel('x')
plt.grid(True)
plt.legend()



#直方图
plt.bar(['5','8','10'],[12,16,6])
plt.bar(['6','9','11'],[6,15,7],color = 'g')


#
data = {
        'a':np.arange(50),
        'd':np.random.randn(50),
        'b': 100 * np.random.randn(50)
        
        }
plt.scatter('a', 'd', c='r', s='b', data=data)
plt.bar('a', 'd', data=data)
plt.plot('a', 'd', data=data)




x = np.linspace(0, 5, 10)
y = x ** 2
plt.figure(1)
plt.subplot(1,2,1)
plt.plot(x, y, 'r--')

plt.figure(2)
plt.subplot(1,2,2)
plt.plot(y, x, 'g*-')
plt.show()




x = ['group_a', 'group_b', 'group_c']
y = np.arange(0,101,20)

plt.figure(1,figsize=(9,3))

plt.subplot(131)
plt.bar(x,[3, 10, 100])

plt.subplot(132)
plt.plot(x,[3, 10, 100])
plt.title('Categorical Plotting')

plt.subplot(133)
plt.scatter(x,[3, 10, 100])

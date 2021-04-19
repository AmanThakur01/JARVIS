from sklearn import datasets
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
iris = datasets.load_iris()

################classificatoin
# print(iris.DESCR)
# features=iris.data
# labels=iris.target
#
# clf=KNeighborsClassifier()
#
#
# clf.fit(features,labels)
# preds=clf.predict([[1,1,1,1],[2,9,7,12],[12,43,0,34]])         #it takes list of list
# print(preds)


####################logestic regression

x=iris["data"][:,3:]
y=(iris['target']==2).astype(np.int)
lgst=LogisticRegression()
lgst.fit(x,y)
res=lgst.predict(([[2.7]]))
print(res)
newX=np.linspace(0,3,1000).reshape(-1,1)
proby=lgst.predict_proba(newX)

plt.plot(newX,proby[:,1:])
plt.show()


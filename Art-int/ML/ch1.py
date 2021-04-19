import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn import datasets, linear_model

diabetes = datasets.load_diabetes()
# dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])


# print(diabetes.DESCR)
diabetesX = diabetes.data       #[:, np.newaxis, 2]
diabetesX_train=diabetesX[:-30]
diabetesX_test=diabetesX[-30:]

diabetesY_train=diabetes.target[:-30]
diabetesY_test=diabetes.target[-30:]

model=linear_model.LinearRegression()
model.fit(diabetesX_train,diabetesY_train)
diabetesY_pred=model.predict(diabetesX_test)
print("mean square error = ",mean_squared_error(diabetesY_test,diabetesY_pred))

print("weight : ",model.coef_)
print("intercept : ",model.intercept_)

# plt.scatter(diabetesX_test,diabetesY_test,label="test")
# plt.scatter(diabetesX_train,diabetesY_train,label="tran")
# plt.plot(diabetesX_test,diabetesY_pred,label="pred")
# plt.legend()
# plt.show()
#################OUTPUT
# mean square error =  3035.0601152912686
# weight :  [941.43097333]
# intercept :  153.39713623331698
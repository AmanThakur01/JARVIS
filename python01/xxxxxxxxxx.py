# a#for i in range(1,20,5):
#    # print(i)
#
# #txt = "helo"[::-1]
# #print(txt)
# import time
# # try:
# #     class person:
# #         def __init__(self):
# #             self.name = "aman"
# #             self.age = 18
# #     a1 = person()
# #     a2 = person()
# #     print(a1.name)
# # except ZeroDivisionError as e:
# #     print("Opps!@....sorry....!")
# # except ValueError as e:
# #     print("value error")
# # finally:
# #     print("come again")
# # for i in range(5):
# #     print(i)
# t1 = time.localtime(time.time())
# print(t1)
# categories = ["Action_and_adventure", "History", "Thriller", "Fantasy", "Fiction", "Mystery", "Horror", "Other"]
#
# for i in categories:
#      print(i)

# a=1,b=2
# res=a+b-(a=b-a)
# importing Numpy package
# importing numpy library
import numpy as np
  
# create numpy 2d-array
m = np.array([[2, 2,1],
              [1, 3,1],
              [1,2,2]])
  
print("Printing the Original square array:\n",
      m)
  
# finding eigenvalues and eigenvectors
w, v = np.linalg.eig(m)
  
# printing eigen values
print("Printing the Eigen values of the given square array:\n",
      w)
  
# printing eigen vectors
print("Printing Right eigenvectors of the given square array:\n",v)

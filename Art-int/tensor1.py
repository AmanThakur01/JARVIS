import numpy as np
import torch
t0=torch.tensor([[2,2,2],[2,2,2]])
t1 = torch.tensor([[1,1,1],[1,1,1]])
t2 = torch.full((3,2),88)
print(t1)
print(t2)
t3 = torch.cat((t1,t0),axis=0)   #axis =1
t4= torch.cos(t1)
print(t3)
print(t4)
x=torch.tensor(4.,requires_grad=True)
w=torch.tensor(2.,requires_grad=True)

t8=w*x
print("dy/dx=",x.grad)#this is differantition
print("dy/dx=",w.grad)


# convert into tensor

a_np = np.array([[1,2,3],[4,5,6]])
print(type(a_np))
a_tensor=torch.from_numpy(a_np)
print(a_tensor)


#convert tensot to numpy
b_np=a_tensor.numpy()
print(b_np)
w1=torch.tensor([[1,23],[12,2]])
w2=torch.tensor([[1,23],[12,2]])

res = torch.matmul(w1,w2.t())#.t() transpose
print(res)


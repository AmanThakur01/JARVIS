import pickle


# car = ["BBT", "BMW", "Bentley", "Audi"]
# file = "mycar.pkl"
# with open("mycar.pkl", "wb") as obj:
#     pickle.dump(car, obj)

file = "mycar.pkl"
with open("mycar.pkl", "rb") as obj:
    mycar = pickle.load(obj)
    print(mycar)



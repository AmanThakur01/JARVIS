from joblib import dump, load
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split

housing = pd.read_excel("data.ods")
trainSet, testSet = train_test_split(housing, test_size=0.2, random_state=42, stratify=housing[('CHAS')])

housing_train = trainSet.drop('MEDV', axis=1)
housing_labels = trainSet["MEDV"].copy()

imputer = SimpleImputer(strategy='mean')  # missing_values=np.nan,
imputer.fit(housing_train)

x = imputer.transform(housing_train)
housingTr = pd.DataFrame(x, columns=housing_train.columns)
########            set data in pipeline
my_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("std_scale", StandardScaler()),
])
housing_num_tr = my_pipeline.fit_transform(housingTr)

model = RandomForestRegressor()
model.fit(housing_num_tr, housing_labels)
################                                saving model
dump(model, "Dragon.joblib")

##            final testing with test set
xTest = testSet.drop('MEDV', axis=1)
yTest = testSet['MEDV'].copy()
X_prepared = my_pipeline.transform(xTest)
finalPredction = model.predict(X_prepared)
final_mse = mean_squared_error(yTest, finalPredction)
final_rmse = np.sqrt(final_mse)
print("This Model may have Error of", final_rmse, "Thousand only\n")

# print(finalPredction)
# print("\n   ", list(yTest))


###########################                 user input for model

model = load("Dragon.joblib")


print("1. CRIM      per capita crime rate by town\n"
      "2. ZN        proportion of residential land zoned for lots over 25,000 sq.ft.\n"
      "3. INDUS     proportion of non-retail business acres per town\n"
      "4. CHAS      Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)\n"
      "5. NOX       nitric oxides concentration (parts per 10 million)\n"
      "6. RM        average number of rooms per dwelling\n"
      "7. AGE       proportion of owner-occupied units built prior to 1940\n"
      "8. DIS       weighted distances to five Boston employment centres\n"
      "9. RAD       index of accessibility to radial highways\n"
      "10. TAX      full-value property-tax rate per $10,000\n"
      "11. PTRATIO  pupil-teacher ratio by town\n"
      "12. B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town\n"
      "13. LSTAT    % lower status of the population\n"
      "14. MEDV     Median value of owner-occupied homes in $1000's\n")

# -0.53010046, 0.02099025, -0.66033355, -0.28997256, -1.18431286,
#                       -1.10275785, -1.03091974, 1.20484991, -0.52498507, -0.2399869,
#                       0.29292564, 0.39425368, 0.23912392
user_list=[]
labels_list=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX',
       'PTRATIO', 'B', 'LSTAT']
for i in range(13):
      usr_value = float(input(f"Enter values of {labels_list[i]} : "))
      user_list.append(usr_value)


features = np.array([user_list])
pred_list=model.predict(features)
for i in pred_list:
      print("This house cost you ",round(i,2),"K US Dollar only")

from sklearn import datasets
import pandas as pd

iris_raw = datasets.load_iris()
iris = pd.DataFrame(
    iris_raw["data"],
    columns=iris_raw["feature_names"]
)

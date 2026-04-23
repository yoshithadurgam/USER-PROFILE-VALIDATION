import random, math
import numpy as np
import pandas as pd
def gen(n=15):
    data = [{"zone": i, "traf": random.randint(0, 100),
             "air_qua": random.randint(0, 300),
             "ener": random.randint(0, 500)} for i in range(1, n + 1)]
    data += [{"zone": n + 1, "traf": 95, "air_qua": 280, "ener": 450},
             {"zone": n + 2, "traf": 0, "air_qua": 50, "ener": 120},
             {"zone": n + 3, "traf": 100, "air_qua": 300, "ener": 500}]
    return data
def classify(r):
    return ("High Risk" if r["air_qua"] > 200 or r["traf"] > 80 else
            "Energy Critical" if r["ener"] > 400 else
            "Safe Zone" if r["traf"] < 30 and r["air_qua"] < 100 else
            "Moderate")
def risk(r):
    return round(r["traf"] * 0.25 + r["air_qua"] * 0.55 + r["ener"] * 0.2, 2)
def sort_data(arr, key):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i][key] < arr[j][key]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr
def detect(df):
    th = df["risk_sc"].mean()
    multi = df[(df["risk_sc"] > th) & (df["air_qua"] > 200)]
    stable = np.var(df["traf"]) < 800
    clusters = [];
    temp = []
    for _, r in df.iterrows():
        if r["risk_sc"] > th:
            temp.append(r["zone"])
        else:
            if len(temp) >= 2: clusters.append(temp)
            temp = []
    return multi, stable, clusters
data = gen()
for r in data:
    r["cat"] = classify(r)
    r["risk_sc"] = risk(r)
roll = 24
data = random.sample(data, len(data)) if roll % 3 == 0 else sort_data(data, "traf")
df = pd.DataFrame(data)
mat = df[["traf", "air_qua", "ener"]].to_numpy()
mean = np.mean(mat, axis=0)
df["sqrt_risk"] = df["risk_sc"].apply(lambda x: math.sqrt(x))
top3 = sort_data(data.copy(), "risk_sc")[:3]
multi, stable, clusters = detect(df)
risk_tuple = (df["risk_sc"].max(), df["risk_sc"].mean(), df["risk_sc"].min())
avg = risk_tuple[1]
decision = ("City Stable" if avg < 100 else
            "Moderate Risk" if avg < 150 else
            "High Alert" if avg < 200 else
            "Critical Emergency")
print("\nDataFrame:\n", df)
print("\nCategories:", df["cat"].value_counts().to_dict())
print("\nTop 3 Zones:", top3)
print("\nMean Values:", mean)
print("\nRisk Tuple:", risk_tuple)
print("\nMulti Risk:\n", multi[["zone", "risk_sc"]])
print("Stable:", stable, "\nClusters:", clusters)
print("\nFinal Decision:", decision)
print("\nSmart City Definition:")
print("A smart city balances traffic, air quality, and energy using data-driven systems.")
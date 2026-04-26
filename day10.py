import random
import copy
import math
import numpy as np
import pandas as pd
def generate_zones(n=15):
    data = []
    for i in range(n):
        zone = {
            "zone": i + 1,
            "metrics": {
                "traffic": random.randint(50, 300),
                "pollution": random.randint(20, 200),
                "energy": random.randint(100, 500)
            },
            "history": [random.randint(10, 100) for _ in range(5)]
        }
        data.append(zone)
    return data
def personalize_data(data, is_odd):
    if is_odd:
        return data[3:] + data[:3]
    else:
        return list(reversed(data))
def replicate(data):
    assign = data
    shallow = list(data)
    deep = copy.deepcopy(data)
    return assign, shallow, deep
def mutate(data):
    for d in data:
        d["metrics"]["traffic"] += 10
        d["metrics"]["pollution"] += 5
        d["history"].append(random.randint(1, 50))
def compute_risk(data):
    risks = []
    for d in data:
        total = d["metrics"]["traffic"] + d["metrics"]["pollution"] + d["metrics"]["energy"]
        risk = math.log(total)
        risks.append(risk)
    return np.array(risks)
def to_dataframe(data, risks):
    rows = []
    for i, d in enumerate(data):
        row = {
            "zone": d["zone"],
            "traffic": d["metrics"]["traffic"],
            "pollution": d["metrics"]["pollution"],
            "energy": d["metrics"]["energy"],
            "risk": risks[i]
        }
        rows.append(row)
    return pd.DataFrame(rows)
def analyze(df, risks):
    mean_val = np.mean(risks)
    var_val = np.var(risks)
    std_val = np.std(risks)
    x = df["traffic"].values
    y = df["pollution"].values
    corr = np.sum((x - x.mean()) * (y - y.mean())) / (
        np.sqrt(np.sum((x - x.mean())**2)) * np.sqrt(np.sum((y - y.mean())**2))
    )
    anomalies = df[df["risk"] > mean_val + std_val]["zone"].tolist()
    return mean_val, var_val, std_val, corr, anomalies
def detect_patterns(original, shallow, risks):
    # hidden corruption
    corruption = 0
    for i in range(len(original)):
        if len(original[i]["history"]) != 5:
            corruption += 1
    threshold = np.mean(risks)
    risky = [i for i, r in enumerate(risks) if r > threshold]
    clusters = []
    current = []
    for idx in risky:
        if not current or idx == current[-1] + 1:
            current.append(idx)
        else:
            clusters.append(current)
            current = [idx]
    if current:
        clusters.append(current)
    stability_index = 1 / np.var(risks)
    return corruption, clusters, stability_index
def decision(corruption, stability):
    if corruption > 5:
        return "Critical Failure"
    elif corruption > 2:
        return "High Corruption Risk"
    elif stability < 0.5:
        return "Moderate Risk"
    else:
        return "System Stable"
def main():
    data = generate_zones()
    data = personalize_data(data, is_odd=True)
    before = copy.deepcopy(data)
    assign, shallow, deep = replicate(data)
    print("BEFORE:\n", before)
    mutate(shallow)
    print("\nAFTER:")
    print("Original:", data)
    print("Shallow:", shallow)
    print("Deep:", deep)
    risks = compute_risk(data)
    df = to_dataframe(data, risks)
    mean_val, var_val, std_val, corr, anomalies = analyze(df, risks)
    corruption, clusters, stability = detect_patterns(data, shallow, risks)
    final = decision(corruption, stability)
    print("\nDataFrame:\n", df)
    print("\nAnomaly Zones:", anomalies)
    print("\nTuple Output:", (max(risks), min(risks), stability))
    print("\nFinal Decision:", final)
main()
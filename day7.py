readings = [15, 60, 180, 45, -5, 120, 35, 155, 80]
usage_data = {
    "efficient": [],
    "moderate": [],
    "high": [],
    "invalid": []
}
for value in readings:
    if value < 0:
        usage_data["invalid"].append(value)
    elif value <= 50:
        usage_data["efficient"].append(value)
    elif value <= 150:
        usage_data["moderate"].append(value)
    else:
        usage_data["high"].append(value)
filtered_values = [x for x in readings if x >= 0]
total = sum(filtered_values)
count = len(readings)
info = (total, count)
if total > 600:
    status = "Energy Waste Detected"
elif len(usage_data["high"]) > 3:
    status = "Overconsumption"
elif abs(len(usage_data["efficient"]) - len(usage_data["moderate"])) <= 1:
    status = "Balanced Usage"
else:
    status = "Efficient Campus"
print("Categories:", usage_data)
print("Total Energy:", total)
print("Total Buildings:", count)
print("Summary:", info)
print("Final Status:", status)
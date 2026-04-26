import copy
def create_users():
    return [
        {"id": 1, "data": {"files": ["a.txt", "b.txt"], "usage": 500}},
        {"id": 2, "data": {"files": ["c.txt"], "usage": 300}}
    ]
def replicate_versions(base):
    ref_copy = base
    shallow_copy = list(base)
    deep_copy = copy.deepcopy(base)
    return ref_copy, shallow_copy, deep_copy
def apply_changes(dataset, odd_flag):
    for entry in dataset:
        file_list = entry["data"]["files"]
        if odd_flag:
            if len(file_list) > 0:
                file_list.remove(file_list[-1])
        else:
            file_list.append("extra.txt")
        entry["data"]["usage"] += 50
def evaluate_integrity(original, shallow, deep, snapshot):
    leak = 0
    safe = 0
    overlap = 0
    for i in range(len(original)):
        if original[i]["data"]["files"] != snapshot[i]["data"]["files"]:
            leak += 1
    for i in range(len(deep)):
        if deep[i]["data"]["files"] == snapshot[i]["data"]["files"]:
            safe += 1
    for i in range(len(original)):
        set1 = set(original[i]["data"]["files"])
        set2 = set(shallow[i]["data"]["files"])
        overlap += len(set1 & set2)
    return (leak, safe, overlap)
def run_program():
    base_data = create_users()
    before_state = copy.deepcopy(base_data)
    ref, shallow, deep = replicate_versions(base_data)
    print("Before changes:\n", base_data)
    is_odd = True
    apply_changes(shallow, is_odd)
    print("\nAfter changes:")
    print("Original:", base_data)
    print("Shallow:", shallow)
    print("Deep:", deep)
    report = evaluate_integrity(base_data, shallow, deep, before_state)
    print("\nIntegrity Result:", report)
    print("\nMutation Insight:")
    print("- Inner structure (file list) was affected due to shared reference.")
    print("- Outer structure was copied, but nested objects were not fully duplicated.")
run_program()
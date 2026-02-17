weights = [4, 18, 70, -2, 30, 55, 0]
vl = []
nl = []
hl = []
ol = []
invalid = []
for w in weights:
    if w < 0:
        invalid.append(w)
    elif w <= 5:
        vl.append(w)
    elif w <= 25:
        nl.append(w)
    elif w <= 60:
        hl.append(w)
    else:
        ol.append(w)
full_name = "Yoshitha Durgam"
L = 0
for ch in full_name:
    if ch != " ":
        L += 1
PLI = L % 3
aff_count = 0
if PLI == 0:
    for item in ol:
        invalid.append(item)
        aff_count += 1
    ol = []
elif PLI == 1:
    aff_count = len(vl)
    vl = []
elif PLI == 2:
    aff_count = len(vl) + len(ol) + len(invalid)
    vl = []
    ol = []
    invalid = []
valid_no = 0
for w in weights:
    if w >= 0:
        valid_no += 1
print("L (NAME LENGTH):", L)
print("PLI VALUE:", PLI)
print("AFFECTED COUNT due to PLI:", aff_count)
print("Total valid weights:", valid_no)
print("\nFINAL LOAD:")
print("Very Light:", vl)
print("Normal Load:", nl)
print("Heavy Load:", hl)
print("Overload:", ol)
print("Invalid Entries:", invalid)

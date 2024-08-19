################
# GENERATED CODE
################

from tabulate import tabulate
import pandas as pd
from pathlib import Path

########## HELPER FUNCTIONS ##########

def generate_ranges(codes):
    codes.sort(key=lambda x: int(x[1:]))
    ranges, start = [], codes[0]
    for i in range(1, len(codes)):
        if int(codes[i][1:]) != int(codes[i-1][1:]) + 1:
            ranges.append(start if start == codes[i-1] else f"{start}-{codes[i-1]}")
            start = codes[i]
    ranges.append(start if start == codes[-1] else f"{start}-{codes[-1]}")
    return ranges

def get_points(data):
    table_data = [["Questions", "Points", "Number", "Total"]]
    order = ["R", "I", "S", "C", "V"]
    order_index = {item: index for index, item in enumerate(order)}
    qtype_list = list(set([k[0] for k in data.keys()]))
    qtype_list_sorted = sorted(qtype_list, key=lambda x: order_index[x])
    points_set = set(data.values())
    for qtype in qtype_list_sorted:
        for points in points_set:
            codes = [key for key in data if data[key] == points and qtype in key]
            number = len(codes)
            if number != 0:
                ranges = ", ".join(generate_ranges(codes))
                points_per_question = f"{points} pt(s)"
                total = f"{points * number} pt(s)"
                subtotal = f"{points} x {number} = {total}"
                table_data.append([ranges, points_per_question, number, subtotal])
    table_data.append(["Grand Total", "", "", f"{sum(data.values())} points"])
    return table_data

########## RUBRIC ##########

questions = {

# R-type questions
	'R1':	6,
	'R2':	6,
	'R3':	6,
	'R4':	6,
	'R5':	2,
	'R6':	2,
	'R7':	2,
	'R8':	2,
	'R9':	2,
	'R10':	2,
	'R11':	2,

# S-type questions
	'S1':	6,
	'S2':	6,

}

print()
table = get_points(data=questions)
df = pd.DataFrame(table[1:], columns=table[0])
df.to_excel(Path(__file__).parent / "worksheet1.xlsx", index=False, engine="openpyxl")
print(tabulate(table, headers="firstrow", tablefmt="simple_grid"))
print()

#######################
# END OF GENERATED CODE
#######################
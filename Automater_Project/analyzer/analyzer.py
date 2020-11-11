import numpy as np
import os
import csv
import pathlib
from configparser import ConfigParser
import statistics

file = 'inputs.cfg'
results = 'results\\'

# create config
config = ConfigParser()
config.read(file)

# extract data from cfg
for sec in config.sections():
    if sec == "Directory":
        use_case_dir = config[sec]["usecasedirectory"]
    elif sec == "Costs":
        energy_cost = float(config[sec]["costofenergy"])
        emission_cost = float(config[sec]["costofco2"])
        retrofit_list = list(config[sec]["costofretrofits"].split(","))
        retrofit_cost = {}
        for i in retrofit_list:
            templist = list(i.split(":"))
            retrofit_cost[templist[0]] = templist[1]

    else:
        r_map = list(config[sec]["retrofits"][1:-1].split("),("))
        for i in range(len(r_map)):
            r_map[i] = list(r_map[i].split(","))

# print(type(use_case_dir))
# print(use_case_dir)
# print(type(energy_cost))
# print(energy_cost)
# print(type(emission_cost))
# print(emission_cost)
# print(type(retrofit_cost))
# print(retrofit_cost)
# print(type(r_map))
# print(r_map)

# init length of data (equal to number of output params by grasshopper)
data = []
for i in range(len(r_map)):
    data.append({})
# print(data)

# add all csv data to 'data' var
for _, dirs, _ in os.walk(use_case_dir):
    for dir in dirs:
        num = int(dir[-1])
        case_dir = os.path.join(use_case_dir, dir)
        for _, _, files in os.walk(case_dir):
            for file in files:
                if file.endswith("out.csv"):
                    this_csv = os.path.join(case_dir, file)
                    mylist = []
                    with open(this_csv, 'r') as csv_file:
                        reader = csv.reader(csv_file)
                        for lines in reader:
                            mylist.append(lines)
        headers = mylist[0][1:]
        mylist = np.transpose(np.array(mylist[1:]))
        mylist = np.delete(mylist, 0, 0)
        csvdict = {}
        for i in range(len(mylist)):
            csvdict[headers[i]] = [float(ele) for ele in mylist[i].tolist()]
        # print(csvdict)
        data[num-1] = csvdict
# print(data)

# total (and by type) energy per use case
energy = results+"energy.csv"
if os.path.exists(energy):  # delete csv if it exists
    os.remove(energy)
energymatrix = []
with open(energy, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # write header
    headercsv = [""]
    for i in data[0]:
        headercsv.append(i+" IN [kWh] IGNORE OTHER UNITS")
    headercsv.append("TOTAL [kWh]")
    headercsv.append("DELTA [kWh] (compared to use case 1)")
    csvwriter.writerow(headercsv)
    energymatrix.append(headercsv)
    # write body
    base_total = -1
    for i in range(len(data)):
        total = 0
        output = ["use case "+str(i+1)]
        for j in data[i]:
            subtotal = sum(data[i][j])*.27778/1000000
            output.append(subtotal)
            total += subtotal
        if i == 0:
            base_total = total
        output.append(str(total))
        output.append(str(total-base_total))
        csvwriter.writerow(output)
        energymatrix.append(output)

energymatrix2 = (np.transpose(np.array(energymatrix[1:]))[1:-1]).tolist()
# print(energymatrix2)
# print(len(energymatrix2))

# sensitivity
sensitivity = results+"sensitivity.csv"
if os.path.exists(sensitivity):  # delete csv if it exists
    os.remove(sensitivity)
with open(sensitivity, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    for i in range(len(retrofit_cost)):
        csvwriter.writerow([list(retrofit_cost.items())[i][0]])
        for j in range(len(energymatrix2)):
            header = [energymatrix[0][j+1]]
            header.append("min")
            header.append("avg")
            header.append("max")
            csvwriter.writerow(header)
            nolist = []
            yeslist = []
            for k in range(len(energymatrix2[j])):
                if r_map[k][i] == "false":
                    nolist.append(float(energymatrix2[j][k]))
                else:
                    yeslist.append(float(energymatrix2[j][k]))
            if len(nolist) > 0:
                no_avg = statistics.mean(nolist)
                no_min = min(nolist)
                no_max = max(nolist)
            else:
                no_avg = -1
                no_min = -1
                no_max = -1
            if len(yeslist) > 0:
                yes_avg = statistics.mean(yeslist)
                yes_min = min(yeslist)
                yes_max = max(yeslist)
            else:
                yes_avg = -1
                yes_min = -1
                yes_max = -1
            body = ["no retrofit"]
            body.append(no_min)
            body.append(no_avg)
            body.append(no_max)
            csvwriter.writerow(body)
            body = ["retrofit"]
            body.append(yes_min)
            body.append(yes_avg)
            body.append(yes_max)
            csvwriter.writerow(body)

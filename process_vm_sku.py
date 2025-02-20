# az vm list-sizes --location "eastus" -o table
import re
from pprint import pprint

sku_dict={}

with open("skulist-01.30.2024.txt", "r") as file:
    for line in file:
        if "Standard" in line:
            result= line.split("_")
            if len(result) > 2:
                if "-" in line:
                    # print("complex")
                    print(line.split("_")[1])
                    # print(line.split()[2])
                    sku_dict[line.split("_")[1]]=line.split()[2]
                else:
                    # print("simple")
                    print(line.split("_")[1])
                    sku_dict[line.split("_")[1]] = line.split()[2]
            else:
                if "-" in line:
                    # print("complex")
                    print(line.split("_")[1].split()[0])
                    # print(line.split()[2])
                    sku_dict[line.split("_")[1].split()[0]] = line.split()[2]
                else:
                    # print("simple")
                    print(line.split("_")[1].split()[0])
                    sku_dict[line.split("_")[1].split()[0]] = line.split()[2]
                # print(line.split("_")[1].split()[0])
                # print(line.split()[2])
            # print(len(result))
            # print(line)
        else:
            print(line.split()[2])
            sku_dict[line.split()[2]] = line.split()[2]

print(len(sku_dict))
pprint(sku_dict)

####### This is Good #########
# for k,v in sku_dict.items():
#     if "-" in k:
#         if re.search('\d\d', k.split('-')[1]):
#             print(k, v)
#     else:
#         if re.search('\d\d', k):
#             print(k,v)
remove_key =[]
for k,v in sku_dict.items():
    if "-" in k:
        if re.search('\d\d', k.split('-')[1]):
            print(k, v)
            remove_key.append(k)
    else:
        if re.search('\d\d', k):
            print(k,v)
            remove_key.append(k)

print(len(remove_key))
print(len(sku_dict))
sku_dict.pop('Name')
for key in remove_key:
    sku_dict.pop(key)

print(len(sku_dict))

pprint(sku_dict)


with open("sku-list-policy-east-us-2.txt", "w") as finalfile:
    for key,value in sku_dict.items():
        finalfile.write(f'"{value}",')
        finalfile.write("\n")
        print(value)

vm_set = set()
#check
with open("AzureVirtualMachines-01-30-24.csv", "r") as file:
    for line in file:
        # print(line.split(","))
        length = len(line.split(","))
        # print(length)
        if length > 1:
            vm_size = line.split(",")[length-1]
            if vm_size in sku_dict.values():
                print("fine")
            else:
                print(vm_size)
                vm_set.add(vm_size)

pprint(vm_set)


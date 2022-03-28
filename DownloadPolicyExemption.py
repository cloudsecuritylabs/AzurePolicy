import os
# Author: Ankan Basu
# uncomment to line below to run code as a user
# user should have at least read access to all subscriptions
# os.system("az login")

subsctiption_list = "subcriptionlist.txt"
# save a list of subscriptions to a file
os.system(" az account list --output table | grep ^sub-[pn] | sort  > " + subsctiption_list)
# open the file to loop over subscriptions
file = open(subsctiption_list, "r")

# 
for sub in file.readlines():
    splitted=sub.split()
    command = 'az account set --subscription ' +   splitted[0]
    # set subcription scope
    os.system(command)
    exemption_list = "excemption_list.txt"
    fileoutput = open(exemption_list, "a")
    fileoutput.write(sub)
    fileoutput.write("\n")
    fileoutput.close()
    os.system("az policy exemption list --query '[].{displayname:displayName, exemptioncategory:exemptionCategory, expireson: expiresOn}' --disable-scope-strict-match -i --output table  >> " + exemption_list)
    os.system("echo ==================== >> " +exemption_list)
file.close()


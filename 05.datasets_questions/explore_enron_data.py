#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
# print type(enron_data)

#quiz ans of size of enron data

# print size(enron_data)

#quiz ans of how many feature against each people

"""for key in enron_data:
    print "People ", key , "\n\nTotal Feature ", len(enron_data[key])"""

#quiz ans of total number of person of interest in enron dataset

"""totalPOI = 0

for people in enron_data:
    if enron_data[people]["poi"]:
        totalPOI+=1

print totalPOI"""

"""for people in enron_data:
    # print people
    if people.lower() == "Prentice James".lower():
        print enron_data[people]["total_stock_value"]"""
# print enron_data[]

"""for people in enron_data:
    if people.lower() == "Skilling Jeffrey K".lower():
        print enron_data[people]["total_stock_value"]
        # print enron_data[people]
"""
"""noSalary = 0
noEmailAdd = 0
for people in enron_data:
    if enron_data[people]["salary"] != "NaN":
        noSalary+=1
    if enron_data[people]["email_address"] != "NaN":
        noEmailAdd+=1
    print "email_address -> ", enron_data[people]["email_address"], " type of email address ",type(enron_data[people]["email_address"])
print "No Email Address -> ",noEmailAdd," No Salary -> ",noSalary"""
    
"""totalPaymentNaN = 0
totalPeople = len(enron_data)
for people in enron_data:
    if enron_data[people]["total_payments"]=="NaN":
        totalPaymentNaN+=1
print "Total People : ", totalPeople , " Total People With NaN as Payment : ",totalPaymentNaN
print float(totalPaymentNaN)/totalPeople*100"""


totalPOIWithPaymentNaN = 0
totalPeopleWithPOI = 0
for people in enron_data:
    if enron_data[people]["poi"] == True :
        totalPeopleWithPOI+=1
        if enron_data[people]["total_payments"]=="NaN":
            totalPOIWithPaymentNaN+=1
print totalPeopleWithPOI, " ", totalPOIWithPaymentNaN
print float(totalPOIWithPaymentNaN)/totalPeopleWithPOI*100


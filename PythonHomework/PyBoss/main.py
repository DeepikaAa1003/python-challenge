#Create a relative path define csvpath as variable
# Open the csv file in read mode
# ignore first line as header and go to next pointer
# For loop to read each line of CSV file 
    # Create function to split name
    # create function to fomrat SSNTIN and date
    # create function to abbreviate state

import os
import csv
from datetime import datetime as dt


EmpId = []
First_Name =[]
Last_Name = []
DOB = []
SSN = []
State = []


# locate the CSV file
csvpath = os.path.join("Resources", "employee_data.csv")

# Dictionary of abbreviated states
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
    }

# Function to split names
def splitName(name):
       names = name.partition(" ")
       First_Name.append(names[0])
       Last_Name.append(names[2])

# Function to format date      
def DateFormat(dateofbirth):
        datetimeobject = dt.strptime(dateofbirth,'%Y-%m-%d')
        NEW_DOB = datetimeobject.strftime('%m/%d/%Y')
        DOB.append(str(NEW_DOB))

# Function to format ssntin
def MaskSSNTIN(ssntin):
        new_tin = "****-**-" + ssntin[7:11]
        SSN.append(new_tin)

# Function to abbreviate state
def StateAbv(state):
        state_abv = us_state_abbrev[state]
        State.append(state_abv)

# Open CSV file
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        #Ignore header 
        csv_header = next(csvreader)

        for data in csvreader:
            EmpId.append(data[0])
            splitName(data[1])
            DateFormat(data[2])
            MaskSSNTIN(data[3])
            StateAbv(data[4])


EmployeeFormatted_data = zip(EmpId,First_Name,Last_Name,DOB,SSN,State)


# Specify the file to write to
output_path = os.path.join("Analysis", "New_employee_data.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w',  newline="") as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # Write the second row
    csvwriter.writerows(EmployeeFormatted_data)

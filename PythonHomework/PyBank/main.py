#Create a relative path define csvpath as variable
# Open the csv file in read mode
# ignore first line as header and go to next pointer
# For loop to read each line of CSV file 
    #  Create a counter and increment to count total number of months
    #  add row[1] to sum the total amount of profit/losses
    #  calculate ChangeinAmount =  row[1] of current row - row[1] of previous row
    #  Calculate total increase or decrease in amount and form a list - put calculated changeinamount in a list
    #  new changeinAmountList will be as follows = [0,116771,-662642 and so on]
    
    
# end for loop
# calculate average change as  Total sum of changeinamount list divide by length of the list
# use max function to find greatest increase in the changeinamount list
# Use min function to find greatest decrease in the changeinamount list

import os
import csv


AmountChangeList = []
MonthOfAmountChangeList = []

previous_row_amount = 0
Total_Months = 0
Total_Amount = 0

# locate the CSV file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open CSV file
with open(csvpath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        #Ignore header 
        csv_header = next(csvreader)

        for data in csvreader:
            # Increment counter for each row to calculate total number of months
            Total_Months = Total_Months + 1

            #Skip logic for 1st row
            if Total_Months > 1:

                #Calculate difference in amount from previous row to current row and store in AmountChangeList. Also store Month for that amount change in another list
                AmountChangeList.append(int (data[1]) - int(previous_row_amount))
                MonthOfAmountChangeList.append(data[0])

            #Calculate total amount by adding column 2 of each row
            Total_Amount = Total_Amount + int (data[1])

            #Store amount of current row to be used while calculating amount change for next row
            previous_row_amount = data[1]

# write the ouput to terminal

print("Financial Analysis")
print ("-----------------------------")
print("Total Months: " + str(Total_Months))
print("Total: " + "$" + str(Total_Amount))
#print("Length of AmountChangeList" + str(len(AmountChangeList)))
#print("Sum of amount changein list " + str(sum(AmountChangeList)))
print("Average Change : "+ "$" + str(round(float(sum(AmountChangeList)/len(AmountChangeList)),2)))
print("Greatest Increase in Profits: " + MonthOfAmountChangeList[AmountChangeList.index(max(AmountChangeList))]  + " ($" + str(max(AmountChangeList)) + ")")
print("Greatest Decrease in Profits: " + MonthOfAmountChangeList[AmountChangeList.index(min(AmountChangeList))] + " ($" + str(min(AmountChangeList)) + ")" )
# print(AmountChangeList)

# Write the output to text file

textpath = os.path.join('Analysis', 'Analysis.txt')
Textfile1 = open(textpath, "w")
Textfile1.writelines("Financial Analysis\n")
Textfile1.writelines("-----------------------------\n")
Textfile1.writelines("Total Months: " + str(Total_Months) + "\n")
Textfile1.writelines("Total: " + "$" + str(Total_Amount) + "\n")
#print("Length of AmountChangeList" + str(len(AmountChangeList)))
#print("Sum of amount changein list " + str(sum(AmountChangeList)))
Textfile1.writelines("Average Change : "+ "$" + str(round(float(sum(AmountChangeList)/len(AmountChangeList)),2)) + "\n")
Textfile1.writelines("Greatest Increase in Profits: " + MonthOfAmountChangeList[AmountChangeList.index(max(AmountChangeList))]  + " ($" + str(max(AmountChangeList)) + ")" + "\n")
Textfile1.writelines("Greatest Decrease in Profits: " + MonthOfAmountChangeList[AmountChangeList.index(min(AmountChangeList))] + " ($" + str(min(AmountChangeList)) + ")"  + "\n")
Textfile1.close()





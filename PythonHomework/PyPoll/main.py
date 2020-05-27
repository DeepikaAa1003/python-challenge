# Open the CSV file 
# Ignore the header
# Read the csv file to create 3 lists for VoterId, County and candidate
# sum the VoterID dictionary to calculate the total number of votes cast
# Complete list of candidates who received votes  - Unique count of Candidate dictionary
# The percentage of votes each candidate won  -  vote count for each candidate / total votes
# The total number of votes each candidate won - vote count of each candidate
# The winner of the election based on popular vote -  max vote count among candidates



import os
import csv

#Locate CSV file
csvpath = os.path.join("Resources", "election_data.csv")
Voters = [] #list to store all voters
Candidate = [] # list to store all candidates
VotingCount_perCandidate = [] # list to store number of votes per candidate


#Open CSV file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
        
    csv_header = next(csvreader)

    for data in csvreader:
        Voters.append(data[0]) # add each row voter name to Voters list
        #If candidate name doesn't exist in Candidate list then add the name of the Candidate to form a list of Unique Candidate names
        if data[2] not in Candidate:
                Candidate.append(data[2])
                VotingCount_perCandidate.append(1)
        else: # If Candidate name already exist in Candidate list then increase the Voting Count for that Candidate in VotingCount_perCandidate list 
            candidate_index = Candidate.index(data[2])
            VotingCount_perCandidate[candidate_index] = VotingCount_perCandidate[candidate_index]  + 1
        

    #Find the maximum value in VotingCount_perCandidate list to figure out winner's index and then use that index to figure out winner name
    WinningIndex = VotingCount_perCandidate.index(max(VotingCount_perCandidate))
    Winner = Candidate[WinningIndex]


    textpath = os.path.join('Analysis', 'Analysis.txt')
    Textfile1 = open(textpath, "w")
    # write the ouput to terminal and  text file
    print("Election Results")   
    print("-------------------------")  
    Textfile1.writelines("Election Results\n")
    Textfile1.writelines("-------------------------\n")
           
    print(f"Total Votes: {len(Voters)}")
    print("-------------------------")   
    Textfile1.writelines(f"Total Votes: {len(Voters)}\n")
    Textfile1.writelines("-------------------------\n")


    for i in range(len(Candidate)):
          Voting_percentage = round((VotingCount_perCandidate[i] / len(Voters)) * 100 ,3)
          print(f"{Candidate[i]}: {Voting_percentage:5.3f}% ({VotingCount_perCandidate[i]})") # print the voting logistics for each candidate
          Textfile1.writelines(f"{Candidate[i]}: {Voting_percentage:5.3f}% ({VotingCount_perCandidate[i]})\n") 
    print("-------------------------")         
    print(f"Winner: {Winner}")
    print("-------------------------")         
    
    # Write the output to text file

    
    Textfile1.writelines("-------------------------\n")
    Textfile1.writelines(f"Winner: {Winner}\n")
    Textfile1.writelines("-------------------------\n")
    Textfile1.close()
          
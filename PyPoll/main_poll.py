import os
import csv

election_data = os.path.join("C:/Users/hahnh/OneDrive/Desktop/DataViz/Homework/Python_Challenge/PyPoll/Resources/election_data.csv")

#Set variables
voter_votes = []
candidates = []

#One set
#Intitial list of candidates. Make set of candidate list for individual names


with open(election_data, newline="") as csvfile:

    csvreader = csv.reader(csvfile)
    csvheader = next(csvreader)

    for row in csvreader:
        voter_votes.append(row[0])


#Complete list of candidates who recieved votes
        candidates.append(row[2])
        
candidate_list = list(set(candidates))
print(candidate_list)

#Count number of votes per candidate
candidate_votes = []
for votes in candidate_list:
    candidate_votes.append(candidates.count(votes))
print(candidate_votes)  

#Determine percentage of votes      
for x in range(len(candidate_list)):
    print(
        f"{candidate_list[x]}: {'{:.2%}'.format(candidate_votes[x]/len(candidates))} ({candidate_votes[x]})")
print("----------------------------------")
print(f"Winner: {candidate_list[candidate_votes.index(max(candidate_votes))]}")
print("----------------------------------")

# Create Analysis 
write_file = "poll_analysis.txt"

with open(write_file, "w") as txt_file:
    txt_file.write("Voter_Poll Analysis")
    txt_file.write("\n")
    txt_file.write("__________________________________")
    txt_file.write("\n")
    txt_file.write(f"Total Votes: {len(voter_votes)}")
    txt_file.write("\n")
    for x in range(len(candidate_list)):
        txt_file.write(
            f"{candidate_list[x]}: {'{:.2%}'.format(candidate_votes[x]/len(candidates))} ({candidate_votes[x]})")
        txt_file.write("\n")
    txt_file.write("__________________________________")
    txt_file.write("\n")
    txt_file.write(f"Winner: {candidate_list[candidate_votes.index(max(candidate_votes))]}")
    txt_file.write("\n")
    txt_file.write("__________________________________")






    
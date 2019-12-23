import pandas as pd
import os
import csv

Polling_results_file = os.path.join('Polling_Results_Report.csv')
summary_report=[]

# read election file and save to dataframe
election_file = "03-Python_Homework_PyPoll_Resources_election_data.csv"
election_file_pd = pd.read_csv(election_file)
# print(election_file_pd.head())



# The total number of votes casts
total_votes = election_file_pd["Voter ID"].count()
# print(total_votes)

# A complete list of candidates who received votes
all_candidates = election_file_pd.Candidate.unique()
# print(all_candidates)

# Total votes per candidates
votes_per_candidates = election_file_pd["Candidate"].value_counts() 
# print(votes_per_candidates.head())

# percentage of each candidate's vote
percentage_of_votes = (votes_per_candidates/total_votes)
# print(percentage_of_votes)

# Convert the votes_per_candidates into a DataFrame
votes_per_candidates_df = pd.DataFrame(votes_per_candidates)
# print(votes_per_candidates_df.head())

# Convert the percentage of votes into a DataFrame
percentage_of_votes_df = pd.DataFrame(percentage_of_votes)
# print(percentage_of_votes_df.head())

# Convert the column name into "Total Votes"
votes_per_candidates_df = votes_per_candidates_df.rename(
    columns={"Candidate": "Total Votes"})
# print(votes_per_candidates_df.head())

# Convert the column name into "Percentage of Votes"
percentage_of_votes_df = percentage_of_votes_df.rename(
    columns={"Candidate": "Percentage of Votes"})
# print(percentage_of_votes_df.head())

# Add formatting to the output
percentage_of_votes_df['Percentage of Votes'] = pd.Series(["{0:.3f}%".format(val * 100) for val in percentage_of_votes_df['Percentage of Votes']], index = percentage_of_votes_df.index)
# votes_per_candidates_df['Total Votes'] = pd.Series(["({0})".format(val) for val in votes_per_candidates_df['Total Votes']], index = votes_per_candidates_df.index)

total_percent_concat = pd.concat([percentage_of_votes_df, votes_per_candidates_df], axis=1)
# print(total_percent_concat)

# Display result



max_row_name = total_percent_concat.loc[total_percent_concat["Total Votes"]==total_percent_concat["Total Votes"].max()]
# print(max_row_name)


print("Election Results")
print("--------------------------------------------------")
print("Total Votes: ",total_votes)
print("--------------------------------------------------")
for k,v in total_percent_concat.iterrows():
    print("{name}: {percent} ({total})".format(name = k, percent = v["Percentage of Votes"], total = v["Total Votes"]))
print("--------------------------------------------------")
for k,v in max_row_name.iterrows():
    print("Winner: {name}".format(name=k))

print("--------------------------------------------------")

with open("Polling_Result.txt",'w') as line:
    line.write("Election Results \n")
    line.write("--------------------------------------------------\n")
    line.write("Total Votes: {total} \n".format(total = total_votes))
    line.write("--------------------------------------------------\n")
    for k,v in total_percent_concat.iterrows():
        line.write("{name}: {percent} ({total})\n".format(name = k, percent = v["Percentage of Votes"], total = v["Total Votes"]))
    line.write("--------------------------------------------------\n")
    for k,v in max_row_name.iterrows():
        line.write("Winner: {name}\n".format(name=k))
    line.write("--------------------------------------------------\n")
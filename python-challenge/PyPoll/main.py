import os
import csv


file= os.path.join("election_data.csv")
Output_file= os.path.join("Analysis", "final_analysis.txt")

#Total Vote Count
total_votes= 0

#Count Candidates and votes
no_candidates= []
group_vote_counts= {}
winner= " "
winning_vote_count= 0

with open(file) as election_data:
    reader = csv.reader(election_data)
    header= next(reader)

    for row in reader:
        total_votes= total_votes +1
        name= row[2]

        if name not in no_candidates:
            no_candidates.append(name)
            group_vote_counts[name] = 0
            group_vote_counts[name]= group_vote_counts[name]+ 1


with open(Output_file, "w") as txt_file:
    Results= (
        f"Election Results"
        f"Total Votes: {total_votes}")
    print(Results, end=" ")

    txt_file.write(Results)


    for candidate in group_vote_counts:
        votes= group_vote_counts.get(candidate)
        vote_percent= float(votes)/ float(votes) *100

    if (votes> winning_vote_count):
        winning_vote_count = votes
        winner= candidate


    output= f"{candidate}: {vote_percent: }% ({votes})"
    print(output, end= " ")

    txt_file.write(output)
    winner_summary= (
        f"Winner: {winner}"
        )
    
    print(winner_summary)

    txt_file.write(winner_summary)
    
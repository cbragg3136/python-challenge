import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

def get_data(readerobj):
    dataset = []
    for item in readerobj:
        dataset.append(item)

    return dataset


def voters(election_data):
    voter_id = []
    for item in election_data:
        voter_id.append(item[0])

    return voter_id


def candidates(election_data):
     candidate_votes = []
     for item in election_data:  
         candidate_votes.append(item[2])

with open (election_data_csv, 'r') as election_data_open:
    csvreader = csv.reader(election_data_open, delimiter= ',')

    csv_header = next(csvreader)
    lines = get_data(csvreader)

    print("Election Results\n-------------------------")  

    resultvoter_id = voters(lines)
    resultcandidate_votes = candidates(lines)

    total_voters = len(resultvoter_id)
    print(f"Total Votes Cast: {total_voters}")

    candidate_list = (resultcandidate_votes)




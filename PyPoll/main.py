import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')

with open (election_data_csv, 'r') as election_data_open:
    csvreader = csv.reader(election_data_open, delimiter= ',')

    csv_header = next(csvreader)
  
    candidatedict ={}
    total_count = 0

    for item in csvreader:
        total_count += 1
        if item[2] in candidatedict:
            candidatedict[item[2]] += 1
        else:
            candidatedict[item[2]] = 1

  
    print("\nElection Results\n-------------------------")  
    print(f"Total Votes Cast: {total_count}\n-------------------------")
    
    candidates = []
    values = []
    items = candidatedict.items()
    for item in items:
        candidates.append(item[0]), values.append(item[1])
        print(f'{item[0]}: {round(item[1]*100/total_count,1)}% ({item[1]})')

    print("-------------------------")
    print(f"Winner: {candidates[values.index(max(values))]}")



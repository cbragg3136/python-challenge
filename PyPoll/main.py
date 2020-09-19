import os
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')
election_data_text = os.path.join('analysis', 'results.txt')

with open (election_data_csv, 'r') as election_data_open:
    with open(election_data_text, 'w') as election_data_output:
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
        election_data_output.write("FINANCIAL ANALYSIS\n----------------------------\n")
        print(f"Total Votes Cast: {total_count}\n-------------------------")
        election_data_output.write(f"Total Votes Cast: {total_count}\n-------------------------\n")

        candidates = []
        values = []
        items = candidatedict.items()
        for item in items:
            candidates.append(item[0]), values.append(item[1])
            print(f'{item[0]}: {round(item[1]*100/total_count,1)}% ({item[1]})')
            election_data_output.write(f'{item[0]}: {round(item[1]*100/total_count,1)}% ({item[1]})\n')
            
        print("-------------------------")
        election_data_output.write("-------------------------\n")
        print(f"Winner: {candidates[values.index(max(values))]}")
        election_data_output.write(f"Winner: {candidates[values.index(max(values))]}")


# import modules for os and for reading csv file
import os

# module for reading csv file and path for reading csv file & writing text file
import csv

election_data_csv = os.path.join('Resources', 'election_data.csv')
election_data_text = os.path.join('analysis', 'results.txt')

# open the file for reading (csv reader) and splits the data at comma
with open (election_data_csv, 'r') as election_data_open:
    with open(election_data_text, 'w') as election_data_output:
        csvreader = csv.reader(election_data_open, delimiter= ',')

        # read the header row
        csv_header = next(csvreader)
    
        # created a dictionary to hold the candidates
        candidatedict ={}
        total_count = 0

        # loop through the item list to update the candidate dictionary with a tally/total of each occurrence of a candidate name. (Else) when the loop comes across a new candidate name, set that name equal to one. 
        # Cite: Johnny Bragg, personal communication, September 13, 2020
        for item in csvreader:
            total_count += 1
            if item[2] in candidatedict:
                candidatedict[item[2]] += 1
            else:
                candidatedict[item[2]] = 1

        # print statements to terminal and write to text file. Note '\n' is new line
        print("\nElection Results\n-------------------------")  
        election_data_output.write("FINANCIAL ANALYSIS\n----------------------------\n")

        # print to terminal and write to text file the total count of all votes within file
        print(f"Total Votes Cast: {total_count}\n-------------------------")
        election_data_output.write(f"Total Votes Cast: {total_count}\n-------------------------\n")

        # display the list of candidate dictionary keys and values (names and number of votes respectively) using the items() method to append and print the name, the number of votes, and percentage of total votes for each candidate. Within candidatedict {names/keys [0] : votes/value [1]}. 
        candidates = []
        values = []
        items = candidatedict.items()
        for item in items:
            candidates.append(item[0]), values.append(item[1])
            print(f'{item[0]}: {"{:.3f}".format(item[1]*100/total_count)}% ({item[1]})')
            election_data_output.write(f'{item[0]}: {"{:.3f}".format(item[1]*100/total_count)}% ({item[1]})\n')


        print("-------------------------")
        election_data_output.write("-------------------------\n")

        # finding the winner by finding the max number of votes/values within the index within the candidates list
        # Cite: Johnny Bragg, personal communication, September 15, 2020
        print(f"Winner: {candidates[values.index(max(values))]}")
        election_data_output.write(f"Winner: {candidates[values.index(max(values))]}")


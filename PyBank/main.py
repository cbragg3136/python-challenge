import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')
budget_data_text = os.path.join('analysis', 'results.txt')

#function to keeping reading file
def get_data(readerobj):
    dataset = []
    for item in readerobj:
        dataset.append(item)

    return dataset

#function for the total number of months
def date_count(budget_data):
    dates = []
    for item in budget_data:
        dates.append(item[0])
        #for each row get the column at the index position 0

    return dates
  
#function for net total amount of profit/losses 
def profit_sum(budget_data):
    profits = []
    for item in budget_data:
        profits.append(int(item[1]))
        #profits += int(item[1])

    return profits



with open(budget_data_csv, 'r') as budget_data_open:
    with open(budget_data_text, 'w') as budget_data_output:

        csvreader = csv.reader(budget_data_open, delimiter=',')
        #print(csvreader)
        #print(budget_data_open)

        #lines = budget_data_open.read()

        #print(lines)
        

        csv_header = next(csvreader)
        #print(csv_header)

        lines = get_data(csvreader)

        print("FINANCIAL ANALYSIS\n----------------------------")
        budget_data_output.write("FINANCIAL ANALYSIS\n----------------------------\n")

        resultdates = date_count(lines)
        resultprofits = profit_sum(lines)

        total_months = len(resultdates)
        print(f"Total Months: {total_months}")
        budget_data_output.write(f"Total Months: {total_months}\n")
    

        net = sum(resultprofits)
        print(f"Net Total Profit: {net}")
        budget_data_output.write(f"Net Total Profit: {net}\n")

        change_profits = []
        for i in range(1,len(resultprofits)):
            change_profits.append((int(resultprofits[i])) - (int(resultprofits[i-1])))

        avg_change = sum(change_profits)/len(change_profits)
        max_rev_change = max(change_profits)
        min_rev_change = min(change_profits)

        max_rev_change_date = str(resultdates[change_profits.index(max(change_profits))+1])
        min_rev_change_date = str(resultdates[change_profits.index(min(change_profits))+1]) 


        print("Avereage Profit Changes: $", round(avg_change,2))
        budget_data_output.write(f"Avereage Profit Changes: ${round(avg_change,2)}\n")
        print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
        budget_data_output.write(f"Greatest Increase in Revenue: {max_rev_change_date} (${max_rev_change})\n")
        print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")
        budget_data_output.write(f"Greatest Decrease in Revenue: {min_rev_change_date} (${min_rev_change})\n")

        
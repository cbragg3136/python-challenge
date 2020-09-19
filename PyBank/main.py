# import modules for os and for reading csv file
import os

# module for reading csv file and path for reading csv file & writing text file
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')
budget_data_text = os.path.join('analysis', 'results.txt')

# defined a function to read the file into a list, to prevent having to reset the readerobj
# Cite: Johnny Bragg, personal communication, September 15, 2020
def get_data(readerobj):
    dataset = []
    for item in readerobj:
        dataset.append(item)

    return dataset

# defined a function of the budget data. For loop to return the list of dates (to use for date_count)
def date_count(budget_data):
    dates = []
    for item in budget_data:
        dates.append(item[0])
        #for each row get the column at the index position 0

    return dates
  
# defined a function of the budget data. For loop to return for list of profit/losses (to use for profit_sum)
def profit_sum(budget_data):
    profits = []
    for item in budget_data:
        profits.append(int(item[1]))
      
    return profits

# open the file for reading (csv reader) and splits the data at comma
with open(budget_data_csv, 'r') as budget_data_open:
    with open(budget_data_text, 'w') as budget_data_output:

        csvreader = csv.reader(budget_data_open, delimiter=',')

        # read the header row
        csv_header = next(csvreader)
     
        # store the list from get_data function inside variable called rows
        # Cite: Johnny Bragg, personal communication, September 15, 2020
        rows = get_data(csvreader)

        # print statements to terminal and write to text file. Note '\n' is new line
        print("FINANCIAL ANALYSIS\n----------------------------")
        budget_data_output.write("FINANCIAL ANALYSIS\n----------------------------\n")

        # variables holding date_count and profit_sum lists (pulled from the defined functions)
        resultdates = date_count(rows)
        resultprofits = profit_sum(rows)

        # assumed the dates are unique and counted (len) the number of entries in list (resultdates) to get the total number of months (set as variable total_months). print to terminal and write result to text file.
        total_months = len(resultdates)
        print(f"Total Months: {total_months}")
        budget_data_output.write(f"Total Months: {total_months}\n")
    
        # Summed the resultprofits list to pull Net Total Profit
        net = sum(resultprofits)
        print(f"Net Total Profit: {net}")
        budget_data_output.write(f"Net Total Profit: {net}\n")

        # Cite for lines 69-95: Hetal. (2017, October 27). Python - How can I find difference between two rows of same column using loop in CSV file?. Stack Overflow. https://stackoverflow.com/questions/46965192/python-how-can-i-find-difference-between-two-rows-of-same-column-using-loop-in
        # create list (change_profits) of differences from a position i in a range minus one from that position. example [cell2 - cell1, cell3 - cell2, cell 4 - cell3] until end of rows/range
        change_profits = []
        for i in range(1,len(resultprofits)):
            change_profits.append((int(resultprofits[i])) - (int(resultprofits[i-1])))

        # add the items within the list of change_profits and divide by the length of the list for the average change in profits
        avg_change = sum(change_profits)/len(change_profits)

        # for generating the greatest increase and decrease in profits:
            # find the max and min values from the change_profits list 
        max_profit_change = max(change_profits)
        min_profit_change = min(change_profits)

        # for pulling the dates of greatest increase and decrease in profits:
            # pull the index at the 'max and min values' of the change_profits list within the list of months (result_dates) 
            # add one to the index (to pull the 2nd date)
        max_profit_change_date = str(resultdates[change_profits.index(max(change_profits))+1])
        min_profit_change_date = str(resultdates[change_profits.index(min(change_profits))+1]) 

        # use variables from greatest increase and decrease (see lines 73-85) in profits to print statements and write to text file
        print("Average Profit Change: $", round(avg_change,2))
        budget_data_output.write(f"Average Profit Change: ${round(avg_change,2)}\n")

        print("Greatest Increase in Profits:", max_profit_change_date,"($", max_profit_change,")")
        budget_data_output.write(f"Greatest Increase in Profits: {max_profit_change_date} (${max_profit_change})\n")

        print("Greatest Decrease in Profits:", min_profit_change_date,"($", min_profit_change,")")
        budget_data_output.write(f"Greatest Decrease in Profits: {min_profit_change_date} (${min_profit_change})\n")

        
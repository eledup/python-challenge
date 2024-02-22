# import csv file
import os
import csv

datacsv = os.path.join("csv", "election_data.csv")

#lists for data
id = []
county = []
candidate = []

#csv into lists and account for headers
with open(datacsv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)

    for row in csvreader:
        id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    # total votes
    votes = len(id)

    #list of candidates?
    candlist = []
    for can in candidate:
        if can not in candlist:
            candlist.append(can)

    # define calculation for each persons votes?
    # list.count(x) for candidate list??????
   
    c0count = candidate.count(candlist[0])
    c1count = candidate.count(candlist[1])
    c2count = candidate.count(candlist[2])

    c0percent = (c0count/votes)*100
    c1percent = (c1count/votes)*100
    c2percent = (c2count/votes)*100
    
    # declare winner
    # ifstatements if c > d+a d=winner etc? 
    if (c0count > c1count and c0count > c2count):
        winner = candlist[0]

    elif (c1count > c0count and c1count > c2count):
        winner = candlist[1]

    elif (c2count > c0count and c2count > c1count):
        winner = candlist[2]

    else:
        winner = "problem"        

    #output
    print("Election Results")
    print("------------")
    print(f"Total Votes: {votes}")
    print("------------")
    print(f"{candlist[0]}: {round(c0percent,3)}% ({c0count})")
    print(f"{candlist[1]}: {round(c1percent,3)}% ({c1count})")
    print(f"{candlist[2]}: {round(c2percent,3)}% ({c2count})")
    print("------------")
    print(f"Winner: {winner}")


# import text file
analysistxt = 'analysis/analysis.txt'

# write results to file
with open(analysistxt, 'w') as txtfile:
    txtfile.write("Election Results"
                  '\n' "------------"
                  '\n' f"Total Votes: {votes}"
                  '\n' "------------"
                  '\n' f"{candlist[0]}: {round(c0percent,3)}% ({c0count})"
                  '\n' f"{candlist[1]}: {round(c1percent,3)}% ({c1count})"
                  '\n' f"{candlist[2]}: {round(c2percent,3)}% ({c2count})"
                  '\n' "------------"
                  '\n' f"Winner: {winner}")
    
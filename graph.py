# importing csv module 
import csv
import datetime
from datetime import datetime
import matplotlib.pyplot as plt


# csv file name
march = "C:\\Users\\Schat\\Desktop\\stats_project\\25_MAR.csv"
april = "C:\\Users\\Schat\\Desktop\\stats_project\\29_APR.csv"


def getData(which): #function to parse data out of the CSV files
    # initializing the titles and rows list
    fields = []
    rows = []
    states = ["Alaska",
              "Alabama",
              "Arkansas",
              "Arizona",
              "California",
              "Colorado",
              "Connecticut",
              "District of Columbia",
              "Delaware",
              "Florida",
              "Georgia",
              "Hawaii",
              "Iowa",
              "Idaho",
              "Illinois",
              "Indiana",
              "Kansas",
              "Kentucky",
              "Louisiana",
              "Massachusetts",
              "Maryland",
              "Maine",
              "Michigan",
              "Minnesota",
              "Missouri",
              "Mississippi",
              "Montana",
              "North Carolina",
              "North Dakota",
              "Nebraska",
              "New Hampshire",
              "New Jersey",
              "New Mexico",
              "Nevada",
              "New York",
              "Ohio",
              "Oklahoma",
              "Oregon",
              "Pennsylvania",
              "Rhode Island",
              "South Carolina",
              "South Dakota",
              "Tennessee",
              "Texas",
              "Utah",
              "Virginia",
              "Vermont",
              "Washington",
              "Wisconsin",
              "West Virginia",
              "Wyoming"]  # all the states

    # for item in states:
    #         states[item].tolower()

    # reading csv file
    with open(which, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        fields = next(csvreader)

        for row in csvreader:
            rows.append(row)
    data = {}
    i = 0
    for row in rows:
        # row = [location_name, date, mean, all bed, bed, icu, icu, iuc, inv, inv, inv, deathsmean, deathlow, deathhigh, ....]

        date1 = datetime.strptime(row[1], '%m/%d/%Y')
        #   date1 = datetime(date1)
        apObj = datetime(2020, 3, 19)
        maobj = datetime(2020, 5, 10)

        if row[0] in states and date1 > apObj and date1 < maobj:
            stateName = row[0]
            deaMean = row[11]
            deaLow = row[12]
            deaHi = row[13]
            data[i] = [stateName, date1, deaMean, deaLow, deaHi]
            i = i + 1
        prevDate = date1
    return data


def plotStateData(dataOld, dataNew, state): #function to plot data state by state
    meanOld = []  # mean of daily deaths from original projections
    dateOld = []
    meanNew = []
    dateNew = []
    lowOld = []
    highOld = []
    lowNew = []
    highNew = []
    rangelow = -1
    rangeHigh = 0
    rangelow2 = -1
    rangeHigh2 = 0

    for i in dataOld: #get the point in the list where the data of this specfic state exists
        if dataOld[i][0] == state:
            if rangelow == -1:
                rangelow = i
                rangeHigh = i

            rangeHigh += 1

    for z in dataNew:
        if dataNew[z][0] == state:
            if rangelow2 == -1:
                rangelow2 = z
                rangeHigh2 = z
            rangeHigh2 += 1

    for k in range(rangelow, rangeHigh): #append data to new list for plot
        dateOld.append(dataOld[k][1])
        meanOld.append(round((float(dataOld[k][2]))))
        lowOld.append(round((float(dataOld[k][3]))))
        highOld.append(round((float(dataOld[k][4]))))

    for j in range(rangelow2, rangeHigh2):
        dateNew.append(dataNew[j][1])
        meanNew.append(round((float(dataNew[j][2]))))
        lowNew.append(round((float(dataNew[j][3]))))
        highNew.append(round((float(dataNew[j][4]))))

    y = meanOld
    plt.clf()


    plt.figure(figsize=(15, 8))
    plt.plot(dateOld, y, "-o", label="Projected Mean")  # mean deaths
    plt.plot(dateNew, meanNew, "-o", label="Actual Mean")
    plt.plot(dateOld, lowOld, "-o", label="Lower Uncertainty Bound (Projected)")
    plt.plot(dateOld, highOld, "-o", label="Upper Uncertainty Bound (Projected)")

    plt.legend(loc="best")
    plt.title("Deaths Per Day " + state)
    plt.xlabel("Month")
    plt.ylabel("People")
    plt.legend()
  #  plt.show()
    plt.savefig("C:\\Users\\Schat\\Desktop\\stats_project\\state_plots_pdf\\" +state +".pdf")
    plt.close()




#main
old = getData(march)
new = getData(april)

states = ["Alaska",
              "Alabama",
              "Arkansas",
              "Arizona",
              "California",
              "Colorado",
              "Connecticut",
              "District of Columbia",
              "Delaware",
              "Florida",
              "Georgia",
              "Hawaii",
              "Iowa",
              "Idaho",
              "Illinois",
              "Indiana",
              "Kansas",
              "Kentucky",
              "Louisiana",
              "Massachusetts",
              "Maryland",
              "Maine",
              "Michigan",
              "Minnesota",
              "Missouri",
              "Mississippi",
              "Montana",
              "North Carolina",
              "North Dakota",
              "Nebraska",
              "New Hampshire",
              "New Jersey",
              "New Mexico",
              "Nevada",
              "New York",
              "Ohio",
              "Oklahoma",
              "Oregon",
              "Pennsylvania",
              "Rhode Island",
              "South Carolina",
              "South Dakota",
              "Tennessee",
              "Texas",
              "Utah",
              "Virginia",
              "Vermont",
              "Washington",
              "Wisconsin",
              "West Virginia",
              "Wyoming"]  # all the states
for state in states:
    plotStateData(old, new, state)



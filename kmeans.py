#K-Means clustering implementation
import csv
import math
import random
import matplotlib.pyplot as plt

# ====
# Define a function that computes the distance between two data points
def distance(datapointX,datapointY,centX,centY):
    distance = math.sqrt(math.pow(centX-datapointX,2) + math.pow(centY-datapointY,2))
    return distance
    
# ====
# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html
def read_csv():
    f = open('databoth.csv')
    csv_f = csv.reader(f)
    countries = []
    for row in csv_f:
        countries.append(row)
    #To Remove the Initial entry that is the label
    del countries[0]
    dataset = countries
    return countries

# ====
# Write the initialisation procedure

#The Complete CSV dataset
dataset = read_csv()

#Create a matrix of the Data in the CSV with a possible of 5 entries per record
#[0] - Contains Country Name
#[1] - Contains X Coordinates
#[2] - Contains Y Coordinates
#[3] - Contains Distance From Cluster
#[4] - Contains Cluster Number which point belongs to.
data = [[1000 for x in range(5)] for x in range(len(dataset))]

#Number of Cluster Variables
clusters = int(input("Please Enter The Amount Of Clusters You Want: "))

#Number of Iterations
iterations = int(input("Please Enter The Amount Of Iterations You Want: "))

#Sanity Check Enable
check = input("Do You Want To Run A Sanity Check? Y or N: ")

#The Centroids list
centroids = []

#Function for getting random Points as centroids
def init_centroids():
    #Getting the amount of centroid points determined by the cluster amount
    
    #print "Centroids initiated at: "
    for i in range(clusters):
        centroids.append(random.choice(dataset))

def populateMatrix():
    totalEntriesList = list(enumerate(dataset))
    #Creates a matrix of The Total amount of entries by 5 for (Name,X,Y,Distance,Cluster)
    for index,item in totalEntriesList:
        data[index][0] = item[0]
        data[index][1] = item[1]
        data[index][2] = item[2]

def get_cluster():
    #Variables
    datasetlist = list(enumerate(dataset))
    currentDistance = 100
    currentCluster = 0
    counter = 0

    #Run through all datapoints to find their closest Centroid
    for i in centroids:
        currentCluster = i
        for index,item in datasetlist:
            #Calculate Distance from point to centroid
            currentDistance = distance(float(item[1]),float(item[2]),float(centroids[counter][1]),float(centroids[counter][2]))

            #Check if Distance is less then assign to that cluster
            if currentDistance < data[index][3]:
                data[index][3] = currentDistance
                data[index][4] = centroids.index(currentCluster)
        counter += 1
        
def update_centroid():
    #Variables
    counter = 0
    totalPoints = 0
    totalX = 0
    totalY = 0
    newX = 0
    newY = 0
    #Running through all datapoints to update centroid to new coordinates
    for i in range(clusters):
        for item in data:
            if item[4] == counter:
                totalPoints += 1
                totalX += float(item[1])
                totalY += float(item[2])
        #Calculate new mean
        newX = totalX/totalPoints
        newY = totalY/totalPoints
        #Setting the new coordinates for centroid
        centroids[counter][1] = newX
        centroids[counter][2] = newY
        counter += 1
    
def get_cluster_count():
    #Variables
    counter = 0
    count = [0 for x in range(clusters)]

    
    for i in range(clusters):
        for item in data:
            if item[4] == counter:
                count[counter] += 1
        counter += 1
    return count

def show_cluster_count():
    #Variables
    counter = 0
    count = [0 for x in range(clusters)]

    #Setup for look and feel
    print ("After " + str(iterations) + " Iterations, The Amount Of Countries For Each Cluster is: ")
    
    #Run through all data to get the count of each cluster
    for i in range(clusters):
        for item in data:
            if item[4] == counter:
                count[counter] += 1
        print ("Cluster " + str(i+1) + " has " + str(count[counter]) + " entries."+ "\n")
        counter += 1
    return count

def show_cluster_countries():
    #Variables
    counter = 0
    countries = ["" for x in range(clusters)]

    #Run through data to get the countries that belong to each cluster
    for i in range(clusters):
        for item in data:
            if item[4] == counter:
                countries[counter] = str(countries[counter]) + item[0]+ " , "
        print ("The Countries included in Cluster " + str(counter+1) + " is: " +str(countries[counter]) + "\n")
        counter += 1

def show_cluster_mean():
    #Variables
    counter = 0
    count = [[0 for x in range(3)] for x in range(clusters)]

    #Run through all the data to get all the mean value
    for i in range(clusters):
        for item in data:
            if item[4] == counter:
                 count[counter][0] += 1
                 count[counter][1] += float(item[1])
                 count[counter][2] += float(item[2])
        print ("The mean for Cluster " + str(counter+1) + " is: Birth Rate per 1000: " + str(count[counter][1]/count[counter][0]) +" Life Expectancy: "+ str(count[counter][2]/count[counter][0]))
        counter += 1

def sanity_check():
    #Check to see if the kmeans is converging
    if check == 'Y':
        counter = 0
        count = [0 for x in range(clusters)]
        for i in range(clusters):
            for item in data:
                if item[4] == counter:
                    count[counter] += float(item[3])
            print ("Cluster " + str(i+1) + " total: " + str(count[counter]))
            counter += 1
        print ("\n")

def plot_data():
    # Used to plot the data using matplotlib
    plt.axis([0, 70, 0, 100])
    plt.ylabel('Life Expectancy')
    plt.xlabel('Birth Rate')

    # Plotting the Centroids on graph
    for item in centroids:
        plt.scatter(item[1], item[2], marker='s', color='y')

    # Plotting the points on the graph and assigning them to the correct cluster
    # Currently only gave a 3 cluster symbol assignment
    symbol = "-"
    setColor = "y"
    for item in data:
        if item[4] == 0:
            symbol = 'o'
            setColor = "r"
        elif item[4] == 1:
            symbol = 'x'
            setColor = "b"
        elif item[4] == 2:
            symbol = '^'
            setColor = "g"

        scat = plt.scatter(item[1], item[2], marker=symbol, color=setColor, alpha=.3)

    plt.show()
    plt.clf()

# ====
# Implement the k-means algorithm, using appropriate looping
def KMeans():
    init_centroids()
    populateMatrix()
    for i in range(iterations):
        get_cluster()
        update_centroid()
        sanity_check()


# ====
# Print out the results
KMeans()

#These can be used to check all the maths
#show_cluster_count()
#show_cluster_countries()
#show_cluster_mean()
plot_data()
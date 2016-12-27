
import matplotlib.pyplot as plt
import kmeans as km

km.KMeans()
centroids = km.centroids
data = km.data

def plot_data():
    # Used to plot the data using matplotlib
    #plt.plot([1, 2, 3, 4], [2, 4, 6, 8], 'b-')
    plt.axis([0,70,0,100])  # xmin,xmax,ymin,ymax
    plt.ylabel('Life Expectancy')
    plt.xlabel('Birth Rate')

    #Plotting the Centroids on graph
    for item in centroids:
        plt.scatter(item[1], item[2], marker='s', color='y')

    #Plotting the points on the graph and assigning them to the correct cluster
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

        plt.scatter(item[1], item[2], marker=symbol, color=setColor, alpha=.3)

    plt.show()

plot_data()


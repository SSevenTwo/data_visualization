import matplotlib.pyplot as plt

from randomwalk import RandomWalk

while True:
    rwalk = RandomWalk(50000)
    rwalk.walk()

    plt.scatter(rwalk.x_values,rwalk.y_values,c=rwalk.x_values, cmap = plt.cm.Blues,
        edgecolor = 'none', s=2)
        
    #Marking the start and end points
    plt.scatter(0,0, c='green', s=20)
    plt.scatter(rwalk.x_values[-1],rwalk.y_values[-1], c='red', s=20)
    
    #Removing axes
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    
    plt.show()

    
    active = input("Make another walk (y/n)? ")
    if active.lower() == 'n':
        break
    

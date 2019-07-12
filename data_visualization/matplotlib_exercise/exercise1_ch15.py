import matplotlib.pyplot as plt

#Typing out values
#x_values = [1,2,3,4,5]
#y_values = [1,8,27,64,125]

#Doing automatic calculations
x_values = list(range(1,1001))
y_values = [x**3 for x in x_values]

#Plotting the points to make a line. Adjusting plot line thickness.
#plt.plot(x_values,y_values,linewidth=5)

#Plotting the points only. Adjusting the size of the points.
#Edge color is the border color of the points
plt.scatter(x_values, y_values, c=y_values, cmap =plt.cm.Purples, edgecolor = 'none',s=10)
#c represents color. We could say c= red, to make the y values red. But we used c map,
#which allows us to change the y value colors into a gradient.

#Adjusting labels
plt.title("Cubic Numbers")
plt.xlabel("Value",fontsize = 10)
plt.ylabel("Cubed Value",fontsize = 10)

#Adjusting axis scales. The first two points are the x scale while y is the next two.
plt.axis([0,1100,0,1300000000])

#Adjusting the ticks of the graph
plt.tick_params(axis = 'both', labelsize = 10)

#Save the graph as a picture. Second argument makes it smaller and removes white spaces.
plt.savefig("cubic_plot.png", bbox_inches="tight")

#Display the graph in a window.
plt.show()



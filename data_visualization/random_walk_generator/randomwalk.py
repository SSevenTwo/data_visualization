from random import choice

class RandomWalk():
    """A class which generates random walks"""
    
    def __init__(self, num_of_points = 5000):
        """Ïnitializes random walk attributes."""
        self.num_of_points = num_of_points
        
        #The walk begins at 0,0
        self.x_values = [0]
        self.y_values = [0]
        
    def walk(self):
        """Generates the points of the walks"""
        
        #Will loop until the number of points is reached
        while len(self.x_values)<self.num_of_points:
            
            #Choose directions and how far to move.
            x_direction = choice([-1,1])
            x_distance = choice([0,1,2,3,4])
            x_move = x_direction * x_distance
            
            y_direction = choice([-1,1])
            y_distance = choice([0,1,2,3,4])
            y_move = y_direction * y_distance
            
            #Enforces the rule that at least x or y must change
            if x_move == 0 and y_move ==0:
                continue
                
            #Calculate the next point, by adding the move to the previous move.
            next_x = self.x_values[-1] + x_move
            next_y = self.y_values[-1] + y_move
            
            #Add these new coordinates to the list of points.
            self.x_values.append(next_x)
            self.y_values.append(next_y)

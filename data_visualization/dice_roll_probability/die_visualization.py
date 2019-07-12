from dice import Die
import pygal

die_1 = Die(8)
die_2 = Die(8)

results=[]
for roll in range(1000):
    results.append(die_1.roll() + die_2.roll())

frequencies=[]
max_result = die_1.sides + die_2.sides
label = ""

for value in range(2,max_result + 1):
    frequencies.append(results.count(value))
#    label += str(value)
    
print(frequencies)
print(label)

hist = pygal.Bar()
hist.title = "Results of rolling two die 1000 times"
hist.x_labels = ['3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("Die", frequencies)
hist.render_to_file("die_visual.svg")

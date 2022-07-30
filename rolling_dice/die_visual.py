from die import Die

from plotly.graph_objs import Bar, Layout
from plotly import offline

# d6 oluştur

die = Die()

# bazı atışlar yap ve sonuçları bir listede döndür

results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# sonuçları analiz et
frequincies = []  

for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequincies.append(frequency)
    
    
# sonuçları görselleştir.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequincies)]
    
x_axis_config = {'title': 'Sonuç'}
y_axis_config = {'title': 'Sonucun frekansı'}

my_layout = Layout(title='Bir D6 yı 1000 kez atmanın sonuçları', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data' : data, 'layout':my_layout}, filename='d6.html')
#print(frequincies)

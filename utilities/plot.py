import requests
import pandas as pd
import matplotlib.pyplot as plt

result = requests.get('http://localhost:3000/cets').json()
data = {}
data['time'] = [x['t'] for x in result]
data['price'] = [x['floor_price'] for x in result]
data['listed'] = [x['listed_count'] for x in result]

plt.plot('time', 'listed', data=data)
ax = plt.gca()
ax.axes.xaxis.set_visible(False)
plt.title('Cets Listed Count')
plt.show()

df = pd.DataFrame.from_dict(data)
print(df)

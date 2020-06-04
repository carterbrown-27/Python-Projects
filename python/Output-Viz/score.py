from pandas import DataFrame
import matplotlib.pyplot as plt

data = {
    'Rank' : [1482,1410,1480,1445,1460,1463,1473,1474]
}

df = DataFrame(data, columns=['Rank'])
df.plot(y='Rank', kind='line')
plt.show()

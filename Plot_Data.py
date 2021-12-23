import json
import matplotlib.pyplot as plt
from Covid_API import add_data


add_data()

with open('Covid_Data.txt', 'r') as file:
    data = file.read()

data = json.loads(data)

x_values = data.keys()
x_values_list = list(x_values)

labels = []
for x in range(0,140,20):
    labels.append(x_values_list[x])

positions = [0,20,40,60,80,100,120]

if __name__ == "__main__":
    plt.xticks(positions, labels)
    plt.xticks(rotation = -45)
    plt.title("Combined Death Figures in the UK due to Covid")
    plt.ylabel("Combined Deaths")
    plt.xlabel("Date")
    plt.grid(True)
    plt.tight_layout()
    plt.plot(range(len(data)),data.values())
    plt.show()
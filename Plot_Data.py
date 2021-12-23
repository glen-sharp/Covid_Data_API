import json
import matplotlib.pyplot as plt
from Covid_API import add_data

if __name__ == "__main__":
    add_data()

    with open('Covid_Data.txt', 'r') as file:
        data = file.read()

    data = json.loads(data)

    x_values = data.keys()
    x_values_list = list(x_values)
    
    labels = (x_values_list[0],x_values_list[20],x_values_list[40],x_values_list[60],x_values_list[80],x_values_list[100],x_values_list[120])
    positions = (0,20,40,60,80,100,120)

    plt.xticks(positions, labels)
    plt.xticks(rotation = -45)
    plt.title("Combined Death Figures in the UK due to Covid")
    plt.ylabel("Combined Deaths")
    plt.xlabel("Date")
    plt.grid(True)
    plt.tight_layout()

    plt.plot(range(len(data)),data.values())
    plt.show()
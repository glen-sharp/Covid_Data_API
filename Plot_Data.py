import json
import matplotlib.pyplot as plt
from Covid_API import add_data
if __name__ == "__main__":
    add_data()

    with open('Covid_Data.txt', 'r') as file:
        data = file.read()

    data = json.loads(data)

    plt.plot(range(len(data)),data.values())
    plt.show()
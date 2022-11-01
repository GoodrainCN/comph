import get_data
import matplotlib.pyplot as plt

data = get_data.run()
x_data = data[0]
x_data = [i*100 + 200 for i in x_data]
y_data = data[1]
y_data = [i*100 + 198.5 for i in y_data]
temp_x = 0
temp_y = 0
for i in range(0,len(x_data)):
    temp_x = x_data[i]
    # temp_y = 398.41 - y_data[i]
    temp_y = y_data[i]
    print(temp_x, temp_y)

plt.plot(x_data,y_data)
plt.show()


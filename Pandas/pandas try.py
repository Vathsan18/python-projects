import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 7, 10]

# Create Scatter Plot
plt.scatter(x, y, color='red')  # 'color' to specify the color of points
plt.title("Simple Scatter Plot")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid(True)  # Adding grid for better visualization

# Show plot
plt.show()

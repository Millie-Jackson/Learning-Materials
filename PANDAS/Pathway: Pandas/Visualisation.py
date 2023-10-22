
# Resource: youtube.com/watch?v=7IV_UZaVgJg&ab_channel=AiCore

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

# Sample data
data = {'Year': [2010, 2011, 2012, 2013, 2014],
        'Sales': [10000, 12000, 9000, 15000, 11000],
        'Expenses': [6000, 7000, 8000, 9000, 9500],
        'Profit': [4000, 5000, 100, 6000, 1500]}

# Create a Pandat DataFrame
df = pd.DataFrame(data)

## CREATE A MATPLOTLIB FIGURE ##
 
## LINE GRAPH ##

# Create a new figure with a specific size (8 inches in width and 5 inches in height)
plt.figure(figsize=(8, 5), facecolor='r')

# Plot the 'Sales' data (y_axis) from the DataFrame df against the 'Year' data (x-axis)
# - 'marker='o'' specifies that data points should be marked with circles
# - 'linestyle='-'' specifies that lines should connect the data points
# - 'color='b'' specifies the color of the line as blue
# - 'label='Sales (Matplotlib) assigns a label for this line for the legend
plt.plot(df['Year'], df['Sales'], marker='*', linestyle=':', color='k', label='Sales (Matplotlib)')

# Set the label for the x-axis
plt.xlabel('Year')
# Set the label for the y-axis
plt.ylabel('Amount')
# Set the title for the plot
plt.title('Sales Over the Years (Matplotlib)')

# Display a legend of the plot, which is useful when multiple lines are present
plt.legend()
# Display a grid on the plot for better readability
plt.grid(True)

# Show the plot
plt.show

## MULTIPLE LINE GRAPH ##

# Create a single plot for all three data series
plt.figure(figsize=(10, 6))

# Plot Sales
plt.plot(df['Year'], df['Sales'], marker='o', label='Sales', color='b')
# Plot Expenses
plt.plot(df['Year'], df['Expenses'], marker='o', label='Expenses', color='r')
# Plot Profit
plt.plot(df['Year'], df['Profit'], marker='o', label='Profit', color='g')

# Set plot labels and legend
plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Sales, Expenses and Profit Over Time')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()

## SUBPLOTS ##

# Create a figure and subplots within the same figure
# The subplots grid is 1 x
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))

# Plot Sales
ax1.plot(df['Year'], df['Sales'], marker='o', label='Sales', color='b')
ax1.set_title('Sales')
ax1.set_xlabel('Year')
ax1.set_ylabel('Amount')

# Plot Expenses
ax2.plot(df['Year'], df['Expenses'], marker='o', label='Expenses', color='r')
ax2.set_title('Expenses')
ax2.set_xlabel('Year')
ax2.set_ylabel('Amount')

# Plot Profit
ax3.plot(df['Year'], df['Profit'], marker='o', label='Profit', color='g')
ax3.set_title('Profit')
ax3.set_xlabel('Year')
ax3.set_ylabel('Amount')

# Add plot labels and legend to the entire figure
fig.suptitle('Sales, Expenses and Profit Over Time', fontsize=16)
fig.legend(loc='upper right')
fig

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.9])

# Show the plot
plt.show()

## OR ##

# Create a figure and subplots with 2 rows and 2 columns
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(15, 20))

# Plot Sales
axes[0, 0].plot(df['Year'], df['Sales'], marker='o', label='Sales', color='b')
axes[0, 0].set_title('Sales')
axes[0, 0].set_xlabel('Year')
axes[0, 0].set_ylabel('Amount')

# Plot Expenses
axes[0, 1].plot(df['Year'], df['Expenses'], marker='o', label='Expenses', color='r')
axes[0, 1].set_title('Expenses')
axes[0, 1].set_xlabel('Year')
axes[0, 1].set_ylabel('Amount')

# Plot Profit
axes[1, 0].plot(df['Year'], df['Profit'], marker='o', label='Profit', color='g')
axes[1, 0].set_title('Profit')
axes[1, 0].set_xlabel('Year')
axes[1, 0].set_ylabel('Amount')

# Create a combined subplot for all three data series
axes[1, 1].plot(df['Year'], df['Sales'], marker='o', label='Sales', color='b')
axes[1, 1].plot(df['Year'], df['Expenses'], marker='o', label='Expenses', color='r')
axes[1, 1].plot(df['Year'], df['Profit'], marker='o', label='Profit', color='g')
axes[1, 1].set_title('Combined')
axes[1, 1].set_xlabel('Year')
axes[1, 1].set_ylabel('Amount')
axes[1, 1].legend()

# Add plot labels and legend to the entire figure
fig.suptitle('Sales, Expenses and Profit Over Time', fontsize=16)
fig

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()

## BAR GRAPHS ##

# Sample data: Product names and their corresponding sales figures
data = {'Products': ['Product A', 'Product B', 'Product C', 'Product D'],
        'Sales_2021': [2500, 3800, 2100, 4500],
        'Sales_2022': [2700, 3900, 2200, 4600]}

df = pd.DataFrame(data)

df.plot.bar()

## OR ##

# Specify the column for the x-axis (products) and the columns to compare (sales for 20021 and 2022)
x_column = 'Products'
y_columns = ['Sales_2021', 'Sales_2022']

# Create a bar plot
# Can turn it into a horizontal bar graph by using barh() instead of bar()
# Can make it a stacked bar graph by passing in argument: stacked = True
df.plot.bar(x=x_column, y=y_columns, color=['skyblue', 'lightcoral'])

# Adding labels and a title
plt.label(x_column)
plt.ylabel("Sales Figures")
plt.title("Sales Figures by Product and Year")

# Display the plot
plt.xticks(rotation=45) # Rotation of x labels
plt.tight_layout()
plt.show()

## OR ##

import numpy as np
# Specify the column for the x-axis (products) and the columns to compare (sales for 2021 and 2022)
x_column = "Products"
y_columns = ["Sales_2021", "Sales_2022"]

# Extra data for plotting
products = df[x_column]
sales_2021 = df[y_columns[0]]
sales_2022 = df[y_columns[1]]

# Set the width of the bars
bar_width = 0.35

# Create an index for the x-axis based on the number of products
x_index = np.arange(len(products))

# Create bar positions for 2021 and 2022
bar_positions_2021 = x_index - bar_width / 2
bar_positions_2022 = x_index + bar_width / 2

# Create a bar plot for 2021
plt.bar(bar_positions_2021, sales_2021, width=bar_width, label="Sales 2021", color="skyblue")

# Create a bar plot for 2022
plt.bar(bar_positions_2022, sales_2022, width=bar_width, label="Sales 2022", color="lightcoral")

# Adding labels and a title
plt.xlabel(x_column)
plt.ylabel("Sales Figures")
plt.title("Sales Figures by Product and Year")

# Set x-axis ticks and labels
plt.xticks(x_index, products, rotation=45)

# Add a legend
plt.legend()

# Display the plot
plt.tight_layout()
plt.show()

## SCATTER PLOTS ##

# Sample data
data = {
    "x": [1, 2, 3, 4, 5],
    "predicted": [2, 8, 4, 9, 6],
    "actual": [1, 4, 7, 4, 5]
    }

# Create a DataFrame
df = pd.DataFrame(data)

# Using pandas .plot()
# df.plot.scatter(x="X", y="Y", label="Data Points", color="blue", marker="o")
# Using matplotlib
plt.scatter(df["x"], df["predicted"], label="Data Points", color="blue", marker="o")

# Add labels and titles
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot Example")

# Add a legend (optional)(required for matplotlib, pandas plot does so automatically)
# plt.legend()

# Show plot
plt.show()

## SUBPLOTS ##

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4)) # 1 row 2 columns

# Plot "predicted" on the first subplot (ax1)
ax1.scatter(df["x"], df["predicted"], label="Predicted", color="blue", marker="o")
ax1.set_xlabel("X-axis")
ax1.set_ylabel("predicted")
ax1.set_title("Predicted vs. X")
ax1.legend()

# Plot "actual" on the second subplot (ax2)
ax2.scatter(df["x"], df["actual"], label="Actual", color="red", marker="x")
ax2.set_xlabel("X-axis")
ax2.set_ylabel("Actual")
ax2.set_title("Actual vs. X")
ax2.legend()

# Adjusted spacing between subplots
plt.tight_layout()

# Show the figure with subplots
plt.show()

## BOX PLOTS ##

# Sample data with more columns
data = {
    "Catagory": ["A", "A", "B", "B", "B", "C", "C", "C", "C"],
    "Values_1": [15, 18, 24, 28, 32, 10, 12, 14, 18],
    "Values_2": [12, 16, 20, 25, 30, 8, 10, 14, 16],
    "Values_3": [10, 14, 18, 22, 28, 6, 8, 12, 14]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create boxplots for multiple columns using pandas and matplotlib
plt.figure(figsize=(10, 6)) # optional: Set the figure size

# Specify the columns you want to include in the boxplot
columns_to_plot = ["Values_1", "Values_2", "Values_3"]

# Create the boxplots
# You can groupby using the "by" argument
# e.g. by="Catagory"
df.boxplot(column=columns_to_plot, vert=True)
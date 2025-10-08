# Program to print the fruit(s) repeating the most times

fruits = ["apple", "banana", "apple", "mango", "banana", "apple", "orange", "mango", "banana"]

# Count frequency of each fruit
fruit_count = {}

for fruit in fruits:
    fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

# Find maximum repetition
max_count = max(fruit_count.values())

# Print fruit(s) with max repetition
print("Fruits repeating the most times:")
for fruit, count in fruit_count.items():
    if count == max_count:
        print(fruit, "->", count, "times")

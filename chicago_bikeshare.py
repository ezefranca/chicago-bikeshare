
# coding: utf-8

# Here goes the imports
import csv
import matplotlib.pyplot as plt

# Let's read the data as a list
print("Reading the document...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Let's check how many rows do we have
print("Number of rows:")
print(len(data_list))

# Printing the first row of data_list to check if it worked.
print("Row 0: ")
print(data_list[0])
# It's the data header, so we can identify the columns.

# Printing the second row of data_list, it should contain some data
print("Row 1: ")
print(data_list[1])

input("Press Enter to continue...")
# TASK 1
# TODO: Print the first 20 rows using a loop to identify the data.
print("\n\nTASK 1: Printing the first 20 samples")
for i in range(0,20):
    print(data_list[i])
# Let's change the data_list to remove the header from it.
data_list = data_list[1:]

# We can access the features through index
# E.g. sample[6] to print gender or sample[-2]

input("Press Enter to continue...")
# TASK 2
# TODO: Print the `gender` of the first 20 rows

print("\nTASK 2: Printing the genders of the first 20 samples")
for line in data_list[:20]:
    print(line[6])

# Cool! We can get the rows(samples) 
# iterating with a for and the columns(features) by index.
# But it's still hard to get a column in a list. Example: List with all genders

input("Press Enter to continue...")
# TASK 3
# TODO: Create a function to add the columns(features) of a list in another list in the same order

def column_to_list(data, index):
    """ Coverts a collum of an bidimensional in a linear array
    :param data: bidimensional matrix list
    :param index: line or collum of matrix
    :return: list of the line (or collum) selected
    """
    column_list = []
    for i in range(0, len(data)):
        column_list.append(data[i][index])
    # Tip: You can use a for to iterate over the samples, get the feature by index and append into a list
    return column_list

def count_elements(data, x):
    """
    Function count element in the list
    Args:
        :data list for count elements
        :x element for count ins the data
    Returns:
        Count elements find in the data
    """
    count = 0
    for ele in data:
        if ele == x:
            count += 1
    return count

def count_genders(column_list):
    """ Count occurencies of genders in a list.
    :param column_list: List with males and females
    :return: array with popular_male and polular_female
    """
    male = count_elements(column_list, "Male")
    female = count_elements(column_list, "Female")
    return [male, female]


# Let's check with the genders if it's working (only the first 20)
print("\nTASK 3: Printing the list of genders of the first 20 samples")
print(column_to_list(data_list, -2)[:20])

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(column_to_list(data_list, -2)) is list, "TASK 3: Wrong type returned. It should return a list."
assert len(column_to_list(data_list, -2)) == 1551505, "TASK 3: Wrong lenght returned."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TASK 3: The list doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we know how to access the features, let's count how many Males and Females the dataset have
# TASK 4
genders = column_to_list(data_list, 6)
male = count_genders(genders)[0]
female = count_genders(genders)[1]

# Checking the result
print("\nTASK 4: Printing how many males and females we found")
print("Male: ", male, "\nFemale: ", female)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert male == 935854 and female == 298784, "TASK 4: Count doesn't match."
# -----------------------------------------------------

input("Press Enter to continue...")
# Why don't we creeate a function to do that?
# TASK 5
# TODO: Create a function to count the genders. Return a list
# Should return a list with [count_male, counf_female] (e.g., [10, 15] means 10 Males, 15 Females)

def count_gender(data_list):
    """ Count occurencies of genders in a list.
    :param data_list: List with males and females
    :return: array with popular_male and polular_female
    """
    male = 0
    female = 0
    for gender in column_to_list(data_list, 6):
        if gender == 'Male':
            male += 1
        elif gender == 'Female':
            female +=1
    return [male, female]


print("\nTASK 5: Printing result of count_gender")
print(count_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(count_gender(data_list)) is list, "TASK 5: Wrong type returned. It should return a list."
assert len(count_gender(data_list)) == 2, "TASK 5: Wrong lenght returned."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TASK 5: Returning wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Now we can count the users, which gender use it the most?
# TASK 6
# TODO: Create a function to get the most popular gender and print the gender as string.
# We expect to see "Male", "Female" or "Equal" as answer.

def most_popular_gender(data_list):
    """ Find most popular gender in a list.
    :param data_list: List of genders
    :return: string of the most popular
    """
    answer = "Male"
    if count_gender(data_list)[1] > count_gender(data_list)[0]:
        answer = "Female"
    elif count_gender(data_list)[1] == count_gender(data_list)[0]:
        answer = "Equal"
    return answer


print("\nTASK 6: Which one is the most popular gender?")
print("Most popular gender is: ", most_popular_gender(data_list))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert type(most_popular_gender(data_list)) is str, "TASK 6: Wrong type returned. It should return a string."
assert most_popular_gender(data_list) == "Male", "TASK 6: Returning wrong result!"
# -----------------------------------------------------

# If it's everything running as expected, check this graph!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('Gender')
plt.xticks(y_pos, types)
plt.title('Quantity by Gender')
plt.show(block=True)

input("Press Enter to continue...")
# TASK 7
# TODO: Plot a similar graph for user_types. Make sure the legend is correct.

def count_user_types(data_list):
    """
       Get types user of list by print in legend of map
       Args:
           data_list: list of user types
       Returns:
           Array with types user
    """
    user_types = column_to_list(data_list, 5)
    customer = count_elements(user_types, "Customer")
    subscriber = count_elements(user_types, "Subscriber")
    return [customer, subscriber]


print("\nTASK 7: Check the chart!")
user_types_list = column_to_list(data_list, 5)
types = ["Customer", "Subscriber"]
quantity = count_user_types(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantity')
plt.xlabel('User Types')
plt.xticks(y_pos, types)
plt.title('Quantity by User Types')
plt.show(block=True)


input("Press Enter to continue...")
# TASK 8
# TODO: Answer the following question
male, female = count_gender(data_list)
print("\nTASK 8: Why the following condition is False?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "We have unknow genders, they can be Female"
print("Answer:", answer)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert answer != "Type your answer here.", "TASK 8: Write your own answer!"
# -----------------------------------------------------

input("Press Enter to continue...")
# Let's work with the trip_duration now. We cant get some values from it.
# TASK 9
# TODO: Find the Minimum, Maximum, Mean and Median trip duration.
# You should not use ready functions to do that, like max() or min().
trip_duration_list = column_to_list(data_list, 2)

def find_min_trip(data_list):
    """ Find Median, Minimum, Maximum and Mean in a list.
    :param data_list: list with all trip values
    :return: array with Minimum, Maximum, Mean and Median trip duration
    """
    trip_min = 10000000000
    trip_max = 0
    trip_mean = 0
    durations = list(map(int, data_list))
    for trip in durations:
        trip_mean += trip
        if trip < trip_min:
            trip_min = trip
        elif trip > trip_max:
            trip_max = trip
    trip_median = find_median_trip(durations)
    trip_mean = trip_mean / len(durations)
    return [trip_min, trip_max, trip_mean, trip_median]

def find_median_trip(lst) -> int:
    """ Find median in a list.
      Args:
          lst: List
      Returns:
          the median
    """

    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return sortedLst[index] + sortedLst[index + 1]/2.0

results = find_min_trip(trip_duration_list)
print(results)

min_trip = results[0]
max_trip = results[1]
mean_trip = results[2]
median_trip = results[3]

print("\nTASK 9: Printing the min, max, mean and median")
print("Min: ", min_trip, "Max: ", max_trip, "Mean: ", mean_trip, "Median: ", median_trip)

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert round(min_trip) == 60, "TASK 9: min_trip with wrong result!"
assert round(max_trip) == 86338, "TASK 9: max_trip with wrong result!"
assert round(mean_trip) == 940, "TASK 9: mean_trip with wrong result!"
assert round(median_trip) == 670, "TASK 9: median_trip with wrong result!"
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 10
# Gender is easy because usually only have a few options. How about start_stations? How many options does it have?
# TODO: Check types how many start_stations do we have using set()
stations = column_to_list(data_list, 3)
user_types = list(set(stations))

print("\nTASK 10: Printing start stations:")
print(len(user_types))

# ------------ DO NOT CHANGE ANY CODE HERE ------------
assert len(user_types) == 582, "TASK 10: Wrong len of start stations."
# -----------------------------------------------------

input("Press Enter to continue...")
# TASK 11
# Go back and make sure you documented your functions. Explain the input, output and what it do. Example:
# def new_function(param1: int, param2: str) -> list:
# """ Example function with annotations.
#       Args:
#           param1: The first parameter.
#           param2: The second parameter.
#       Returns:
#           List of X values
#       """

input("Press Enter to continue...")
# TASK 12 - Challenge! (Optional)
# TODO: Create a function to count user types without hardcoding the types
# so we can use this function with a different kind of data.
print("Will you face it?")
answer = "yes"

def get_genders(list, genders):
    """
    Get genders count
    :param list: list of all genders and a set of genders
    :return: list with genders
    """
    genders_count = []
    for gender in genders:
        x = list.count(gender)
        genders_count.append(x)
    return genders_count

def count_items(column_list):

    item_types = set(column_list)
    count_items = get_genders(column_list, item_types)
    return item_types, count_items

if answer == "yes":
    # ------------ DO NOT CHANGE ANY CODE HERE ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTASK 11: Printing results for count_items()")
    print("Types:", types, "Counts:", counts)
    assert len(types) == 3, "TASK 11: There are 3 types of gender!"
    assert sum(counts) == 1551505, "TASK 11: Returning wrong result!"
    # -----------------------------------------------------
# artificial intelligence lab
 All solved lab of FAST NUCES Lahore campus _ 2022 Spring

# ----------------------------------------------------------------
#                                   LAB - 2
# ----------------------------------------------------------------

# Question 1.1:  
    Concatenate two lists 
    Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Question 1.2:   
    Convert a tuple to a Dictionary. (3 Marks)
    Write a Python program to convert a tuple to a dictionary. 
    Sample Output: {'w': 2, 'r': 3}

# Question 1.3:
    Reverse a tuple (2 Marks)
    Write a Python program to reverse a tuple.

# Question 1.4:
    Sort a Tuple (3 Marks)
    Sort a tuple of tuples by 2nd item.
    Given: tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
    Expected: (('c', 11), ('a', 23), ('d', 29), ('b', 37))

# Question 1.5:
    Create a Dictionary (5 Marks)
    Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.
    Sample Dictionary:
    sample_dict = {
        "name": "Kelly",
        "age": 25,
        "salary": 8000,
        "city": "New york"}
    # Keys to extract
    keys = ["name", "salary"]

# Question 1.6:
    Nested Dictionary (5 Marks)
    Write a Python program to change Brad’s salary to 8500 in the following dictionary.
    Given:
    sample_dict = {
        'emp1': {'name': 'Jhon', 'salary': 7500},
        'emp2': {'name': 'Emma', 'salary': 8000},
        'emp3': {'name': 'Brad', 'salary': 500}
    }


# ----------------------------------------------------------------
#                                    LAB - 3
# ----------------------------------------------------------------

# Question 1:
    Write a Python program to find the length of a set, apply all sets
    operations(union,intersection) and print the results,find maximum and the minimum value in a
    set,create a shallow copy of sets,check if a set is a subset of another set, remove all elements
    from a given set,check if two given sets have no elements in common.check if a given set is
    superset of itself and superset of another given set.
    set1 = {1,2,3,4,5}
    set2 = {4,5,6,7,8}

# Question 2:
    Python program to count the number of vowels using sets in a given string.
    sample output
    Input : Hello World
    Output : No. of vowels : 3
    2: Exception Handling (10 marks)

# Question 3:
    Write a function to add, mul, divide two numbers x and y. Implement exception handling
    technique
    (try..except clause) for handling possible exceptions in the scenario.

# ----------------------------------------------------------------
#                                    LAB - 4
# ----------------------------------------------------------------

# Question 1:
    For a list of integers, find square and cube for each value using lambda function.

# Question 2:
    Form a queue such that it works in FIFO order

# Question 3:
    Create a class for rectangle shape that calculates its area based upon the length and width

# Question 4:
    Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.


# ----------------------------------------------------------------
#                                    LAB - 6
# ----------------------------------------------------------------

# Question 1:
    4.1	NumPy is a library for the Python which adds support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays. Create two arrays A= [1,2,3,2,3,4,3,4,5,6] and B= [7,2,10,2,7,4,9,4,9,8]. You need to get the positions where elements of A and B match. Use a numpy function or implement your own logic. 
    Desired Outcome:
    [1, 3, 5, 7]

# Question 2:

    4.2.1   You need to findinsights about data using as many different techniques as you can. Don’t use libraries that haven’t been covered yet.

    Hint: Explore the dataset, look for the outliers, missing values, etc
    Use the automobile data set provided in the Google class room to explore EDA functions.

        1.	Check first five entries of data set.   # data.head().
        2.	Check last five entries of dataset.# data.tail().
        3.	Check the columns of data set.# data.columns.
        4.	Check unique values for each column    # data.numique().
        5.	Check the missing values for each column.   # data.isnull().sum().
        6.	Drop unnecessary data columns     # new_data= data.drop([‘column_name’,‘second_column_name’], axis=1).
        7.	Drop null value. #df.dropna(subset=df.columns,inplace=True) 

# Question 3:
    4.2.2	Data Analysis is the process of exploring and analyzing large datasets to make predictions and decisions. It involves a broad set of activities to clean, process, transform a data collection to learn from it and derive meaningful insights. Its profound application can be seen in analysing consumer behaviour in retail industry to reach out to the right customers and perform targeted marketing to increase sales. One sample dataset has been provided which lists various features of cars. You need to use your data analysis skills in answering the questions given ahead. 

        (Libraries Involved: Numpy, Pandas)
        Dataset: automobile_data.csv
        Initial Steps: 
        •	Import necessary libraries
        •	Upload/Read the csv file using pandas
        •	Review the dataset for identifying any missing values
        •	Observe the different attributes and entries

        Questions
        a.	Find the most expensive car from the dataset and display its price
        b.	Calculate total cars per manufacturer and show the result
        c.	Read the details of vehicles against Toyota manufacturer and print them
        d.	Arrange the cars according to the prices (highest-lowest) and display relevant information for first 5 rows only


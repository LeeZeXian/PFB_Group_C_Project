  # -*- coding: utf-8 -*-

## Function to return key
def MyKeyFn_One(a):
    return a[1]

## Function to return key
def MyKeyFn_Zero(a):
    return a[0]

# If data in column is fluctuating, find the difference between the next data
# This ignore whether the difference between the two data is negative or positive

def test_column_increasing(data, column_index):
  for i in range(1, len(data)):
    if data[i][column_index] <= data[i - 1][column_index]:
      return False
  return True

# Test whether the column data is always decreasing
def test_column_decreasing(data, column_index):
  for i in range(1, len(data)):
    if data[i][column_index] >= data[i - 1][column_index]:
      return False
  return True

def find_differences(data, column_index):
  differences = []

  for i in range(1, len(data)):
    #print(data[i], data[i][1])
    difference = float(data[i][column_index]) - float(data[i - 1][column_index])
    if difference != 0:
      differences.append((data[i][0], difference))  
  
  ## Sort base on value
  sorted_differences = sorted(differences, key=MyKeyFn_One, reverse=True)
  
  # Check if the column is increasing
  if test_column_increasing(data, column_index):
  # Find the day and amount of the highest increasing column

  # Print the results
    print("each day is higher than previous day")
    text1= ("each day is higher than previous day")
  
    print(f"{sorted_differences[1][0]} , amount of ${sorted_differences[1][1]}")
    text2 = (sorted_differences[0][0] , sorted_differences[0][1])
    
    text3 = 0
  
  elif test_column_decreasing(data, column_index):
    
# Find the day and amount of the highest decreasing column
    print("each day is lower than previous day")
    text1= ("each day is lower than previous day")
    
    print(f"{sorted_differences[-1][0]} , amount of ${sorted_differences[-1][1]}")
    text2 = (sorted_differences[-1][0] , sorted_differences[-1][1])
    
    text3 = 1
    
  else:
   # If the column data is fluctuating, find the top three differences
    print("The column is not always increasing.")
  
    print("each day is fluctuating")
    text1= ("each day is fluctuating")
    
    text2 = 0   ## Export 0, use top_3_second_elements(output) funtions for fluctuating data
  
    text3 = 2
  return sorted_differences , text1, text2, text3


def top_3_second_elements(list_of_lists):
    """
    Function will find the top 3 positive numbers of the second elements in a list of lists
    """

    second_elements = [inner_list[1] for inner_list in list_of_lists if len(inner_list) >= 2]
    positive_second_elements = [num for num in second_elements if num > 0]
    negative_second_elements = [abs(num) for num in second_elements if num < 0]

    return positive_second_elements[:3], negative_second_elements[3:] 

def check_data_for_difference(data, column_index):
    
    # Find all differences
    differences, text1, text2, text3 = find_differences(data, column_index)

    positive_list = []
    sorted_positive = []
    for i in range(1, len(differences)):
        if differences[i][column_index] > 0:
            print((differences[i]))
            positive_list.append(differences[i])
            
    ## Sort base on Key[0], which is 'Day'
    #sorted_positive = sorted(positive_list, key=lambda x: (x[0]), reverse=False)
    sorted_positive = sorted(positive_list, key=MyKeyFn_Zero, reverse=False)
    
    negative_list = []
    sorted_negative = []
    for i in range(1, len(differences)):
        if differences[i][column_index] < 0:
            print((differences[i]))
            negative_list.append(differences[i])
            
    ## Sort base on Key[0], which is 'Day'
    sorted_negative = sorted(negative_list, key=MyKeyFn_Zero, reverse=False)
    
    return sorted_positive,  sorted_negative,  text1, text2, text3

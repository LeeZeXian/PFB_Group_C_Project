# -*- coding: utf-8 -*-

## Function to return key, get csv data. grab the list of 1st or second item
def MyKeyFn_One(a):
    return a[1] #Data (Amt)

## Function to return key, get csv data.
def MyKeyFn_Zero(a):
    return a[0] #Day 

# Test for increasing data
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

# If data in column is fluctuating, find the difference between the next data
# This ignore whether the difference between the two data is negative or positive
def find_differences(data, column_index):
  differences = []

  for i in range(1, len(data)):
    difference = float(data[i][column_index]) - float(data[i - 1][column_index])
    if difference != 0:
      differences.append((data[i][0], difference))  
     
  # Sort base on value
  sorted_differences = sorted(differences, key=MyKeyFn_One, reverse=True)

  # Check if the column is increasing
  if test_column_increasing(data, column_index):
  # Find the day and amount of the highest increasing column

  # Print the results
    print("each day is higher than previous day")
    text1= ("each day is higher than previous day")
  
    print(f"{sorted_differences[0][0]} , amount of ${sorted_differences[0][1]}")
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
   # If the column data is fluctuating, find the top thress differences
    print("The column is not always increasing.")
  
    print("each day is fluctuating")
    text1= ("each day is fluctuating")
    
    text2 = 0   ## Export 0, use top_3_second_elements(output) funtions for fluctuating data
  
    text3 = 2
  return sorted_differences , text1, text2, text3

def top_3_second_elements(list_of_lists):
    """
    Function will find top 3 positive number of second element in list of lists
    """

    second_elements = [inner_list[1] for inner_list in list_of_lists if len(inner_list) >= 2]
    positive_second_elements = sorted([num for num in second_elements if num > 0], reverse=True)
    negative_second_elements = sorted([abs(num) for num in second_elements if num < 0], reverse=False)

    return positive_second_elements[:3], negative_second_elements[3:] 
    

def check_data_for_difference(data, column_index):
    
    # Find all differences
    differences, text1, text2, text3 = find_differences(data, column_index)
    
    positive_list = [] #Convert to list
    sorted_positive = [] #Convert to list
    for i in range(1, len(differences)):
        if differences[i][column_index] > 0:
            print((differences[i]))
            positive_list.append(differences[i])
            
    ## Sort base on Key[0], which is 'Day'
    sorted_positive = sorted(positive_list, key=MyKeyFn_Zero, reverse=False)
#Key function will take first number on positive or negative list, then do reverse sorting. Positive list is arranged via biggest to smallest day, reverse function reverses this.    

    negative_list = [] #Convert to list
    sorted_negative = [] #Convert to list
    for i in range(1, len(differences)):
        if differences[i][column_index] < 0:
            print((differences[i]))
            negative_list.append(differences[i])
    
    ## Sort base on Key[0], which is 'Day'
    sorted_negative = sorted(negative_list, key=MyKeyFn_Zero, reverse=False)
    
    return sorted_positive,  sorted_negative,  text1, text2, text3

def cash_on_hand(data):
    # Extract the column index (replace with actual index)
    column_index = 1  
    
    # Check data list for increasing, descresing or fluctuating and find the difference
    sorted_positive,  sorted_negative, text1, text2, text3 = check_data_for_difference(data, column_index)
   
    # Write into Summary.txt file
    with open('summaryreport.txt', 'a') as outfile:
        if text3 == 0 :
            outfile.write("[Cash Surplus]: Cash on %s \n" % (text1))
            outfile.write("[Highest Cash Surplus]: Day: %s, Amount: SGD%s \n" % (text2[0], abs(text2[1])))
        elif text3 == 1:
            outfile.write("[Cash Deficit]: Cash on %s \n" % (text1))
            outfile.write("[Highest Cash Deficit]: Day: %s, Amount: SGD%s \n" % (text2[0], abs(text2[1])))
        elif text3 == 2:
            if sorted_positive:
                for day, difference in sorted_positive:
                    outfile.write("[Cash Surplus] Day: %s, Amount: SGD%s \n" % (day, abs(difference)))
                positive_top = sorted(sorted_positive, key=MyKeyFn_One, reverse=True)
                outfile.write("[Highest Cash Surplus] Day: %s, Amount: SGD%s \n" % (positive_top[0][0], positive_top[0][1]))
                outfile.write("[2nd Highest Cash Surplus] Day: %s, Amount: SGD%s \n" % (positive_top[1][0], positive_top[1][1]))
                outfile.write("[3rd Highest Cash Surplus] Day: %s, Amount: SGD%s \n" % (positive_top[2][0], positive_top[2][1]))

            if sorted_negative:
                for day, difference in sorted_negative:
                    outfile.write("[Cash Deficit] Day %s, Amount: $%s \n" % (day, abs(difference)))
                negative_top = sorted(sorted_negative, key=MyKeyFn_One, reverse=False)
                outfile.write("[Highest Cash Deficit] Day %s, Amount: $%s \n" % (negative_top[0][0], abs(negative_top[0][1])))
                outfile.write("[2nd Highest Cash Deficit] Day %s, Amount: $%s \n" % (negative_top[1][0], abs(negative_top[1][1])))
                outfile.write("[3rd Highest Cash Deficit] Day %s, Amount: $%s \n" % (negative_top[2][0], abs(negative_top[2][1])))
 
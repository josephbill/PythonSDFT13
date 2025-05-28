from itertools import combinations
# printing the difference between every pair of adjacent elements 
arr = [10,15,20,25]  # Assume its sorted - input []  output []
"""
Adjacent Traversal 
1. traverse the array with attempt to get adjacent elements
   for loop i in range(len(arr) - 1):
        current = arr[i]  # current element
        next_element = arr[i+1]  # next element 
2. difference between the adjacent elements
range(start,stop,step)
"""
for i in range(len(arr) - 1): 
    current = arr[i]
    print(i)
    print(f"Current element: {current}")
    next_element = arr[i+1]
    print(i+1)
    print(f"Next element: {next_element}")
    absolute_difference = abs(current - next_element)
    print(f"Difference between {current} and {next_element} is {absolute_difference}")
    
"""
Unique Pairings 
Print all unique pairs in the array 
(1,2), (1,3), (2,3)
1. convert the array to a set to remove duplicates 
2. convert set back to list [1(0),2(1),3(2)]
range(Start,stop,step)
3. loop to get pairings -> how 
   for i in range(len(arr)) 1,2  i + 1
       for j in range(i+ 1, len(arr))  2
           print(arr[i], arr[j])
"""
arr = [1,1,2,2,3,3]
unique_array = set(arr)
print(unique_array)
arr = list(unique_array)
print(arr)
for i in range(len(arr)):
    print(i)
    for j in range(i + 1, len(arr)):
        print(j)
        print(f"pairs ({arr[i],arr[j]})")
 
  
'''
1. Get a unique array by flattening the inner list [1,1,2,3,3]
2. same steps as above 
'''
def flattenPairs(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):
            # extend : list items and joins them to another lists 
            flat.extend(item)
        else:
            flat.append(item)
            
    return list(combinations(flat,2))

print(flattenPairs( [1,[1,2,3],3]))

print(list([1,[1,2,3],3]))

### SLIDING WINDOW TECHNIQUE 
'''
find the sum of every window of 3 elements : 4
(0,1,2) (1+2+3)
(1,2,3) (2,3,4)
(2,3)  (3,4,5)
1. move iterations to element at 3 (2) , window sum i , i + 1, i + 2 
'''
arr=  [1,2,3,4,5]
for i in range(len(arr) - 2):
    print(i)
    print(arr[i], arr[i+1], arr[i+2])
    windowsum = arr[i] + arr[i+1] + arr[i+2]
    print(windowsum)
    
    
'''

How do you get the start pointer and end pointer in this array 
Sorting , 
Check if any pair in the sorted array given below adds to the given target 
target = 9

'''
arr = [1,3,4,5,7,10]
startLeft = arr[0]
endRight = arr[-1] # arr.length - 1 
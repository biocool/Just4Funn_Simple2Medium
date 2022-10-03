##################################################################################################################################################################################################################
'''
Reverse to Make Equal
Given two arrays A and B of length N, determine if there is a way to make A equal to B by reversing any subarrays from array B any number of times.
Signature
bool areTheyEqual(int[] arr_a, int[] arr_b)
Input
All integers in array are in the range [0, 1,000,000,000].
Output
Return true if B can be made equal to A, return false otherwise.
Example
A = [1, 2, 3, 4]
B = [1, 4, 3, 2]
output = true
After reversing the subarray of B from indices 1 to 3, array B will equal array A.
'''
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################
#because we can reverse any subarray then we can swap any two elements and it means we can sort an array (or have any permutation of that).
#1- Brute force: computing all permutatoin
#2- better: sorting two arrays and comparing them (O(nlogn)) space O(1)
#3- seems optimal : precomputing a hashtable with having the frequency of each element and then we can use these hash tables to compare the arrays 
#3- teta(N) time. and O(M) space (M = max (A,B))
##################################################################################################################################################################################################################
##################################################################################################################################################################################################################
import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

#my example A = [|4,5,65,76,333|,456,||2310,3453||]
#B = [333,76,65,5,456,3453,2310]
def are_they_equal(array_a, array_b):
  # Write your code here
  #assume the same length 
  array_a.sort()
  array_b.sort()
  array_len = len(array_a)
  flag_equal = 1
  for i in range(array_len):
    if array_a[i] != array_b[i]:
      flag_equal = 0
  return flag_equal
  
  










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.
def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 4
  a_1 = [1, 2, 3, 4]
  b_1 = [1, 4, 3, 2]
  expected_1 = True
  output_1 = are_they_equal(a_1, b_1)
  check(expected_1, output_1)

  n_2 = 4
  a_2 = [1, 2, 3, 4]
  b_2 = [1, 2, 3, 5]  
  expected_2 = False
  output_2 = are_they_equal(a_2, b_2)
  check(expected_2, output_2)

  # Add your own test cases here
  n_3 = 8 
  a_2 = [4,5,65,76,333,456,2310,3453]
  b_2 = [333,76,65,5,4,456,3453,2310]
  expected_3 = True
  output_3 = are_they_equal(a_2, b_2)
  check(expected_3, output_3)
  

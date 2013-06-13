### SortingTester - Joren Vaes - Created on 08 - 06 - 2013
###
### This tester will generate a random list of integers, between 50 and 150 values long, filled with random values from 0 to 250.
### The list can contain dublicates.
### 
### The sorting stage expects a sorting algorithm to take the list, and sort it, returning a new sorted version.
### This sorted version then goes through a few tests, checking it's length, it's contents, and, ofcourse, whether or not its sorted.
### 
### This is just a first version of this tester, I'm planning on adding more functionalities and such.
### 
###
### To use a different algorithm, simply change both the import quicksort in the imports section and the function in "do some actual sorting" part
###
###
### Good luck and have fun testing!
### 
### Created by Joren Vaes - last edit on 08/06/2013


print "\nSortingTester - version 1.0\n\n\n================STARTUP================\n"

###############
### IMPORTS ###
############### 

from SpecificationLibrary import *
from heapsort import *
import random
import time
import os

print "Imported files."

########################
### Assign variables ###
########################

number_of_errors = 0
length = random.randint(50, 150)
random_list = []

########################
### Define functions ###
########################

def test_is_array_sorted(array):
	print "\nChecking if the list is sorted...."
	assert for_all(range(0,(len(array)-1)), lambda i:\
		array[i] <= array[i+1])

def test_length_still_same(sorted_array, unsorted_array):
	print "\nChecking if the sorted list contains as much values as the original list..."
	assert len(sorted_array) == len(unsorted_array)

def test_array_contents_same(sorted_array, unsorted_array):
	print "\nChecking if the contents of the sorted list are the same as those of the unsorted list..."
	for i in range(0, len(sorted_array)):
		unsorted_array.remove(sorted_array[i])
	assert(len(unsorted_array) == 0)

def terminate():
	print "\n\nError occured, no use continuing. Shutting down."
	os._exit(0)

##########################	
### Create random list ###
##########################

for i in range(0, length):
	random_list = random_list + [random.randint(0, 250)]

#########################################	
### Store backup for later comparison ###
#########################################
	
sort_list = list(random_list)

###########################
### Print status report ###
###########################


print "Initialized data."
print "The length of the list is", length, "values. \n"
print "================SORTING================\n"


##############################
### Do some actual sorting ###
##############################


start_time = time.clock()
sorted_list = sort(sort_list)
end_time = time.clock()


################################
### Yet another statusreport ###
################################


print "Sorting took", end_time - start_time, "seconds. \n"
print "================TESTING================"


######################
### Do some tests! ###
######################


try:
	test_length_still_same(sorted_list, random_list)
except (AssertionError, TypeError):
	print "List is not the right length!"
	number_of_errors += 1
	terminate()
else:
	print "\n	-Length of the lists is equal."

	
try:
	test_array_contents_same(sorted_list, random_list)
except (AssertionError, TypeError):
	print "Sorted list does not contain the right values!"
	number_of_errors += 1
	terminate()
else:
	print "\n	-Sorted list contains the right values."

	
try:
	test_is_array_sorted(sorted_list)
except (AssertionError, TypeError):
	print "List is not sorted!"
	number_of_errors += 1
	terminate()
else:
	print "\n	-List is sorted!"


print "\n\nTests complete! No errors ocured, sorting alorithm works!"
print "\n\nTerminating program"
os._exit(0)




'''
* Christine Downey
* 06/18/2021
* CS210
'''

import re
import string

def mainMenu(): # function for main menu
	print("1. List of all items purchased with the number of times each item was purchased")
	print("2. List how many times a specific item was purchased on a given day")
	print("3. All items purchased on a given day with the number of times each item was purchased")
	print("4. Exit")

def countWords(words): # function to get read list and output the items and quantity sold
	text = open("Input_File.txt" , "r")
	d = dict()
	for line in text:
		words = line.split()
		for word in words:
			if word in d:
				d[word] = d[word] +1
			else:
				d[word] = 1
	keys = d.keys()
	for k in keys:
		print(str(k) + ": " + str(d[k]))
	text.close()

	return 0;

def countWord(foodName): # function to get the quantity of the item called for
	text = open("Input_File.txt" , "r")

	d = dict()
	for line in text:
		words = line.split()
		for word in words:
			if word in d:
				d[word] = d[word] + 1
			else:
				d[word] = 1
	text.close()

	convertedString = foodName.capitalize() #capitalize the first letter of input
	if d.get(convertedString):
		return d.get(convertedString);
	else:
		print("\nPlease try again.")
		return 0;
	
def listName(choice): # function to list the items
	text = open("Input_File.txt" , "r")
	result = dict()
	for line in text:
		words = line.split()
		for word in words:
			if word in result:
				result[word] = result[word] +1
			else:
				result[word] = 1
	
	keys = result.keys()
	for k in keys:
		print(str(k))
	text.close()
	return 0;

def histoList(choice): # function to make data histogram
	fp = open("Input_File.txt")
	dict_of_words = dict()
	for line in fp:
		for word in line.strip(string.punctuation).split():
			if(not dict_of_words.get(word)):
				dict_of_words[word] = 1
			else:
				dict_of_words[word] += 1
	print("Item Frequency")
	print("----------------")
	for x in dict_of_words.keys():
		print(str(x) + ": " +("*"*dict_of_words[x]))
	fp.close()
	return 0;

def freqData(choice): #function to write into file
	text = open("Input_File.txt" , "r")
	d = dict()
	for line in text:
		words = line.split()
		for word in words:
			if word in d:
				d[word] = d[word] +1
			else:
				d[word] = 1
	text.close()

	f = open("frequency.dat", "w")
	keys = d.keys()
	for k in keys:
		f.write(str(k) + " " + str(d[k]))
		f.write("\n")
	f.close()
	return 0;

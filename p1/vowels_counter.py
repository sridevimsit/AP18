#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	s = input()
	# the input string is in s
	# remove pass and start your code here
	num=0
	for char in s :
		if char in "aeiou":
			num=num+1
	print(num)
    


if __name__== "__main__":
	main()

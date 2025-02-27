Practice Questions
1. What are escape characters?
ans.Escape characters are special characters in python that allow you to include characters in a string that are normally difficult to type(like new lines, tabs, or quotes)
eg:- print("this is a line\This is a line")
     output = This is a line
	      This is a line
 		
2. What do the \n and \t escape characters represent?
ans.\n - moves text to next line
    \t - adds a big tabular space between the text

3. How can you put a \ backslash character in a string?
ans. To print a backslash you need to add two "\\" in the string.
     eg:- print("his is a backslash:\\")
     output = This is a backslash:\

4. The string value "Howl's Moving Castle" is a valid string. Why isn’t it 
a problem that the single quote character in the word Howl's isn’t 
escaped?
ans.The reason why this is not a problem is because the whole string is quoted
    inside double quotes " ".
    but incase you use single quotes then you must escape it by \
    eg:-printHowl\'s Moving Castle')  # Escape needed!
	output:-Howl's Moving Castle
	
5. If you don’t want to put \n in your string, how can you write a string 
with newlines in it?
ans.By using """ triple quotes(any single or double)
    eg:- text ="""This is line 1
         This is line 2
         This is line 3"""
     print(text)
    output:- This is line 1
	     This is line 2
             This is line 3

6. What do the following expressions evaluate to?
 •	'Hello world!'[1]
ans inde[1] will print e
 •	'Hello world!'[0:5]
ans index [0:5] slices from index 0 to 4
 •	'Hello world!'[:5]
ans index[:5] slices from start index[0] till 4
 •	'Hello world!'[3:]
ans slices from index[3] till end
 7. 
What do the following expressions evaluate to?
 •	'Hello'.upper()
ans converts all letter to uppercase letters
 •	'Hello'.upper().isupper()
ans 'Hello'.upper converts all letters to uppercase then .isupper() checks if all
    letters are uppercase and since they are final result is True.
 •	'Hello'.upper().lower()
ans 'hello'.upper converts hello to uppercase letters then .lower() converts all
    the letters to lower case.
 8. What do the following expressions evaluate to?
 •	'Remember, remember, the fifth of November.'.split()
ans .split() will split this string into a list of words like
    ['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']

 •	'-'.join('There can be only one.'.split())
ans this will split words and join them with -
    output - There-can-be-only-one.

 9. What string methods can you use to right-justify, left-justify, and center 
a string?
ans. string.rjust(width) :- right justifies the text
     string.ljust(width) :- left justifies the text
     string.center(width) :- centers the text

for example :- 
		text = "hello"
		print(text.rjust(10)) #right-justifies the text , add spaces on left
		print(text.ljust(10)) #left-justifies the text, add spaces on right
		print(text.center(10)# centers the text adds spaces on both sides

 10. How can you trim whitespace characters from the beginning or end of 
a string?
ans. By using
 string.strip() #removes white spaces from both sides
 string.lstrip() #removes white spaces from left side
 strign.rstrip() #removes white spaces from right side


        
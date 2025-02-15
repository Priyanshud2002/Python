practice Questions

 1. What does the code for an empty dictionary look like?
 ans. emptyDictionary = {}
 
 2. What does a dictionary value with a key 'foo' and a value 42 look like?
 ans dictionary = {'key':42}
 
 3. What is the main difference between a dictionary and a list?
 ans.   list:- it is an ordered collection of values indexed by integers.
               eg- list[0] gives first element of the list
        dictionary:- it is an unordered collection of key-value pairs where
        values are accessed using keys instead of numerical integers

        
 4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
 ans. You will get an key error because ['foo'] is not a key in the
      dictionary.
      
 5. If a dictionary is stored in spam, what is the difference between the 
 expressions 'cat' in spam and 'cat' in spam.keys()?
 ans. both expressions 'cat' in spam and spam.keys find the keys in the
 dictionary and return true or false if there is 'cat' in it.
 
 6. If a dictionary is stored in spam, what is the difference between the 
 expressions 'cat' in spam and 'cat' in spam.values()?
 ans. 'cat' in spam searches if 'cat' is a key in the dictionary
       'cat' in spam.values() check if 'cat' is one of the values

 7. What is a shortcut for the following code?
    if 'color' not in spam:
        spam['color'] = 'black'
    ans. spam.setdefault('color', 'black')
 8. What module and function can be used to “pretty print” dictionary 
    values?
    ans.    import pprint
            pprint.pprint(dictionary)

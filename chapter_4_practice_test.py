Practice Questions (Chapter 4)
1. What is []?
ans. [] creates an empty list in python with no elemets which stores
      variables,strings

      
2.
    1.How would you assign the value 'hello' as the third value in a list stored 
    in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].)
    ans.
        spam = [2, 4, 6, 8, 10]
        spam[2] = 'hello'
        print(spam)

        
    2. For the following three questions, let’s say spam contains the list ['a', 
    'b', 'c', 'd'].        
 a. What does spam[int('3' * 2) / 11] evaluate to?
 ans spam[int('3'*2) / 11]
     will do first '3' * 2 which is 33
     then it will change the string 33 to int
     and then 33 / 11 will divide 33 by 11
     which is 3.0 the final answer
 b. What does spam[-1] evaluate to?
 ans. [-1] will print the last element of the string.
 c. What does spam[:2] evaluate to?
 ans spam[:2] will print the elements inside the list from index 0 to 1
 
 
 For the following three questions, let’s say bacon contains the list  
[3.14, 'cat', 11, 'cat', True].
 6. What does bacon.index('cat') evaluate to?
 7. bacon.index('cat') will evaluate to 1 as the index number of cat is 1
What does bacon.append(99) make the list value in bacon look like?
ans. bacon.append(99) will add 99 at the end of the bacon list.
 8. What does bacon.remove('cat') make the list value in bacon look like?
ans. bacon.remove('cat') will remove cat from the bacon list.


 9. What are the operators for list concatenation and list replication?
 ans. for concatenation we shall use '+' and for replication '*'
 
 10. What is the difference between the append() and insert() list methods?
 ans. append() adds to the list while insert() inserts item at a specific
      index.

 11. What are two ways to remove values from a list?
     spam = {3, 0, 11, 50)
     suppose i want to remove 0 from the spam list then i will
     del spam[0]
     remove(0)
    
 12. Name a few ways that list values are similar to string values.
 ans. both support len() function to get length
      both support indexing and slicing
      both can be iterated over using loops
      both are sequences of elements
      
 13. What is the difference between lists and tuples?
 ans Lists are mutable(can be changed)
     tuples are immutable(cannot be changed)
     
 14. How do you type the tuple value that has just the integer value 42 in it?
 ans. myTuple = (42.)
 15. How can you get the tuple form of a list value? How can you get the list 
form of a tuple value?
ans.    Convert list to tuple: tuple(my_list)
        Convert tuple to list: list(my_tuple)
 16. Variables that “contain” list values don’t actually contain lists directly. 
    What do they contain instead?
    ans.    Variables that "contain" list values actually store references to the list in memory, not the list itself.
    
 17. What is the difference between copy.copy() and copy.deepcopy()?
 ans.   copy.copy() creates a shallow copy (copies references, not nested objects).
copy.deepcopy() creates a deep copy (recursively copies all objects, including nested ones).

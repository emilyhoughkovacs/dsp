# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> The biggest difference is that a list is mutable (can be changed) and a tuple is immutable. Tuples are enclosed by parenthesis `()`, whereas lists use brackets `[]`. You can use tuples as keys for dictionary because they are immutable but you cannot use a list because it is mutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Unlike lists, every element in a set must be unique. Sets are unordered but lists are ordered. A set uses curly braces `{}`. A common example for using a set is uniqueness testing. In comparison, you would have to use a list to represent the Fibbonacci sequence, because its ordering matters and its elements are not unique (e.g. 1 appears twice). For a set named `setname`, you can find an element `x` by doing `x in setname` so that would be O(1). If you know the index of an element in a list you can access the element in O(1) by doing list[index], but to search if an element is in a list you must traverse the whole list taking O(n) time worst case scenario. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> The lambda function allows you to create a small function, mostly as a way of filtering, sorting, or mapping. An example for `sorted` would help you specify which element you want to sort on. Suppose you have a list of tuples, `mytuples`, and want to sort on the 2nd element. You could do `sorted(mytuples, key=lambda sorter:sorter[1]` to sort on the second element.

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> A list comprehension is a one-liner way to iterate through a list and create another list. You can also filter using `if`. An example would be `squares = [x**2 for x in range(100)]`. 
>> The same example, but using `map`:
>> `nums = range(100)`
>> `squares = map(x**2, nums)`
>> As you can see, using a list comprehension is a bit nicer as it only takes one line. You do not have to create the original list first.
>> An exmaple of how to use `filter` and `lambda` to print only odd numbers: `odds = filter(lambda x: x%2, nums)`

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```
-82 days (because earlier date is date_stop)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```
7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)






import string


def two_list():
    """
    Take two lists, say for example these two:
    a =[1,1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b =[1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    and write a program that returns a list
    that contains only the elements that are common
    between the lists (without duplicates).

    """
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    return list(set(a).intersection(b))


def number_of_times(given_string):
    """
    Return the number
    of times that the letter “a” appears
    anywhere in the given string

    Given string is “I am a good developer.
    I am also a writer” and output should be 5.
    """
    given_string = 'I am a good developer. I am also a writer'
    return given_string.count('a')


def number_is_power(n):
    """
    Write a Python program to check if a given
     positive integer is a power of three
    Input : 9
    Output : True
    """
    while (n % 3 == 0):
        n /= 3
    return n == 1


def add_positive_integer(number):
    """
    Write a Python program to add
    the digits of a positive integer
    repeatedly until the result has a single digit.
    Input : 48
    Output : 3
    For example given number is 59, the result will be 5.
    Step 1: 5 + 9 = 14
    Step 1: 1 + 4 = 5

    """
    while len(str(number)) != 1:
        number = sum([int(i) for i in str(number)])
    return number


def all_zero(l):
    """
    Write a Python program to push all zeros to the end of a list.
    Input : [0,2,3,4,6,7,10]
    Output : [2, 3, 4, 6, 7, 10, 0]
    """
    i = 0
    while 0 in l:
        l.pop(0)
        i += 1
    for j in range(i):
        l.append(0)
    return l


def check_a_sequence_numbers():
    """
    Write a Python program to check a sequence of numbers is an arithmetic progression or not.
    Input : [5, 7, 9, 11]
    Output : True
    In mathematics, an arithmetic progression or arithmetic sequence is
    a sequence of numbers such that the difference between the consecutive terms is constant.
    For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with common difference of 2.

    """
    l = [5, 7, 9, 11]
    if len(l) < 2:
        return False
    diff = l[1] - l[0]
    for i in range(len(l) - 1):
        if l[i + 1] - diff != l[i]:
            return False
        return True


def find_the_number(l):
    """
     Write a Python program to find
        the number in a list that doesn't occur twice.
        Input : [5, 3, 4, 3, 4]
        Output : 5
    """
    l = [5, 3, 4, 3, 4]
    result = 0
    for i in l:
        result ^= i
    return result

def find_missing_number(num_list):
    """
    Write a Python program to find a missing number from a list.
    Input : [1,2,3,4,6,7,8]
    Output : 5
    """
    num_list = [1,2,3,4,6,7,8]
    original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
    num_list = set(num_list)
    return (list(num_list ^ set(original_list)))


def count_of_elements():
    """
    Write a Python program to count the elements in a list until an element is a tuple.
    Sample Test Cases:
    Input: [1,2,3,(1,2),3]
    Output: 3
    """
    l = [1,2,3,(1,2),3]
    number = 0
    for i in l:
        if isinstance(i, tuple):
            break
        number+=1
    return number


def some_param():
    """
    Write a program that will take the str parameter being passed and return
    the string in reversed order. For example: if the input string is "Hello World and Coders"
    then your program should return the string sredoC dna dlroW olleH.
    """
    some_s_rev = "Hello World and Coders"[::-1]
    return some_s_rev


def num_parameter(num):
    """
    Write a program that will take the num parameter being passed and return the number of
    hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    """
    hours = str(int(num/60))
    minutes = str(num % 60)
    return (hours + ':' + minutes)


def largest_word(mystring):
    """
    Write a program that will take the parameter being passed
    and return the largest word in the string. If there are
    two or more words that are the same length, return the
    first word from the string with that length. Ignore punctuation.
    Sample Test Cases:
    Input:"fun&!! time"
    Output:time
    Input:"I love dogs"
    Output:love:
    """
    mystring_new = [i.strip(string.punctuation) for i in mystring.split()]
    longest = mystring_new[0]
    for i in mystring_new:
        if len(i) > len(longest):
            longest = i
        elif len(i) == len(longest):
            continue
    return longest


def asks_the_users():
    """
    Write a program (using functions!) that asks the user
    for a long string containing multiple words. Print back
    to the user the same string, except with the words in backwards order.
    For example:
    Input: My name is Michele
    Outout: Michele is name My
    """
    s = input("Some string: ")
    return ' '.join(s.split()[::-1])

def fibonacci_number(x):
    """
    Write a program that asks the user how many Fibonnaci numbers
    to generate and then generates them. Take this opportunity to
    think about how you can use functions. Make sure to ask the
    user to enter the number of numbers in the sequence to generate.
    (Hint: The Fibonnaci seqence is a sequence of numbers where the
    next number in the sequence is the sum of the previous two numbers
    in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

    """
    x = int(input("How many fibonacci numbers would you like to generate? "))
    i = 1
    if x == 0:
        fib = []
    elif x == 1:
        fib = [1]
    elif x == 2:
        fib = [1,1]
    elif x > 2:
        fib = [1,1]
        while i < (x - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
        return fib


def some_saved_list(a):
    """
    Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
    Write one line of Python that takes this list a and makes a new list that has only
    the even elements of this list in it.
    """
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [i for i in a if i % 2 == 0]
    return b


def add_pull_off(number):
    """
    Write a program that will add up all the numbers
    from 1 to input number. For example: if the input
    is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10.
    """
    return number + add_pull_off(number - 1) if number > 1 else 1


def factorial(n):
    """
    Write a program that will take the parameter
    being passed and return the factorial of it. For example: if num = 4,
    then your program should return (4 * 3 * 2 * 1) = 24
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def modify_parameter(example):
    """
    Write a program that will take the str parameter
    being passed and modify it using the following algorithm.
    Replace every letter in the string with the letter following
    it in the alphabet (ie. cbecomes d, zbecomes a). Then capitalize
    every vowel in this new string (a, e, i, o, u) and finally return this modified string.
    Input: abcd
    Output: bcdE
    """
    letters = ['a', 'e', 'i', 'o', 'u']
    new_string = ''
    for i in example:
        if i == 'z':
            new_string += 'a'
            continue
        new_string += chr(ord(i) + 1)
    for j in new_string:
        if j in letters:
            new_string = new_string.replace(j, j.capitalize())
    return new_string


def letters_alphabetical_order(s):
    """
    Write a program that will take the str string parameter being passed
    and return the string with the letters in alphabetical order (ie. hello becomes ehllo).
    Assume numbers and punctuation symbols will not be included in the string.
    Input: edcba
    Output: abcde
    """
    return ''.join(sorted(s))


def greater(num1,num2):
    """
    Write a program that will take both parameters being passed and return the true
    if num2 is greater than num1, otherwise return the false. If the parameter
    values are equal to each other then return the string -1
    """
    if num2>num1:
        return  True
    elif num1==num2:
        return  '-1'
    else:
        return False


#   12.1
#   Create a tuple filled with 5 numbers assign it to the variable n
#   the ( ) are optional
n = 5, 7, 3, 1, 4
#   Create a tuple named tup using the tuple function
tup = tuple()
#   Create a tuple named first and pass it your first name
first = tuple('Ryan')
#   print the first letter of the first tuple by using an index
print first[0]
#   print the last two letters of the first tuple by using the
#   slice operator (remember last letters means use
#   a negative number)
print first[-2:4]
#   12.2
#   Given the following code, swap the variables then print the
#   variables
var1 = tuple("hey")
var2 = tuple("you")

var1, var2 = var2, var1

print var1
print var2

#   Split the following into month, day, year, then print the month,
#   day and year
date = 'Jan 15 2016'
month, day, year = date.split(' ')
print month
print day
print year

#   12.3
#   pass the function divmod two values and store the result in the var answer, print answer

answer = divmod(11, 3)

print answer

#   12.4
#   create a tuple t4 that has the values 7 and 5 in it, then use the scatter parameter to pass
#   t4 into divmod and print the results

t4 = 7, 5
print divmod(*t4)


#   12.5
#   zip together your first and last names and store in the variable zipped
#   print the result

f = 'Ryan'
l = 'Hanks'

zipped = zip(f, l)
print zipped

#   12.6
#   Store a list of tuples in pairs for six months and their order (name the var months):
#   [('Jan', 1), ('Feb', 2), etc

months = [('Jan', 1), ('Feb', 2), ('Mar', 3), ('Apr', 4), ('May', 5), ('Jun', 6)]

#   create a dictionary from months, name the dictionary month_dict then print it

month_dict = dict(months)

print month_dict

#   12.7
#   From your book:


def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), word))

    t.sort(reverse=True)

    res = []
    for length, word in t:
        res.append(word)
    return res
#   Create a list of words named my_words that includes at least 5 words  and test the code above
#   Print your result

my_words = ('strength', 'power', 'belief', 'movement', 'action')

print sort_by_length(my_words)

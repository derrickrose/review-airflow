# built-in function zip()
## used to combine 2 arrays so that we can iterate them together once in a raw
arr = [1, 2, 3]
arr2 = ['a', 'b', 'c']
combined2 = zip(arr, arr2)
for i in combined2:
    print(i)
## here is how it is working
combined = []
for i in range(min(len(arr), len(arr2))):
    combined.append((arr[i], arr2[i]))
print(combined)
## deep diving on zip()
## note that zip just combine the minimum number of elements betweeen the lists
arr3 = ["w", "x", "y", "z"]
combined3 = list(zip(arr, arr2, arr3))
print(combined3)

# diving deep into slicing
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = arr[1:4:]
print(arr2)
## the syntax is arr[start:end:step] same as in range
arr2 = arr[1:4:2]
print(arr2)
## absurd indexes slicing
arr2 = arr[4:1]
## will print an empty array since the start > end
print("arr2 absurd", arr2)
## reverse slicing
rev = arr[::-1]
print(rev)
## reverse slicing with step==2
rev2 = arr[::-2]
print(rev2)  # reversing the slicing since the step is negatif

# method pop of an array
arr = [1, 2, 3, 4, 5]
## pop() method will pop the last element
print(arr.pop())
print(arr)
# poping the first element
print(arr.pop(0))
print(arr)
# poping the last element by specifying the index to pop
print(arr.pop(-1))
print(arr)

# sorting an array
arr = [8, 1, 2, 9, 3, 4, 10, 5]
## sorted() will return a new
print(sorted(arr))
print(arr)
## in contrast method sort() will actually sort the current instance 
arr.sort()
print(arr)
## sorting an array with key
## key sensitive sorting
## Upper case comes first
## Bob come before adeline in default sort
arr = ["alice", "aDeline", "Bob", ]
print(sorted(arr))
print(sorted(arr, key=str.lower))  # alphabetical order ignoring case
## sort a list using a key question 30
data = [(4, 5, 6), (7, 8, 9), (1, 2, 3), ]
## return new list
print(sorted(data, key=lambda tup: tup[1]))
print(data)
## proceed the sorting here directly
data.sort(key=lambda tup: tup[1])
print(data)

# appending an array to itself will not raise an exception in python
## instead it will show an array with etc => [...]
arr = [1, 2, 3]
arr.append(arr)
print(arr)

# conditional definition of array
net_profit = [-10.5, 4.5, 30.8, -3.5, 14.0]
## using only if should be at the end of the instructions
positif_profit = [profit for profit in net_profit if profit > 0]
print(positif_profit)
## if using if-else, it should be at the beginning of the instructions
negatif_profit_rounded_to_zero = [profit if profit > 0 else 0 for profit in net_profit]
print(negatif_profit_rounded_to_zero)

# double boucle in a comprehension list
## first boucle comes first
## and the variable to return comes at the head
toto = [i for i in range(3) for j in range(3)]
## => 000111222
tata = [j for i in range(3) for j in range(3)]
## => 012012012
print(toto, tata)

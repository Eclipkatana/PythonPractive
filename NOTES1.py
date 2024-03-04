dict = {"dkm": 3, "ccc": 2}
#! zip , enumerate
inventory1= ['a', 'b', 'c', 'd']
inventory2= [1, 2, 3, 4]
for name, inventory_num in enumerate(zip(inventory1, inventory2)):
    print(name, inventory_num)

#! List comprehension
mylist = [num for num in range(1, 11) if num < 10]
mylist = [num if num < 10 else 0 for num in range(1, 11)]
chessboard_list_comprehension = [[f'{letter}{num}' for num in range(1,9)] for letter in 'ABCDEFGH'[::-1]]
#! other comprehension. They are not used as often as list comprehension
#! check this out
dict_comprehension = {letter:num for letter, num in zip('ABCDE'[::-1], range(1,6))}
print(dict_comprehension)
#%% 
set_comprehension = {x for x in 'mississippi' if x in 'm'}

tuple_comprehension = tuple(x for x in range(10) if x % 2 == 0)
generator_comprehension = (x for x in range(10) if x % 2 == 0)

combined = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]

#%% #! sorted
list_item = [('a ', 1), ('b', 7), ('c', 1), ('d', 2), ('e', 10), ('f', 9), ('g', 5), ('h', 6)]
print(list_item)
print(sorted(list_item, key=lambda x: x[0]))
#%% #! Map. Rarely used now. List compression is more readable and preferred
mylist= [1, 2, 3, 4, 5]
def square(num):
    return num**2
print(list(map(square, mylist)))
print(list(map(lambda num: num**2, mylist)))

print([num **2 for num in mylist])
#%% #! Filter. Rarely used now. list compression is more readable
mylist= [1, 2, 3, 4, 5]
def check_even(num):
    return num % 2 == 0
print(list(filter(check_even, mylist)))
print(list(filter(lambda num: num % 2 == 0, mylist)))

print([num for num in mylist if num % 2 == 0])

items =[]
items.append(1)
items.append(2)
items.append("hello")
items.append([10,20,30])

"""for item in items:
    print(item, type(item))"""
    
"""for i in range(0, len(items)):
    print(i, items[i])"""
    
"""for i, item in enumerate(items):
    print(i, item)"""
    
li2 = [4,5,6,7]

#items = items+li2
#items.extend(li2)
#items.append(li2)
# print(items)

"""for index, x in enumerate(items):
    print(index, x, items[index])"""
    
items  = [1,2,3]
"""another_list = [4,5,6]

items.append(another_list)
print(items)
print("The list has {} items.".format(len(items)))
print(items[3][0])
"""
#print(dir(items))

"""This command the python shell"""
# help(list.pop) 


#print(help(list.sort))

items = (2,2,3,4)
# print(items, type(items))
# print(dir(items))

# print(items.index(2))

a = 10
b = 5 

# t = b
# b = a
# a = t

# a,b = b,a

t = (a,b)
c,d = t
# print(a,b,c,d)
""" SET """
s = {1,2,3}
s.add(4)
s.add(4)
s.add(5)
s.add(5)
# print(s, type(s))
# print(dir(s))
li  = [1,2,3,3,3,4,4]
# s = set(li) 
# li = list(s)
li = list(set(li))
# print(li, type(li))


s = {1,3,4,5}

# print(2 in s)
# print(3 in s)

# print(s[0])

# print(dir(set))

"""dictionary"""
text = "The cheerfull robin, wtih its bright red breast, perched on the emerald green windowsill. Beside it, a vibrant yellow sunflower swayed gently in the summer breeze. A cloud, cotton-white and fluffy, drifted across teh azure blue sky, casting a berif lavendar shadow on the blooming purple crocuses below red green blue"

colors = ['red', 'green', 'yellow', 'white', 'blue', 'purple', 'black']

# li = set()

# word_list = text.split()

# for word in word_list:
#     if word in colors:
#         li.add(word)
        
# print(li)

# dt = {}

# word_list = text.split()
# for word in word_list:
#     if word in colors:
#         if word not in dt.keys():
#             dt[word] = 1
#         else:
#             dt[word] += 1 
        
# print(dt)


dt = { 1:"one", 2:"two", 3:"three"}

# print(dt.keys())
# print(dt.values())

# for k,v in dt.items():
#     print(k,v)

# for t in dt.items():
#     print(t, type(t))

dt = {"one": 1, "two": 2, "three": 3}
print(dt["three"])
#字典dict是python的唯一一个映射类型
#映射是指，两个元素集之间相互对应的关系
brand = ['LiNing', 'nike', 'Adidas']
slogen = ['一切皆有可能', 'Just do it', 'Impossible is nothing']

#用index()方法也可以，但是不够简洁：
#print("Slogen of Adidas is:", slogen[brand.index('Adidas')])
#字典可以用映射的方式把元素连接起来
#字典不是序列类型，是映射类型
dict1 = {'LiNing': '一切皆有可能', 'nike': 'Just do it', 'Adidas': 'Impossible is nothing'}
#通过键，查找值:
print("Slogen of Adidas is:", dict1['Adidas']) 
#也可以用value反向读取键：
get_value = input('please input the value for searching the key:')
if get_value in dict1.values():
# mydisc.keys()：取出字典mydisc的所有key
# list(list)：将list转化为列表，列表的好处就是有序，所以能通过list[index]取元素
#list.index(x)：返回元素x在list中的索引（如果list中存在多个重复的x，会返回首次出现的索引）
#list[x]：取list中第x个元素的值
    print('The key of the value is:', list(dict1.keys())[list(dict1.values()).index(get_value)])
else:
    print('Sorry, '+get_value+'is not exist.')

#还可以用元组/列表：
dict2 = dict((('h', 72), ('e', 69), ('l', 76), ('l', 76), ('o', 79)))
print(dict2)
#运行结果会把元组里重复的元素忽略掉：{'h': 72, 'e': 69, 'l': 76, 'o': 79} 

#字典的fromkeys()方法可以返回具有指定键和值的字典
#我的理解是：fromkeys()的作用是创建新字典
dict2 = {}
dict2ForShow = dict2.fromkeys((1, 2, 3), '阳光彩虹小白马')
print(dict2ForShow)
#运行结果：{1: '阳光彩虹小白马', 2: '阳光彩虹小白马', 3: '阳光彩虹小白马'}

#keys():读取数组中的键的数据
#value():读取数组中的键所映射的值
#items():读取数组中的所有元素内容（）
dict3 = {}
dict3ForShow = dict3.fromkeys(range(32), '赞')
print(dict3ForShow)
for eachKey in dict3ForShow.keys():
    print(eachKey)
for eachValue in dict3ForShow.values():
    print(eachValue)
for eachItem in dict3ForShow.items():
    print(eachItem)

#以列表的形式返回所有的元素
print(list(dict3ForShow.items()))


#假如有一个字符串列表，我想要将每一个元素都转换成大写字母

"""

#可以用传统for循环来做
#使用 .upper()方法 和 .append()方法

directions = ["north", "east", "south", "west"]
#建立一个新数组
#然后再用append()方法追加数组元素到这个数组
directions_upper = [] 

for direction in directions:
    turnedUP = direction.upper()
    directions_upper.append(turnedUP)

print(directions_upper)
#['NORTH', 'EAST', 'SOUTH', 'WEST']

"""
#但是用 map() 函数更方便
def to_upper_case(needUpWord):
    return needUpWord.upper()

directions = ["north", "east", "south", "west"]
directions_upper = map(to_upper_case, directions)
print(list(directions_upper))
#['NORTH', 'EAST', 'SOUTH', 'WEST']



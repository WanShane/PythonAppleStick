#把年龄和城市设为默认参数
#这样大多数的学生注册时不需要提供年龄和城市，只提供必须的两个参数
#e.g.: enroll('Alax', 'male')
#输出结果就会自动添加上默认的age：29，city：Dongying

def enroll(name, gender, age = 29, city = 'Dongying'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#只有与默认参数不符的学生才需要提供额外的信息
#e.g.: enroll('Adam', 'M', city='Tianjin')
enroll('wan', 'female')
enroll('Alax', 'male',city='New York')
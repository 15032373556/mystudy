def show_magicians(names):
    """打印每个魔术师的名字"""
    for name in names:
        print(name)

def make_great(names,names_1):
    """在每个魔术师名字中加入the Great 字样"""
    while names:
        current_name = names.pop()
        name = "the Great " + current_name
        names_1.append(name)

magician_names = ['A','B','C']
magician_names_1 =[]
make_great(magician_names[:],magician_names_1)
print("打印原始列表：")
show_magicians(magician_names)
print("\n打印改过的列表：")
show_magicians(magician_names_1)
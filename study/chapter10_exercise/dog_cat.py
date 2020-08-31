def print_file(filename):
    """打印文件中的内容"""
    try:
        with open(filename,encoding='utf-8') as fo:
            content = fo.read()
    except FileNotFoundError:
        # print("sorry,the file " + filename + " does not exist.")
        pass
    else:
        print(content)

filenames = ['cats.txt','dogs.txt','pigs.txt']
for filename in filenames:
    print_file(filename)

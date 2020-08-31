def make_album(singer_name,album_name,number_song=''):
    """制作专辑"""
    if number_song:
        album = {'singer': singer_name, 'album': album_name,'number':number_song}
    else:
        album = {'singer':singer_name,'album':album_name}
    return album

while True:
    print("Enter 'q' at any time to exit.")
    singer_name = input("请输入歌手的名字： ")
    if singer_name == 'q':
        break
    album_name = input("请输入专辑的名字: ")
    if album_name == 'q':
        break
    number_song = input("请输入专辑中歌曲的数量: ")
    if number_song == 'q':
        break
    album = make_album(singer_name,album_name,number_song)
    print(album)

# album_1 = make_album('黑豹乐队','黑豹')
# print(album_1)
# album_2 = make_album('李宇春','Chris Lee')
# print(album_2)
# album_3 = make_album('薛之谦','初学者',6)
# print(album_3)
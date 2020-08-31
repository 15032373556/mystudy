#使用任意数量的关键字实参
def build_profile(first,last,**user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['firstname'] = first
    profile['lastname'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

# user_profile = build_profile('刘','小小',location='China',field='physics')
# print(user_profile)

user_profile = build_profile('Li','Jingyan',location='China',field='math',sexual='woman')
print(user_profile)
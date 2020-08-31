class User():
    """一次模拟用户的简单尝试"""

    def __init__(self,first_name,last_name,login_attempts,**user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        self.user_info = user_info

    def describe_user(self):
        """打印用户信息摘要"""
        user = {}
        user['first name'] = self.first_name
        user['last name'] = self.last_name
        user['login_attempts'] = self.login_attempts
        for key,value in self.user_info.items():
            user[key] = value
        print(user)

    def greet_user(self):
        """向用户发出个性化的问候"""
        user_full_name = self.first_name + ' ' + self.last_name
        print(user_full_name.title() + ",thank you for your visit.")

    def increment_login_attempts(self,increment_number=1):
        """将属性login_attempts的值 + 1"""
        self.login_attempts += increment_number
        return self.login_attempts

    def reset_login_attempts(self):
        """将属性login_attempts的值重置为0"""
        self.login_attempts = 0
        return self.login_attempts


class Privileges():
    """管理员权限"""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """显示管理员的权限"""
        print("Administrator privileges are as follows: ")
        for privilege in self.privileges:
            print("--" + privilege)


class Admin(User):
    """管理员信息管理"""

    def __init__(self,first_name,last_name,login_attempts,**user_info):
        """管理员"""
        super().__init__(first_name,last_name,login_attempts,**user_info)
        self.privileges = Privileges()


# admin = Admin('aaa','back',3)
# admin.privileges.show_privileges()






# user = User('jack','queen',2)
# u = user.increment_login_attempts()
# print(u)
# u = user.increment_login_attempts()
# print(u)
# u = user.increment_login_attempts()
# print(u)
# re = user.reset_login_attempts()
# print(re)


# user_1 = User('jack','queen')
# user_1.describe_user()
# user_1.greet_user()
#
# user_2 = User('hannah','margot',location='china')
# user_2.describe_user()
# user_2.greet_user()
#
# user_3 = User('zhu','ming',location='china',favorite_number=9)
# user_3.describe_user()
# user_3.greet_user()
from user import User

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

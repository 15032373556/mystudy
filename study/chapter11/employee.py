class Employee():
    """一个表示雇员的类"""
    def __init__(self,first_name,last_name,annual_salary):
        """初始化雇员"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self,raise_salary=5000):
        """增加年薪，默认增加5000美元"""
        self.annual_salary += raise_salary
        return self.annual_salary

    # def show_info(self):
    #     msg = self.first_name.title() + ' ' + self.last_name.title() + ',annual salary - ' + str(self.annual_salary)
    #     return msg

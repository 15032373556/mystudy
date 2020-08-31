import unittest

import study.data_visual.chapter17.python_repos_x as pr

class PythonRepoTestCase(unittest.TestCase):
    """测试python_repos_x.py"""

    def SetUp(self):
        """调用所有的函数，并分别测试各个方面"""
        self.r = pr.get_response()
        self.repo_dicts = pr.get_repo_dicts(self.r)
        self.repo_dict = self.repo_dicts[0]
        self.names,self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)

    def test_get_response(self):
        """测试获得了有效的响应"""
        self.assertEqual(self.r.status_code,200)

    def test_repo_dicts(self):
        """测试获得了期望的数据"""
        # 应获得30个描述仓库的字典
        self.assertEqual(len(self.repo_dicts),30)
        # 描述仓库的字典应包含必要的键
        required_keys = ['name', 'owner', 'stargazers_count', 'html_url']
        for key in required_keys:
            self.assertTrue(key in self.repo_dict.keys())

unittest.main()

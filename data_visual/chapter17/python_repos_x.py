import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS

def get_response():
    """执行API调用并返回响应"""
    url = 'https://api.github.com/search/repositories?q=language:c&sort=stars'
    r = requests.get(url)
    return r

def get_repo_dicts(r):
    """返回一系列表示最受欢迎仓库的字典"""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_names_plot_dicts(repo_dicts):
    """处理这些表示仓库的字典，从中提取用于绘制图形的数据"""
    names, plot_dicts = [], []
    for repo_dict in repo_dicts:
        names.append(repo_dict['name'])
        # 项目被删除后，它依然会被列出并有星级，但没有描述。
        #   将描述用作标签时，如果它为None，将引发异常。
        desc = repo_dict['description']
        if not desc:
            desc= 'No description provided'
        plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': str(repo_dict['description']),
            'xlink': repo_dict['html_url'],
        }
        plot_dicts.append(plot_dict)
    return names,plot_dicts

def make_visualization(names,plot_dicts):
    """可视化最受欢迎的项目"""
    my_style = LS('#333366', base_style=LCS)

    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 20
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000

    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred C Projects on GitHub'
    chart.x_labels = names

    chart.add('', plot_dicts)
    chart.render_to_file('c_repos.svg')

r = get_response()
repo_dicts = get_repo_dicts(r)
names, plot_dicts = get_names_plot_dicts(repo_dicts)
make_visualization(names, plot_dicts)






# numpy 的使用
'''
import numpy as np
data1 = [1,2,3,4]
data2 = [5,6,7,8]
data = [data1,data2]
arr = np.array(data)
print(arr)
print(arr.dtype)
print(np.zeros((2,3)))
print(np.ones((3,4)))
print(np.arange(1,10,2))
print(np.linspace(1,10,4))
arr2 = np.array([1.1,2,3,4])
print(arr2.dtype)
arr3 = np.array(['量','化','分','析'])
print(arr3.dtype)
float_arr = arr.astype(np.float64)
print(float_arr)
int_arr2 = arr2.astype(np.int32)
print(int_arr2)
u_arr3 = arr3.astype(np.unicode_)
print(u_arr3)

# 数组索引，切片，赋值
arr4 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr4)
print(arr4[1])
print(arr4[1,2])
print(arr4[:2,:2])
arr4[:2,:2] = 10
# arr4[:2,:2] = [[10,1],[2,4]]
arr4.copy()[:2,:2] = 5
print(arr4)

# 基本的数组运算
arr5 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr5)
print(arr5 + arr5)
print(arr5 * 2)
print(arr5 * arr5)
print(arr5 ** 0.5)
print(arr5.sum())
print(arr5.max())
print(arr5.min())
print(arr5.mean())
print(arr5.std())
print(np.array([[3,7],[3,7]]).std())

# 随机数
import numpy.random as npr
import matplotlib.pyplot as plt
print(npr.rand(3,2))
print(npr.rand(3,2) * 2 + 2)
print(npr.random(10))
print(npr.randn(10))
print(npr.randint(1,10,5))
print(npr.choice([3,22,56,7,90],3))
print(npr.binomial(100, 0.3, 10))
print(npr.normal(10, 20, 10))
print(npr.chisquare(0.5, 10))
print(npr.poisson(2.0, 10))
'''

# pandas 的使用
'''
import pandas as pd
# Series
obj = pd.Series([40,12,-3,25])
print(obj)
print(obj[0])
print(obj.index)
print(obj.values)
obj = pd.Series([40,12,-3,25],index = ['a','b','c','d'])
print(obj)
print(obj['b'])
print(obj[obj > 15])
print(obj.describe())
print(obj.to_dict())

# DataFrame
d = {'one':pd.Series([1,2,3,4],index=['a','b','c','d']),'two':pd.Series([3,4,5],index=['a','b','c'])}
df = pd.DataFrame(d)
print(df)
# 设置输出格式
pd.set_option("display.max_rows",3)
pd.set_option("display.max_columns",1)
pd.set_option("precision",1)   # 精度
# pd.set_option('large_repr', 'truncate')  # 截断
print(df)

# 数据读取与写入
a = pd.read_csv(r'C:\\Users\刘邦国\Desktop/closeprice.csv',dtype={'ticker':str},encoding='gbk')
print(a)
# a.to_excel('closeprice.xlsx')
print(a.describe())
print(a.info())
a = pd.read_csv(r'C:\\Users\刘邦国\Desktop/closeprice.csv',encoding='gbk')
print(a)
b={1:'银行',2:'房地产',4:'医药生物',5:'房地产',6:'采掘',7:'休闲服务',8:'机械设备'}
a['field'] = a.ticker.map(b)
print(a)

# DataFrame按多列排序
data = pd.DataFrame({'group':['1','1','1','2','2','2','3','3','3',],'ounces':[4,3,12,6,7.5,8,3,5,6]})
data.sort_values(by=['group','ounces'],ascending=[False,True],inplace=True) # 先按group降序排列,当group相同时再按ounces升序排列
print(data)

data = pd.DataFrame({'k1':['one'] * 3 + ['two'] * 4,'k2':[3,2,1,3,3,4,4]})
print(data)
print(data.drop_duplicates())  # 完全相同的行去重
print(data.drop_duplicates(subset=['k1'],keep='last')) # subset=k1,只要k1重复,Pandas就认为是重复的,通过 keep参数确定需要保留哪个，一般在使用keep时先排序
print(data[data.duplicated()])  # 查看重复的行

a = pd.read_csv(r'C:\\Users\刘邦国\Desktop/closeprice.csv',encoding='gbk')
# print(a)
print(a.drop(['Unnamed: 0'],axis=1))
print(a.drop(['Unnamed: 0'],axis='columns'))

# 替换数据
import numpy as np
a = pd.read_csv(r'C:\\Users\刘邦国\Desktop/closeprice.csv',encoding='gbk')
print(a)
print(a.replace(1,np.nan))  #  批量替换数据中的指定数值
print(a.rename(columns={'Unnamed: 0':'id'}))   # 重命名某些列

# 切片与筛选
print(a.loc[:,['ticker','closePrice']])
print(a.iloc[:4,[1,4]])
print(a.iloc[1:2,5:6])
print(a[a.closePrice > 10])
print(a[(a.closePrice > 10) & (a.ticker > 3)])
print(a[(a.closePrice>10)*1 + (a.ticker>3)*1==2])

bins = [4,9,10,20,30]
cat = pd.cut(a.closePrice,bins)
print(cat)
print(pd.value_counts(cat))
group_names = ['low','middle_1','middle_2','high']
print(pd.cut(a.closePrice,bins,labels=group_names))
'''

# Scipy 的初步使用
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
data  = pd.read_csv('data.csv',index_col='Date')
data.index = [dt.datetime.strptime(x,'%Y-%m-%d') for x in data.index]
print(data.head())
'''

# seaborn调色盘
'''
# 调色盘---------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

current_palette = sns.color_palette()
sns.palplot(current_palette)
sns.palplot(sns.color_palette('Accent',8)) # 颜色风格为Accent，颜色色块个数为8个
sns.palplot(sns.color_palette('Paired',16))

sns.palplot(sns.hls_palette(8,l=0.8,s=0.5))  # 设置亮度(l)、饱和度(s)

# 按照线性增长计算，设置颜色
# n_colors 颜色个数,start 值区间在0-3，开始颜色，rot 颜色旋转角度，gamma 颜色伽马值，越大颜色越暗，
# dark,light 值区间0-1，颜色越深，reverse 布尔值，默认为false,由浅到深
sns.palplot(sns.cubehelix_palette(8,gamma=2))
sns.palplot(sns.cubehelix_palette(8,start=0.5,rot=-0.75))
sns.palplot(sns.cubehelix_palette(8,start=2,rot=0,dark=0,light=0.95,reverse=True))

# 颜色深浅
sns.palplot(sns.light_palette('green')) # 按照green做浅色调色盘
sns.palplot(sns.dark_palette('red',reverse=False)) # 按照red做深色调色盘

# 创建分散颜色
# h_neg, h_pos-起始/终止颜色值，s-值区间0-100，饱和度，l-值区间0-100，亮度
# n-颜色个数，center-中心颜色为浅色还是深色'light', 'dark', 默认为light
pallete = sns.diverging_palette(h_neg=145,h_pos=280,s=75,l=50,sep=10,n=6,center='light',as_cmap=False)
sns.palplot(pallete)
# 用分散颜色制作热力图
plt.figure(figsize=(8,6))
x = np.arange(24).reshape(4,6)
cmap = sns.diverging_palette(200,20,sep=20,as_cmap=True)
sns.heatmap(x,cmap=cmap) 
plt.show()
'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as sci
# 设置风格、尺寸
# sns.set_style('darkgrid')
# sns.set_style('whitegrid')
sns.set_style('ticks')
sns.set_context('paper')
# 不发出警告
import warnings
warnings.filterwarnings('ignore')

# 分布数据可视化--------------------
# 直方图 distplot()----
'''
# 直方图1--------------------------
rs = np.random.RandomState(10) # 设定随机数种子
s = pd.Series(rs.randn(100) * 100)
sns.distplot(s,bins=10,hist=True,kde=True,norm_hist=False,
             rug=True,vertical=False,
             color='b',label='distplot',axlabel='x')
plt.legend() # 创建图例
plt.show()   

# 直方图2-------------------------- 
sns.distplot(s,rug=True,# rug 是否显示数据分布情况
             rug_kws={'color':'y'}, # 设置数据频率分布颜色
             kde_kws={'color':'k','lw':1,'label':'KDE','linestyle':'--'},
             # 设置密度曲线颜色、线宽、标注、 线形
             hist_kws={'histtype':'stepfilled','linewidth':1,'alpha':1,'color':'g'}
             # 设置箱子的风格、线宽、透明度、颜色
             )  
plt.legend()
plt.show()
'''

# 密度图 kdeplot()----
'''
# 单个样本数据密度分布图------------------
sns.kdeplot(s,shade=False,# 是否填充
            color='r', # 设置颜色
            vertical=False) # 设置是否水平
# bw --> 控制拟合的程度，类似直方图的箱数
sns.kdeplot(s,bw=1,label='bw:0.2',linestyle='--',linewidth=1.2,alpha=0.5)
sns.kdeplot(s,bw=20,label='bw:2',linestyle='--',linewidth=1.2,alpha=0.5)
# 数据频率分布,函数rugplot()显示数据分布情况
sns.rugplot(s,height=0.1,color='g',alpha=0.5)
plt.show()

# 两个样本数据密度分布图------------------
rs = np.random.RandomState(2)
df = pd.DataFrame(rs.randn(100,2),
                  columns=['A','B'])
# 两个维度数据生成曲线密度图，以颜色作为密度的衰减显示
sns.kdeplot(df['A'],df['B'],
            cbar=True,             # 是否显示颜色的图例
            shade=True,            # 是否填充
            cmap='Reds',           # 设置调色盘
            shade_lowest=False,    # 最外围颜色是否显示
            n_levels=50            # 曲线个数(如果非常多，则会越平滑)
            )
# 注意设置x,y轴
plt.scatter(df['A'],df['B'],s=5,alpha=0.5,color='k')
sns.rugplot(df['A'],color='g',axis='x',alpha=0.5)
sns.rugplot(df['B'],color='r',axis='y',alpha=0.5)
plt.show()

# 多个样本数据密度分布图------------------
rs1 = np.random.RandomState(2)
rs2 = np.random.RandomState(5)
df1 = pd.DataFrame(rs1.randn(100,2) + 2,columns=['A','B'])
df2 = pd.DataFrame(rs2.randn(100,2) - 2,columns=['A','B'])
# 创建图表
sns.kdeplot(df1['A'],df1['B'],cmap='Greens',shade=True,shade_lowest=False)
sns.kdeplot(df2['A'],df2['B'],cmap='Blues',shade=True,shade_lowest=False)
plt.show()
'''

# 散点图----
# 综合散点图 - jointplot()
'''
----------------# 散点图+分布图--------------
rs = np.random.RandomState(2)
df = pd.DataFrame(rs.randn(100,2),columns=['A','B'])
sns.jointplot(x=df['A'],y=df['B'],   # 设置xy轴，显示columns名称
              data=df,   # 设置数据
              color='b',  # 设置颜色
              s=50,edgecolor='w',linewidth=1,  # 设置散点大小、边缘颜色及宽度(只针对scatter)
              stat_func=sci.pearsonr,
              kind='scatter',  # 设置类型：'scatter','reg','resid','kde','hex'
              # stat_func=<function pearsonr>,
              space=0.1,  # 设置散点图和布局图的间距
              size=8,  # 图表大小(自动调整为正方形))
              ratio=5,  # 散点图与布局图高度比，整型
              marginal_kws=dict(bins=15,rug=True),  # 设置柱状图箱数，是否设置rug
              )
plt.show()
# 六边形图---------
sns.jointplot(x=df['A'],y=df['B'],   # 设置xy轴，显示columns名称
              data=df,   # 设置数据
              color='b',  # 设置颜色
              stat_func=sci.pearsonr,
              kind='hex',  # 设置类型：'scatter','reg','resid','kde','hex'
              space=0.1,  # 设置散点图和布局图的间距
              size=8,  # 图表大小(自动调整为正方形))
              ratio=5,  # 散点图与布局图高度比，整型
              # marginal_kws=dict(bins=15,rug=True),  # 设置柱状图箱数，是否设置rug
              )
plt.show()
# 六边形图---------
df = pd.DataFrame(rs.randn(500,2),columns=['A','B'])
with sns.axes_style('white'):
    sns.jointplot(x=df['A'],y=df['B'],data=df,color='k',
                  stat_func=sci.pearsonr,kind='hex',
                  marginal_kws=dict(bins=20),
                  )
plt.show()
# 密度图------------
rs = np.random.RandomState(2)
df = pd.DataFrame(rs.randn(100,2),columns=['A','B'])
g = sns.jointplot(x=df['A'],y=df['B'],data=df,color='k',
                  stat_func=sci.pearsonr,kind='kde',
                  shade_lowest=False)   # 创建密度图
g.plot_joint(plt.scatter,c='w',s=30,linewidth=1,marker='+')  # 添加散点图
plt.show()

---------------# 可拆分绘制的散点图-------------
# plot_joint() + ax_marg_x.hist() + ax_marg_y.hist()
# 拆分图-------------
# 设置风格
sns.set_style('white')
# 导入数据
# tips = sns.load_dataset('tips.csv')  # 一直出错，没找到原因
tips = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\tips.csv')
print(tips.head())
# 创建一个绘图表格区域，设置好x,y对应数据
g = sns.JointGrid(x='total_bill',y='tip',data=tips)
g.plot_joint(plt.scatter,color='m',edgecolor='white')  # 设置框内图表，scatter
g.ax_marg_x.hist(tips['total_bill'],color='b',alpha=0.6,
                 bins=np.arange(0,60,3))  # 设置x轴为直方图，注意bins是数组
g.ax_marg_y.hist(tips['tip'],color='r',alpha=0.6,orientation='horizontal',
                 bins=np.arange(0,12,1))  # 设置y轴直方图，注意需要orientation参数
from scipy import stats
g.annotate(stats.pearsonr)
#设置标注，可以为pearsonar， spearmanr
plt.grid(linestyle='--')
plt.show()

# 两个条形图在一个函数里进行设置----------
# 创建一个绘图表格区域，设置好x,y对应数据
g = sns.JointGrid(x='total_bill',y='tip',data=tips)
g = g.plot_joint(plt.scatter,color='g',s=40,edgecolor='white')   # 绘制散点图
plt.grid(linestyle='--')
g.plot_marginals(sns.distplot,kde=True,color='g')  # 绘制x，y直方图
plt.show()

# kde - 密度图----------
# 创建一个绘图表格区域，设置好x,y对应数据
g = sns.JointGrid(x='total_bill',y='tip',data=tips)
g = g.plot_joint(sns.kdeplot,cmap='Reds_r')  # 绘制密度图
plt.grid(linestyle='--')
g.plot_marginals(sns.kdeplot,shade=True,color='r')  # 绘制x,y轴密度图
plt.show()
'''
# 矩阵散点图 - pairplot()
'''
# 普通矩阵图示意-------
sns.set_style('white')
iris = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\iris.csv')
sns.pairplot(iris,
             kind='scatter',  # 散点图/回归分布图{'scatter', 'reg'})
             diag_kind='hist',  # 直方图/密度图{'hist'， 'kde'}
             hue='species',  # 按照某一字段进行分类
             palette='husl',  # 设置调色板
             markers=['o','s','D'],  # 设置不同系列的点样式（这里根据参考分类个数）
             size=2  # 图标大小
             )
plt.show()

# 只提取局部变量进行对比----------
sns.pairplot(iris,vars=['sepal_width','sepal_length'],kind='reg',diag_kind='kde',hue='species',palette='husl',)
plt.show()

# 其它参数设置-------------
sns.pairplot(iris, diag_kind='kde', markers='+',
             plot_kws=dict(s=50, edgecolor='b', linewidth=1),  # 设置点样式
             diag_kws=dict(shade=True))  # 设置密度图样式
plt.show()

# 可拆分绘制的散点图-------------
# map_diag() + map_offdiag()
# 可筛选创建一个绘图表格区域，设置好x，y对应的数据，按照species分类
g = sns.PairGrid(iris, hue='species', palette='hls',
                 vars=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
# 对角线图表，plt.hist/sns.kdeplot
g.map_diag(plt.hist,
           histtype='step',  # 可选：'bar','barstacked', 'step', 'stepfilled'
           linewidth=1, edgecolor='w')
# 其它图表：plt.scatter/plt.bar...
g.map_offdiag(plt.scatter, edgecolor='w', s=40, linewidth=1)  # 设置点颜色、大小、描边宽度
g.add_legend()  # 添加图例()
plt.show()

# 上三角和下三角------------------
# map_diag() + map_lower() + map_upper()
g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot,lw=3)  # 设置对角线图表
g.map_upper(plt.scatter,color='r')  # 设置对角线上端图表
g.map_lower(sns.kdeplot,cmap='Blues_d')  # 设置对角线下端图表
plt.show()
'''
# 分类散点图 - stripplot()/swarmplot()
'''
# 按照不同类别对样本数据进行分布散点图绘制 - stripplot()------
tips = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\tips.csv')
print(tips.head())
# hue----------------
sns.stripplot(x='day',    # 设计分组统计字段
              y='total_bill',  # 数据分布统计字段
              # 这里xy数据对调，会使得散点图横向分布
              data=tips,  # 对应数据
              jitter=True,  # 当数据重合较多时，用该参数做一些调整，也可以设置间距如，jitter=0.1
              size=5,edgecolor='w',linewidth=1,marker='o'
              )
# 通过hue参数再分类
sns.stripplot(x='sex',y='total_bill',hue='day',data=tips,jitter=True)
plt.show()
# 设置调色盘-----------------
sns.stripplot(x='sex',y='total_bill',hue='day',
              data=tips,jitter=True,
              palette='Set2',  # 设置调色盘
              dodge=True)
plt.show()
# 用order参数进行筛选分类类别-------------
print(tips['day'].value_counts())  # 查看day字段的唯一值
sns.stripplot(x='day',y='total_bill',data=tips,jitter=True,
              order=['Sat','Sun'])  # order筛选类别
plt.show()

# 分簇散点图 - swarmplot()---------------------------------
# 用法和stripplot类似
sns.swarmplot(x='day',y='total_bill',data=tips,
              size=5,edgecolor='w',linewidth=1,marker='o',
              palette='Reds')
plt.show()
'''

# 分布图----
# 箱型图 - boxplot()
'''
tips = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\tips.csv')
sns.boxplot(x='day',y='total_bill',data=tips,
            linewidth=2,  # 线宽
            width=0.8,  # 箱之间的间隔比例
            fliersize=3,  # 异常点大小
            palette='hls',  # 设置调色板
            whis=1.5,  # 设置IQR
            notch=True,  # 设置是否以中值做凹槽
            order={'Thur','Fri','Sat','Sun'},  # 筛选类别
            )
# 可以添加散点图
sns.swarmplot(x='day',y='total_bill',data=tips,color='k',size=3,alpha=0.8)
plt.show()
# 通过参数再分类
sns.boxplot(x='day',y='total_bill',data=tips,hue='smoker',palette='Reds')
plt.show()
'''
# 小提琴图 - violinplot()
'''
tips = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\tips.csv')
sns.violinplot(x='day',y='total_bill',data=tips,
               linewidth=2,  # 线宽
               width=0.8,  # 箱之间的间隔比例
               palette='hls',  # 设置调色板
               order={'Thur','Fri','Sat','Sun'},  # 筛选类别
               scale='count',  # 测度小提琴图的宽度:area-面积相同,count-按照样本数量决定宽度,width-宽度一样
               gridsize=50,  # 设置小提琴图的平滑度,越高越平滑
               inner='box',  # 设置内部显示类型 --> 'box','quartile','point','stick',None
               # bw = 0.8      #控制拟合程度，一般可以不设置
               )
plt.show()
# 通过hue再分类
sns.violinplot(x='day',y='total_bill',data=tips,
               hue='smoker',palette='muted',
               split=True,  # 设置是否拆分小提琴图
               inner='quartile')
plt.show()
# 结合散点图
sns.violinplot(x='day',y='total_bill',data=tips,palette='muted',inner=None)
sns.swarmplot(x='day',y='total_bill',data=tips,color='w',alpha=0.5)
plt.show()
'''
# LV图表 - lvplot()
'''
tips = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\tips.csv')
# 绘制LV图
sns.lvplot(x='day',y='total_bill',data=tips,palette='mako',
           # hue='smoker',
           width=0.8,  # 箱之间的间隔比例
           linewidth=12,
           scale='area',  # 设置框的大小 --> 'linear'、'exonential'、'area'
           k_depth='proportion'  # 设置框的数量 --> 'proportion','tukey','trustworthy'
           )
# 可以添加散点图
sns.swarmplot(x='day',y='total_bill',data=tips,color='k',size=3,alpha=0.8)
plt.show()
'''

# 统计图----
# 柱状图(置信区间估计) - barplot()
'''
# 置信区间：样本均值 + 抽样误差
sns.set_context('paper')
# 示例1-------------
titanic = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\titanic.csv')
print(titanic.head())
sns.barplot(x='sex',y='survived',hue='class',data=titanic,
            palette='hls',
            order=['male','female'],  # 筛选类别
            capsize=0.05,  # 误差线横向延申宽度
            saturation=8,  # 颜色饱和度
            errcolor='gray',errwidth=2,  # 误差线颜色、宽度
            ci='sd'  # 置信区间误差 --> 0-100内值、 'sd' 、None
            )
plt.show()
# 计算数据
print(titanic.groupby(['sex','class']).mean()['survived'])
print(titanic.groupby(['sex','class']).std()['survived'])
# 示例2--------------
tips = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\tips.csv')
sns.barplot(x='day',y='total_bill',hue='sex',data=tips,
            palette='Blues',edgecolor='w')
plt.show()
print(tips.groupby(['day','sex']).mean())
# 示例3----------------
crashes = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\car_crashes.csv')\
    .sort_values('total',ascending=False)
f,ax = plt.subplots(figsize=(6,15))  # 创建图表
sns.set_color_codes('pastel')  # 设置第一个柱状图
sns.barplot(x='total',y='abbrev',data=crashes,
            label='Total',color='b',edgecolor='w')
sns.set_color_codes('muted')  # 设置第二个柱状图
sns.barplot(x='alcohol',y='abbrev',data=crashes,
            label='Alcohol-involve',color='b',edgecolor='w')
ax.legend(ncol=2,loc='lower right')
sns.despine(left=True,bottom=True)
plt.show()
'''
# 计数柱状图 - countplot()
'''
# x/y --> 以x或者y轴绘图（横向，竖向）
# 用法和barplot相似
titanic = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\titanic.csv',error_bad_lines=False)# error_bad_lines=False
print(titanic.head())
sns.countplot(x='class',hue='who',data=titanic,palette='magma')
plt.show()
'''
# 折线图(置信区间估计) - pointplot()
'''
tips = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\tips.csv')
sns.pointplot(x='time',y='total_bill',hue='smoker',data=tips,
              palette='hls',
              dodge=True,  # 设置点是否分开
              join=True,  # 是否连线
              markers=['o','x'],linestyles=['-','--']  # 设置点样式、线型
              )
plt.show()
print(tips.groupby(['time','smoker']).mean()['total_bill'])
'''

# 线性关系数据可视化-lmplot()------------------
'''
tips = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\tips.csv')
sns.lmplot(x='total_bill',y='tip',hue='smoker',data=tips,
           palette='Set1',
           ci=70,  # 误差值
           size=5,  # 图表大小
           markers=['+','o']  # 点样式
           )
plt.show()
# 拆分多个表格------
sns.lmplot(x='total_bill',y='tip',data=tips,col='smoker')
plt.show()
# 多图表1---------
sns.lmplot(x='size',y='total_bill',hue='day',col='day',data=tips,
           # aspect=0.6,  # 长宽比
           # x_jitter=0.3,  # 给x或者y轴随机增加噪音点
           col_wrap=2  # 每行的列数
           )
plt.show()
# 多图表2---------
sns.lmplot(x='total_bill',y='tip',row='sex',col='time',data=tips,size=4)
plt.show()
# 非线性回归------
sns.lmplot(x='total_bill',y='tip',data=tips,order=4)  # order是幂数
plt.show()
'''

# 时间线图表 - tsplot()
'''
x = np.linspace(0,15,31)
# print(x)
data = np.sin(x) + np.random.rand(10,31) + np.random.randn(10,1)
# print(data)
print(data.shape)
print(pd.DataFrame(data).head())   # 10rows,31cols
# 示例1：
sns.tsplot(data=data,
           err_style='ci_band',  # 误差数据风格，可选：ci_band, ci_bars, boot_traces,
           # boot_kde, unit_traces, unit_points
           interpolate=True,  # 设置连线
           ci=[40,70,90],  # 设置误差区间
           color='g',  # 设置颜色
           )
plt.show()
# 示例2：
sns.tsplot(data = data, err_style = 'boot_traces',
           n_boot = 300   #迭代次数
           )
plt.show()
# 示例3：
# 参数设置
# 导入数据
gammas = sns.load_dataset('gammas')
print(gammas.head())
print('数据量为：%i条' % len(gammas))
print('timepoint为0.0时的数据量为：%i条' % len(gammas[gammas['timepoint'] == 0]))
# 查看唯一具体信息
print('timepoint共有%i个唯一值' % len(gammas['timepoint'].value_counts()))
sns.tsplot(time='timepoint',  # 时间数据， x轴
           value='BOLD signal',  # y轴value
           unit='subject',  # 拆分，默认参数
           condition='ROI',  # 分类
           data=gammas
           )
plt.show()
'''
# 热图- heatmap()
'''
# 示例1----------
df = pd.DataFrame(np.random.randn(10,12))
sns.heatmap(df,vmin=0,vmax=1,  # 设置图例最大最小值
            )
plt.show()--------
# 示例2 - 设置参数
flights = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\flights.csv')
flights = flights.pivot('month', 'year', 'passengers')
print(flights.head())
sns.heatmap(flights,
            annot=True,  # 是否显示数值
            fmt='d',  # 格式化字符串
            linewidth=0,  # 格子边线宽度
            center=100,  # 调色盘的色彩中心值，若没有指定，则以cmap为主
            cmap='Reds',  # 设置调色盘
            cbar=True,  # 是否显示图例色带
            # bar_kws = ['orientaion':'horizaintal'], #是否横向显示图例色带
            # square = True   #是否正方形显示图表
            )
plt.show()
# 示例3：绘制半边热图------
rs = np.random.RandomState(33)
d = pd.DataFrame(rs.normal(size=(100, 26)))
corr = d.corr()  # 求解相关性矩阵表格
print(corr)
# 设置一个‘上三角形’蒙版
mask = np.zeros_like(corr,dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# 设置调色盘
cmap = sns.diverging_palette(220,10,as_cmap=True)
# 生成半边热图
sns.heatmap(corr,mask=mask,cmap=cmap,vmax=.3,center=0,
            square=True,linewidths=0.2)
plt.show()
'''

# 结构化图表可视化-FacetGrid()------------------
'''
# 绘制直方图
# 示例1
tips = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\tips.csv')
# 创建一个绘图表格区域，设置好row, col并分组
g = sns.FacetGrid(tips,col='time',row='smoker')
# 以total_bill 字段数据分别做直方图统计
g.map(plt.hist,'total_bill',alpha=0.5,color='k',bins=10)
plt.show()
# 示例2
g = sns.FacetGrid(tips,col='day',
                  size=4,   # 图表大小
                  aspect=0.5  # 图表长宽比
                  )
g.map(plt.hist, 'total_bill', bins=10,
      histtype='step',   # 'bar', 'barstacked', 'step', 'stepfilled'
      color='k')
plt.show()
# 示例3 绘制散点图
g = sns.FacetGrid(tips, col='time', row='smoker')
g.map(plt.scatter,
      'total_bill','tip',   # share(x,y) ---> 设置x，y数据
      edgecolor='w',s=40, linewidth=1  # 设置点大小，描边宽度及颜色
      )
g.add_legend()  # 添加图例
plt.show()
# 示例4 分类
# 创建一个绘图表格区域，设置好col并分组，按hue分类
g = sns.FacetGrid(tips, col='time',hue='smoker')
g.map(plt.scatter,
      'total_bill','tip',   # share(x,y) ---> 设置x，y数据
      edgecolor='w',s=40, linewidth=1  #设置点大小，描边宽度及颜色
      )
g.add_legend()
plt.show()
# 图表矩阵
attend = pd.read_csv('C:\\Users\刘邦国\PycharmProjects\study\data_visual\\attention.csv')
print(attend.head())
g = sns.FacetGrid(attend,col='subject',
                  col_wrap=5,  # 设置每行的图表数量
                  size=1.5)
g.map(plt.plot,'solutions','score',marker='o',color='gray',linewidth=2)
g.set(xlim=(0,4),
      ylim=(0,10),
      xticks=[0,1,2,3,4],
      yticks=[0,2,4,6,8,10])
plt.show()
'''

# 生成数据分析报告pandas_profiling
'''
data = pd.read_csv(r'C:\\Users\刘邦国\PycharmProjects\study\data_visual\csdn\titanic.csv',error_bad_lines=False)
import pprint  # 漂亮格式
pprint.pprint(data.head())
print(data.info())
import pandas_profiling as pp
report = pp.ProfileReport(data)
report.to_file('report.html')
'''
# 炫酷可视化
import cufflinks as cf

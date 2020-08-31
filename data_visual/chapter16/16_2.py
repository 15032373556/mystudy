import csv
from datetime import datetime
from matplotlib import pyplot as plt

def get_weather_data(filename,dates, highs, lows):
    """从文件中获取日期,最高气温和最低气温"""
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[0], "%Y-%m-%d")
                high = int(row[1])
                low = int(row[3])
            except ValueError:
                print(current_date, 'missing date')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

# 获取锡特卡的气温数据
dates, highs, lows = [],[],[]
get_weather_data('sitka_weather_2014.csv',dates, highs, lows)
# 根据数据绘制图形
fig = plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.6)
plt.plot(dates,lows,c='blue',alpha=0.6)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.2)

# 获取死亡谷的气温数据
dates, highs, lows = [],[],[]
get_weather_data('death_valley_2014.csv',dates, highs, lows)
#根据数据绘制图形
plt.plot(dates,highs,c='red',alpha=0.3)
plt.plot(dates,lows,c='blue',alpha=0.3)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形的格式
plt.title("Daily high and low temperatures - 2014\nsitka + death_valley",fontsize=24)
plt.xlabel("",fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis="both",which="major",labelsize=16)
plt.ylim(10,120)

plt.show()
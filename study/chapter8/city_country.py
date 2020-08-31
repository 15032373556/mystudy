def city_country(city_name,country):
    """城市名称及所属国家"""
    msg = '"' + city_name.title() + ',' + country.title() + '"'
    return msg

city_1 = city_country('santiago','chile')
print(city_1)
city_2 = city_country('new york','america')
print(city_2)
city_3 = city_country('beijing','china')
print(city_3)

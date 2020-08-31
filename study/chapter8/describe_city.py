def describe_city(city_name,country='china'):
    """城市名称及所属国家"""
    print(city_name.title() + " is in " + country.title() + '.')

describe_city('beijing')
describe_city('shanghai')
describe_city('new york')

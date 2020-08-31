cities ={
    '北京':{
        'coountry':'中国',
        'population':'2153.6万',
        'fact':'中国的首都。',
    },
    '纽约':{
        'coountry':'美国',
        'population':'851万',
        'fact':'自由女神像所在城市。',
    },
    '伦敦':{
        'coountry':'英国',
        'population':'890万',
        'fact':'世界第一大金融中心',
    },
}
for city,city_info in cities.items():
    print('\ncity name:' + city)
    for key,value in city_info.items():
        print('\t' + key + ':' + value)
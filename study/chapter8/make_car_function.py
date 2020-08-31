def make_car(manu,model,**car_info):
    """将一辆汽车的信息存储在一个字典中"""
    car_file = {}
    car_file['manufacturer'] = manu
    car_file['car_model'] = model
    for key,value in car_info.items():
        car_file[key] = value
    return car_file
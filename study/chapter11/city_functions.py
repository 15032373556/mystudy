def city_country(city_name,country_name,population=''):
    if population:
        msg = city_name.title() + ',' + country_name.title() + ' - population ' + str(population)
    else:
        msg = city_name.title() + ',' + country_name.title()
    return msg
judy = {
    'pet_type':'dog',
    'owner':'jimi',
}
sandy = {
    'pet_type':'cat',
    'owner':'david',
}
albert = {
    'pet_type':'bird',
    'owner':'danny',
}
pets = [judy,sandy,albert]
for pet in pets:
    #print(pet)
    for key,value in pet.items():
        print(key + ':' + value)
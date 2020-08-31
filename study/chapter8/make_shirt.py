def make_skirt(size='XXXL',word='"I love Python"'):
    """打印T恤的码数和字样"""
    print("This " + size + "-shirt has " + word + " on it." )

# make_skirt('L','Hello')
# make_skirt(size='L',word='Hello')

make_skirt()
make_skirt(size='XL')
make_skirt(size='L',word='Hello')
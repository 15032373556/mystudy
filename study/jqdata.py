import jqdatasdk as jq

jq.auth('15032373556','373556')
data = jq.get_price(security='000001.XSHE',start_date='2020-07-01',end_date='2020-07-07')
print(data)

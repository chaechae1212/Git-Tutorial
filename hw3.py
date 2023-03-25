def get_fixed_price(price,input_rate):
    fixed_price=price*(100/(100-input_rate))
    return fixed_price

rate=int(input('할인율은?'))

A=int(input('A 상품의 할인된 가격은?'))
B=int(input('B 상품의 할인된 가격은?'))

A_price=get_fixed_price(A,rate)
B_price=get_fixed_price(B,rate)

print('A 상품의 정가는',A_price,'원')
print('B 상품의 정가는',B_price,'원')




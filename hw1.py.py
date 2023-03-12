
def get_radius(prompt):
    r=int(input(prompt))
    return r

def get_circle_area(R):
    area=R**2*3.14
    return area


prompt='넓이를 구하고자 하는 원의 반지름은?'
R=get_radius(prompt)
print('반지름이 %.2f인 원의 넓이=3.14 x %.2f x %.2f = %.2f'%(R,R,R,get_circle_area(R)))
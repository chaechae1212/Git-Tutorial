def read_single_digit(N):
    number=["영","일","이","삼","사","오","육","칠","팔","구"]
    return number[N]

def read_number(n):
    if len(str(n))==1:
        m=read_single_digit(n)
        return m
    elif len(str(n))==2:
        number=["영","일","이","삼","사","오","육","칠","팔","구"]
        ten=n//10
        one=n%10
        return number[ten]+' '+number[one]
    elif len(str(n))==3:
        number=["영","일","이","삼","사","오","육","칠","팔","구"]
        hun=n//100
        ten=(n%100)//10
        one=((n%100)%10)
        return number[hun]+' '+number[ten]+' '+number[one]
    
num=int(input('세 자리 정수 입력:'))
result=read_number(num)
print(result)



        

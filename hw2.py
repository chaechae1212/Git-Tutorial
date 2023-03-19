def exchange(input_M):
    m_500=input_M//500
    input_M%=500
    m_100=input_M//100
    input_M%=100
    m_50=input_M//50
    input_M%=50
    m_10=input_M//10
    input_M%=10

    print('500원 동전의 개수:',m_500)
    print('100원 동전의 개수:',m_100)
    print('50원 동전의 개수:',m_50)
    print('10원 동전의 개수:',m_10)
   
def get_integer(prompt):
    m=int(input(prompt))
    return m

M=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(M)
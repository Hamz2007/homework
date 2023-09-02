def student(**info): 
    print(info)
    print(f"{info.get('first_name')} {info.get('last_name')} this is my name")  
    
student(first_name="hamzah",last_name="al-attas")
def empty_func():
    pass

empty_func()

def get_sma(*numbers): 
    full_number = sum(numbers)
    full_number /= len(numbers)

    return full_number 
sma = get_sma(5,6,6,4,2)
print(sma)

def make_math(first_num,opreratation,second_num):
    match opreratation:
        case"+":
            return first_num + second_num
        case"-":
            return first_num - second_num
        case"x"|"*":
            return first_num * second_num 
        case"/":
            return first_num / second_num
r=make_math(634,"/",612) 
print(r)   
 
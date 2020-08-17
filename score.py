score=int(input('score'))
if score>=0 and score<=100:
    if score >=90:
        print('a')
    elif score >=80:
        print('b')
    elif score >=70:
        print('c')
    elif score >=60:
        print('d')
    else:
       print('e')
else:
    print('rong')
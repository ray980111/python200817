eng=int(input('english score'))
math=int(input('math score'))
if eng <=100 and eng >=0 and math <=100 and math >=0:
    if eng<60 and math<60:
        print('punshment')
    elif eng<60 or math<60:
        print ('safe')
    elif eng>=90 and math>=90:
        print ('present')
else:
    print ('again ')

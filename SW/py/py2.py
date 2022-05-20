our_pots = {'김규진':1 , '김도원':2 , '김찬웅':3 , '김채은':4, '김태현':5} 
for i in our_pots:
    print(i)
    
    
for i in our_pots:
    print('{}의 집에는 {}개의 냄비가 있다'.format(i,our_pots[i]))
        
for i in our_pots :
    if our_pots[i] >= 3 :
        print('{}의 집에는 {}개의 냄비가 있다'.format(i,our_pots[i]))
        break
    

for x in range(2, 10):
    print("------- [" + str(x) +"] -------")
    for y in range(1, 10):
        print(x, "X", y, "=", x*y)
print("---------------------")
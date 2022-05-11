mun = "Happy programming"
for i,m in enumerate(mun):
    print(i,'-',m)
    
    
for i in range(1,9+1):
    if i == 7:
        break
    print("2 x {} = {}".format(i,2*i))
    
array = []
for i in range(1,10,2):
    array.append(i*i)
    
    
    
array = [i*i for i in range(1,10,2)]
print(array)
array = [i*i for i in range(1,10,2) if i*i > 30]
print(array)
array = [i*i for i in range(1,10,2)]
for i in range(5):
    array[i] = 0
print(array)
# 문제 1번

i = 0 
j = 0


while i < 100 :
    i = i+1
    j = j+i
print(i, j)

##########

# 문제 2번

i = 0
j = 0
sw = 0  

while i < 100:

    i = i + 1

    if sw == 0:  
        j = j + i
        sw = 1   
    else:       
        j = j - i
        sw = 0   

print(j)


##########

# 문제 3번 

# 1 : J = 1
# 2 : i = i + 1
# 3 : J = J * (-i)


i = 0
j = 1  


while i < 100:

    i = i + 1  

    if i % 2 == 0:  
        j = j * i
    else:           
        j = j * (-i)

print("최종 결과 (J):", j)
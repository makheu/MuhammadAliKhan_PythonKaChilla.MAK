#there are two kinds of loops, while and for loops
#while loops

# x=0
# while(x<5):
#     print(x)
#     x=x+1
#for loop

# for x in range(4,11):
#     print(x)    
    
# array 
days= ["mon", "tue", "wed", "thur", "fri", "sat", "sun"]

for d in days:
    # if (d=="fri"):break  # loops stops 
    if(d=="fri"):continue
    print(d)


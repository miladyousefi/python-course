first_vector=list(map(int, input().split()))
second_vector=list(map(int, input().split()))
sum=0
sign=-1
for i in range(0,len(first_vector)):
    sum +=sign*first_vector[i]*second_vector[i]
    sign *=-1    
print(sum)

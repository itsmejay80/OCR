# seq='CSQU305438'
seq='MEDU322018'
# seq='MEDU218229'


letters={'A':10,'B':12,'C':13,'D':14,'E':15,'F':16,'G':17,'I':18,'J':20,'K':21,'L':23,'M':24,'N':25,'O':26,'P':27,'Q':28,'R':29,'S':30,'T':31,'U':32,'V':34,'W':35,'X':36,'Y':37,'Z':38}
num=[0,0,0,0,0,0,0,0,0,0]
for i in range(4):
    num[i]=letters.get(seq[i])


for i in range(4,len(seq)):
    num[i]=int(seq[i])

print(num)
mult=[1,2,4,8,16,32,64,128,256,512]
sum=0
for i in range(len(num)):
    sum += num[i] * mult[i]

print(sum)

div=int(sum/11)
mult11=div*11
print(sum-mult11)

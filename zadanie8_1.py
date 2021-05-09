ptaki=['sroka','wrobel','orzel']

print ('--- po indeksie ---')
print (ptaki[0])
print (ptaki[1])
print (ptaki[2])


print ("--- po pętli for ---")
for s in ptaki:
    print (s)

print ('--- po idx w pętli')

for idx in range(len(ptaki)):
    print("idx: " + str(idx) + " : " + ptaki[idx])

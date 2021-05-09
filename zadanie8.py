samochody=['syrena','polonez']
pojemnosc=[0.9, 1.6]

print ('--- po indeksie ---')
print (samochody[0])
print (samochody[1])


print ("--- po pętli for ---")
for s in samochody:
    print (s)

print ('--- po idx w pętli')

for idx in range(len(samochody)):
    print("idx: " + str(idx) + " : " + samochody[idx])

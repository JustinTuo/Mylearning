i =1
while i:
    j=1
    while j:
        print j, "*", i, "=", i*j,'',
        if i==j:
            break
        j+=1
        if j>=10:
            break
    print "\n"
    i=i+1
    if  i>=10:
        break

i=1
while i<5:
    print(i*"*")
    i+=1
# break  (for)
i=1
while i<10:
    if (i==6):
        print("aya anestk bihom")
        break
    print(i)
    i+=1
#continue used to skip only the current iteration then continue in while loop   it breaks but skip and continue in the same time
i = 10
while i > 1:
    i-=1
    if i==6:
        print("this shit will be skipped")
        continue
    print(i)
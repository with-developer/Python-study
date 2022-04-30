for j in range(2,10,1):
    print("# %d단#"% j,end=" ")
print()
for i in range(1,10,1):
    for k in range(2,10,1):
        print("%dx%d=%2d"% (k,i,(i*k)), end=" ")
    print()


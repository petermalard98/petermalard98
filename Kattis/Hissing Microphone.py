a=input()

for i in range(len(a)-1):
    if a[i]==a[i+1]:
        print("hiss")
        break
else:
    print("no hiss")

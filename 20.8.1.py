a = input("Nhap vao nhanh: ")
d = {}
for i in range(len(a)):
    if(a[i] not in d.keys()):
       d[a[i]] = 1
    else:
        d[a[i]] = d[a[i]] + 1
for key, value in d.items():
       if(value > 0):
           print(key + "\t" , value)

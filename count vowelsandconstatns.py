vcount=0;
ccount=0;
str="Hi friend welcome to our channel";
str=str.lower();

for i in range(0,len(str)):
    if str[i] in ('a','e','i','o','u'):
        vcount=vcount+1;
    elif(str[i]>='a' and str[i]<='z'):
        ccount=ccount+1

print(vcount)
print(ccount)

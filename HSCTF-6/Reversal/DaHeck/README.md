# DaHeck

| Event | Title | Category | Cost |
|:------|:----------|:---------|-------:|
| HSCTF 6 | DaHeck| Reversal | ~300 |

### Discription
>Written by: ItzSomebody
>
>Unicode? ...da heck?
### Solution 

In this task we are given a program on Java that receives a string (a potential flag), encode it and check whether it is equal to another unicode string.
If the comparison is correct we are informed that we are right. Otherwise, we are wrong. 

Let's look through the code. The most interesting strings, that are executed in the main loop, are:
```java
if (heck[n] - cs[n % cs.length] < 0) daheck[n] = (char) (heck[n] - cs[n % cs.length] % 128);

else daheck[n] = (char) (heck[n] - cs[n % cs.length] % 255);
```

In order to make some conclusions, we have to take into account that number representation of unicode symbols varies from 0 to 65535.
Therefore, we can write decoding function, that will be an inverse one to the presented above: 


```py
s = u"\uffc8\uffbd\uffce\uffbc\uffca\uffb7\uffc5\uffcb\u0005\uffc5\uffd5\uffc1\uffff\uffc1\uffd8\uffd1\uffc4\uffcb\u0010\uffd3\uffc4\u0001\uffbf\uffbf\uffd1\uffc0\uffc5\uffbb\uffd5\uffbe\u0003\uffca\uffff\uffda\uffc3\u0007\uffc2\u0001\uffd4\uffc0\u0004\uffbe\uffff\uffbe\uffc1\ufffd\uffb5"
num = "001002939948347799120432047441372907443274204020958757273"
l = []
ans = ""
for i in range(len(s)):
    j = ord(num[i])-(ord(s[i])-65536)
    if j>128:
        ans += chr(j % 128)
    else: 
        ans += chr(j)
print(ans)
```
After all calculations we get the desired prize...
>hsctf{th4t_w4s_fun!_l3ts_try_s0m3_m0r3_r3v3rs3}

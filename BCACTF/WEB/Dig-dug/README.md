# Dig-dug

| Event | Title | Category | Cost |
|:------|:----------|:---------|-------:|
| BCACTF | dig-dug | WEB | 100 |

### Discription
>I found this super sketchy website called hole.sketchy.dev. Can you help me dig up some of its secrets?
>
>Oh, and someone told me that the secrets are TXT. I don't know what this means, so good luck!
>
>https://hole.sketchy.dev/

### Solution

Using tips on the Linux `dig` command, we get nothing.

![](https://github.com/Red-Cadets/CTF-writeups/blob/master/BCACTF/WEB/images/3_1.PNG)

A little googling the arguments of the command dig we found what we need.

![](https://github.com/Red-Cadets/CTF-writeups/blob/master/BCACTF/WEB/images/3_2.PNG)

##### Flag

```
bcactf{d1g-f0r-h073s-w/-dns-8044323}
```

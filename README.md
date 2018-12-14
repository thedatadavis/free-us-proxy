# free-us-proxy
Pulls list of free US proxies from www.us-proxy.org

Wrote this little script to replace copy and pasting from the site directly. It only returns a list of the ip addresses that resolve https.

Example response:

```
[{'ip_address': '206.189.184.18:3128',
  'is_ip_hidden': True,
  'is_proxy_hidden': True,
  'last_checked': '19 seconds ago'},
 {'ip_address': '192.241.129.232:80',
  'is_ip_hidden': True,
  'is_proxy_hidden': True,
  'last_checked': '19 seconds ago'}]
  ```
 
  
**A note on proxy anonymity from the site FAQs:**

There are 3 levels of proxies according to their anonymity.

- Level 1 - Elite Proxy / Highly Anonymous Proxy: The web server can't detect whether you are using a proxy.
- Level 2 - Anonymous Proxy: The web server can know you are using a proxy, but it can't know your real IP.
- Level 3 - Transparent Proxy: The web server can know you are using a proxy and it can also know your real IP.

I split these into two attributes `is_ip_hidden` and `is_proxy_hidden`. E.g. Level 2 is `True` and `False`, respectively.


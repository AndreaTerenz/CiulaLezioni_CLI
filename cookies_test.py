import http.cookiejar as http_cj
import urllib.request as url_rq
import urllib.response as url_rs
import requests
import browser_cookie3

url = "https://drive.google.com/drive/u/1/folders/1o9B3ZrbR2BRI0aJDNwl2dLXJUBVAvFkt"
cj = browser_cookie3.firefox(domain_name="drive.google.com")

r = requests.get(url, cookies=cj)

print(r)

fcj = http_cj.MozillaCookieJar("cookiez.txt")

fcj.save()

"""




cj = http_cj.CookieJar()
fcj = http_cj.MozillaCookieJar("cookiez.txt")


request = url_rq.Request(url)
response = url_rq.urlopen(request)

fcj.extract_cookies(response, request)

fcj.save("cookiez.txt")

cj = browser_cookie3.load(domain_name="drive.google.com")

opener = url_rq.build_opener(url_rq.HTTPCookieProcessor(cj))
login_html = opener.open(url).read()
"""
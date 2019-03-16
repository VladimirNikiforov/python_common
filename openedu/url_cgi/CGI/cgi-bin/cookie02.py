import os
import http.cookies

cookie=http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
cookie_name=cookie.get("name")

if cookie_name is None:
	print("Set-cookie: name='python3'")
	print("Content-type: text/html\n")
	print("На темной стороне есть печеньки")
else:
	print("Content-type: text/html\n")
	print("Печенька с именем")
	print(cookie_name.value)

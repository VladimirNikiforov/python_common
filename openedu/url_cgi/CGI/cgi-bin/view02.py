import cgi
import html

form = cgi.FieldStorage()
text_1 = form.getfirst("author","not set")
text_1=html.escape(text_1)
text_2 = form.getfirst("book","not set")
text_2=html.escape(text_2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
		<html>
		<head>
			<meta charset="cp1251">
			<title>Obrabotka knig</title>
		</head>
		<body>""")

print("<h1>Obrabotka knig</h1>")
print("<p>Author: %s </p>"%text_1)
print("<p>Book: %s </p>"%text_2)

print("""</body>
		</html>""")
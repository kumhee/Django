import cgi

form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
url = form.getvalue('url')

print("Content-Type: text/plain")

print("Welcome...CGI CODE")
print("name : ", name)
print("email : ", email)
print("url : ", url)
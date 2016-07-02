import cgi
form = cgi.FieldStorage()
user = form.getfirst("user", "").upper() 
print user
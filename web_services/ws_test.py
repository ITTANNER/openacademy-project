import functools
import xmlrpclib

HOST = 'localhost'
PORT = 8069
DB = 'odoo_curso'
USER = 'admin'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
if uid == 0:
    print "Error: Incorrect --->  Username or Password"
else:
    print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# 2. Read the sessions
model = 'openacademy.session'
domain = []
method_name = 'search_read'

sessions = call(model,method_name, domain, ['name','seats','taken_seats'])
print "sessions", sessions

for session in sessions:
   print "Session %s (%s seats), taken seats %d" % (session['name'], session['seats'], session['taken_seats'])


# 3.create a new session

course_ids = call('openacademy.course', 'search', [('name','=','Course 0')])
#print "-----COURSO IDS --------",course_ids
course_id = course_ids[0]

session_id = call(model, 'create', {
   'name' : 'My session from Web Service',
   'course_id' : course_id,
   'seats' : 25,
})

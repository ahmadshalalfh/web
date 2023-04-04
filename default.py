import webbrowser

from gluon import DAL


def index():


    if request.vars['first']:
      first = request.vars['first']
      last = request.vars['last']
      email = request.vars['email']
      password = request.vars['password']


      db.executesql("INSERT INTO students (  first_name,last_name, email,passwords) VALUES ( %s , %s, %s ,%s)", placeholders=( first,last, email,password))

      redirect(URL('default', 'clic'))

    else:


     return locals()






def login():

    x = "ee"
    if request.vars['username']:
       username = request.vars['username']
       password = request.vars['password']
       x = db.executesql("select email from web.students where passwords =" + password , as_dict=True)
       return dict(x =x[0])

    else:

     return dict(x =x)

def userp():

   courses = db.executesql("SELECT * FROM courses  " , as_dict=True)


   return dict(courses = courses)


def courses():

        if request.vars['code']:
         code = request.vars['code']
         courses = db.executesql("SELECT * FROM courses WHERE course_code=" + code, as_dict=True)
         return dict(courses=courses )
        elif request.vars['name']:
         name = request.vars['name']
         courses = db.executesql("SELECT * FROM courses WHERE course_code=" + name, as_dict=True)
         return dict(courses=courses )
        elif request.vars['instructor']:
         name = request.vars['instructor']
         courses = db.executesql("SELECT * FROM courses WHERE course_code=" + name, as_dict=True)
         return dict(courses=courses )




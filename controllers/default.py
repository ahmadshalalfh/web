# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    response.flash = T("Hello World")
    return dict(message=T('Welcome to web2py!'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----


def reg():


    if request.vars['first']:
      first = request.vars['first']
      last = request.vars['last']
      email = request.vars['email']
      password = request.vars['password']
      registration_key = request.vars['registration_key']


      db.executesql("INSERT INTO student (  first_name,last_name, email,password , registration_key) VALUES (%s, %s , %s, %s ,%s)", placeholders=( first,last, email,password , registration_key))

      redirect(URL('default', 'user'))

    else:


     return locals()

@auth.requires_login()
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


@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)
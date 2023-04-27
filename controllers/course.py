
@auth.requires_login()
def incourse():
    form = SQLFORM (db.courses)
    if form.process().accepted:
        response.flash='form accepted'
    elif form.errors:
        response.flash='form has errors'
    else:
        response.flash='please fill out the form'

    return dict(form=form)
def copy_selected_rows(form ):

      student_id = auth.user.id

      try:

            for id in form:
                 row = db.courseschedules(id)
                 days = db(db.studentchedules.days == row.days).select()
                 start_time = db(db.studentchedules.start_time == row.start_time).select()


                 if days  and start_time :
                     return locals()
                 else:
                   if row.numper_of_student != row.cabasety:
                     db.studentchedules.insert(schedual_id=None,
                                                      course_schedual=row.schedule_id,
                                                   id=student_id,
                                                   days=row.days,
                                                   start_time = row.start_time,
                                                   end_time = row.end_time,
                                                   room_num = row.room_no)


                     db(db.courseschedules.schedule_id==row.schedule_id).update(numper_of_student=row.numper_of_student + 1)
            response.flash='تم الحفظ'
      except Exception:
            response.flash='يوجد تعارض في الجدول'



@auth.requires_login()
def schedules():

    grid = SQLFORM.grid(db.courseschedules , deletable=False, csv=False ,selectable=copy_selected_rows,  formargs=dict(onsubmit=copy_selected_rows),
                    selectable_submit_button=' save' )

    return dict(grid = grid )



def courses():
    grid = SQLFORM.grid(db.courses , deletable=False, csv=False  )
    return dict(grid = grid)


def delete(form ):

      for id in form:
         row = db.studentchedules(id)

         db( db.studentchedules.schedual_id == row.schedual_id ).delete()
         db(db.courseschedules.schedule_id==row.course_schedual ).update(numper_of_student=db.courseschedules.numper_of_student - 1)






def studentschedules():

    grid = SQLFORM.grid(db.studentchedules ,selectable=delete,selectable_submit_button=' delete',  create=False,editable=False,  csv=False)
    return dict(grid=grid)

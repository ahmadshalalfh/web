
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
      selected_ids = request.vars._select
      for id in selected_ids:
                row = db.mytable(id)
                db.student_schedules.insert(
                                       days=row.days,
                                       start_time = row.start_time,
                                       end_time = row.end_time,
                                       room_no = row.room_no)
                grid.elements('input[type=submit]')[0]['_onclick'] = "return ajax('copy_selected_rows', ['" + grid._id + "'], ':eval')"


@auth.requires_login()
def schedules():
     grid = SQLFORM.grid(db.courseschedules , deletable=False, csv=False ,selectable=copy_selected_rows,  formargs=dict(onsubmit=copy_selected_rows),
                    selectable_submit_button=' save' )



     return dict(grid = grid)


def courses():
    grid = SQLFORM.grid(db.courses , deletable=False, csv=False  )
    return dict(grid = grid)




def studentschedules():
    grid = SQLFORM.grid(db.student_schedules , deletable=False, csv=False )
    return dict(grid = grid)

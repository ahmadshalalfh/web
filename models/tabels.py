import datetime


db.define_table('courses',
    Field('course_code', 'string', required=True , nitnull = True),
    Field('course_name', 'string' ),
    Field('description', 'text' ),
    Field('prerequisites', 'string', 'reference courses' , requires=IS_IN_DB(db,'courses.course_code','%(course_name)s')),
    Field('instructor', 'string'),
    Field('capacity', 'integer'),
    Field('schedule_id', 'integer','reference courseschedules',requires=IS_IN_DB(db, 'courseschedules.schedule_id' , '%(days)s: %(start_time)s - %(end_time)s' )),
   primarykey =['course_code']
   )

db.define_table('courseschedules',
    Field('schedule_id', 'integer', required=True , notnull = True),
    Field('days', 'string'),
    Field('start_time', 'time'),
    Field('end_time', 'time', ),
    Field('room_no', 'string'),
    Field('cabasety', 'int'),


   primarykey =['schedule_id']
   )
db.define_table('studentchedules',
    Field('schedule_id', 'integer', required=True , notnull = True),
    Field('days', 'string'),
    Field('start_time', 'time'),
    Field('end_time', 'time', ),
    Field('room_no', 'string'),
    Field('cabasety', 'int'),

   primarykey =['schedule_id']
   )


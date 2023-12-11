search_user_query = '''select * from visitor where name = %s and surname = %s and patronymic = %s and passport = %s'''
delete_user_query = '''delete from visitor where passport = %s'''

query_emp = '''select * from staff'''
query_tasks = '''select * from schedule'''

search_empl_query = '''select * from staff where passport = %s and name = %s and surname = %s and patronymic = %s'''
delete_empl_query = '''delete from staff where passport = %s and name = %s and surname = %s and patronymic = %s'''
add_empl_query = '''Insert into staff(name, surname, patronymic, passport, experience, salary) values (%s, %s, %s, %s, %s, %s)'''
update_salary = '''update staff set salary = %s where passport = %s and name = %s and surname = %s and patronymic = %s'''


search_task_query = '''select * from schedule where staff_id = %s and task_id = %s and room_id = %s and date = %s 
and date_end = %s and ordered = %s'''
delete_task_query = '''delete from schedule where schedule_id = %s'''
insert_task_query = '''insert into schedule(task_id, staff_id, room_id, date, date_end, ordered) values (%s, %s, %s, %s, %s, %s)'''

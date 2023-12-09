search_user_query = '''select * from visitor where name = %s and surname = %s and patronymic = %s and passport = %s'''
delete_user_query = '''delete from visitor where passport = %s'''
query_emp = '''select * from staff'''
query_tasks = '''select * from schedule'''

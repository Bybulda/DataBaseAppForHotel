query = "select room_id, settle_datetime, eviction_datetime from hotel_schema.booking " \
        "where visitor_id = (select visitor_id from hotel_schema.visitor where passport = %s and " \
        "name = %s and surname = %s and patronymic = %s)"
serach_query = '''Select v.visitor_id from visitor v where v.name = %s and v.surname = %s and v.patronymic = %s and 
v.passport = %s'''
insrt_vis = '''Insert Into visitor(name, surname, patronymic, passport, phone_number, gender) Values(%s, %s, %s, %s, %s, %s)'''
search_room_time = '''select room_id from room where type = %s except select distinct room_id from booking b where
(b.settle_datetime <= %s and b.eviction_datetime >= %s) or 
(b.settle_datetime > %s and b.eviction_datetime < %s) or
(b.settle_datetime = %s and b.eviction_datetime > %s) or
(b.settle_datetime > %s and b.eviction_datetime = %s)
'''


insrt_book = '''Insert into booking(visitor_id, room_id, settle_datetime, eviction_datetime) values(
%s, %s, %s, %s)'''
room_price = '''select distinct price from room where type = %s'''
search_booking_pos = '''select distinct b.booking_id from booking b where b.visitor_id = (select v.visitor_id from visitor v where v.passport = %s) and b.settle_datetime = %s and b.eviction_datetime = %s'''
cancel_booking = '''delete from booking where booking_id = %s'''

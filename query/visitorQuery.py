query = "select room_id, settle_datetime, eviction_datetime from hotel_schema.booking " \
        "where visitor_id = (select visitor_id from hotel_schema.visitor where passport = %s and " \
        "name = %s and surname = %s and patronymic = %s)"
serach_query = '''Select v.visitor_id from visitor v where v.name = %s and v.surname = %s and v.patronymic = %s and 
v.passport = %s'''
insrt_vis = '''Insert Into table visitor v (v.name, v.surname, v.patronymic, v.passport, v.passport, v.phone, 
v.gender) Values(%s, %s, %s, %s, %s, %s)'''
search_room_time = '''select r.room_id from room r where r.type = 'classic' and (r.room_id in (select b.room_id from booking 
b where %s not between b.settle_datetime and b.eviction_datetime and %s not between b.settle_datetime and b.eviction_datetime) or r.room_id not in (select d.room_id from booking d))'''
insrt_book = '''Insert into table booking b (b.visitor_id, b.room_id, b.settle_datetime, b.eviction_datetime) values(
%s, %s, %s, %s)'''
room_price = '''select distinct r.price from room where r.type = %s'''
search_booking_pos = '''select b.visitor_id from booking b where b.visitor_id = (select v.visitor_id where passport = %s) and %s = b.settle_datetime'''
cancel_booking = '''delete from booking where visitor_id = %s and (settle_datetime = %s or eviction_datetime = %s)'''

serach_query = '''Select v.visitor_id from visitor v where v.name = %s and v.surname = %s and v.patronymic = %s and 
v.passport = %s'''
insrt_vis = '''Insert Into table visitor v (v.name, v.surname, v.patronymic, v.passport, v.passport, v.phone, 
v.gender) Values(%s, %s, %s, %s, %s, %s)'''
search_room_time = '''select r.room_id from room r where r.type = %s and r.room_id in (select b.room_id from booking 
b where not %s between b.settle_datetime and b.evictionand not %s between b.settle_datetime and b.eviction)'''
insrt_book = '''Insert into table booking b (b.visitor_id, b.room_id, b.settle_datetime, b.eviction_datetime) values(
%s, %s, %s, %s)'''
room_price = '''select distinct r.price from room where r.type = %s'''

print(insrt_book)
print(room_price)
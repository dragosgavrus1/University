set transaction isolation level read committed --soultion
set transaction isolation level repeatable read 

begin tran
select * from product
exec sp_log_locks 'Non-Repeatable Reads 2: between selects'
waitfor delay '00:00:10'
select * from product
exec sp_log_locks 'Non-Repeatable Reads 2: after both selects'
commit tran 
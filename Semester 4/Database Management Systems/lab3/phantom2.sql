set transaction isolation level repeatable read --solution
set transaction isolation level serializable 

begin tran
select * from product
exec sp_log_locks 'Phantom 2: between selects'
waitfor delay '00:00:10'
select * from product
exec sp_log_locks 'Phantom 2: after both selects'
commit tran 
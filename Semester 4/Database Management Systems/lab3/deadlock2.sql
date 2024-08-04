begin tran
update product set product_name = 'Deadlock tran 2' where product_id = 10
exec sp_log_locks 'Deadlock 2: between updates'
waitfor delay '00:00:05'
update orders set order_date='2000-2-2' where order_id=20
commit tran
begin tran
declare @oldData int
declare @newData int
update product set @oldData=unit_price, unit_price=1000, @newData=unit_price where product_id=10
exec sp_log_changes @oldData, @newData, 'Dirty reads 1: update'
exec sp_log_locks 'Dirty reads 1: after update'
waitfor delay '00:00:10'
update product set @oldData=unit_price, unit_price=1500, @newData=unit_price where product_id=10
exec sp_log_changes @oldData, @newData, 'Dirty reads 1: update'
exec sp_log_locks 'Dirty reads 1: after update'
waitfor delay '00:00:10'
commit tran
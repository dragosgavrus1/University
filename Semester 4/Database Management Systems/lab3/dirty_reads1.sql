select @@TRANCOUNT
select @@SPID

insert into product(product_id, product_name, unit_price) values(10, 'Deadlock', 35)
Delete from product where product_id = 10

select * from orders
select * from product

set transaction isolation level read uncommitted --solution
set transaction isolation level read committed 

begin tran 
select * from product
exec sp_log_locks 'Dirty reads 2: after select'
waitfor delay '00:00:10'
select * from product
waitfor delay '00:00:10'
select * from product
commit tran


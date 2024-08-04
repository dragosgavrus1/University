select @@TRANCOUNT
select @@SPID

Insert into orders(order_id, order_date) Values (20, '2019-12-12')
insert into product(product_id, product_name, unit_price) values(10, 'Deadlock', 35)
Delete from orders where order_id = 20
Delete from product where product_id = 10

select * from orders
select * from product

begin tran
update orders set order_date='2000-1-1' where order_id=20
exec sp_log_locks 'Deadlock 1: between updates'
waitfor delay '00:00:10'
update product set product_name = 'Deadlock tran 1' where product_id = 10
commit tran
select @@TRANCOUNT
select @@SPID

Insert into orders(order_id, order_date) Values (20, '2019-12-12')
insert into product(product_id, product_name, unit_price) values(10, 'Name1', 35)
Delete from orders where order_id = 20
Delete from product where product_id = 10
Delete from product where product_id = 11

select * from orders
select * from product

begin tran
waitfor delay '00:00:10'
insert into product(product_id, product_name, unit_price) values(11, 'Name2', 42)
exec sp_log_changes null, 3, 'Phantom 1: insert'
exec sp_log_locks 'Phantom 1: after insert'
commit tran
select @@TRANCOUNT
select @@SPID

Insert into orders(order_id, order_date) Values (20, '2019-12-12')
insert into product(product_id, product_name, unit_price) values(10, 'Name1', 35)
Delete from orders where order_id = 20
Delete from product where product_id = 10

select * from orders
select * from product

begin tran
declare @oldData int
declare @newData int
waitfor delay '00:00:10'
SELECT @oldData = unit_price
FROM product
WHERE product_id = 10

UPDATE product
SET unit_price = 1000
WHERE product_id = 10

SELECT @newData = unit_price
FROM product
WHERE product_id = 10
exec sp_log_changes @oldData, @newData, 'Non-Repeatable Reads 1: update'
exec sp_log_locks 'Non-Repeatable Reads 1: after update'
commit tran


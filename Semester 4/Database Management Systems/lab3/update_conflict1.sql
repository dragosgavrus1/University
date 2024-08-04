select @@TRANCOUNT
select @@SPID

Insert into orders(order_id, order_date) Values (20, '2019-12-12')
insert into product(product_id, product_name, unit_price) values(10, 'Name1', 35)
Delete from orders where order_id = 20
Delete from product where product_id = 10

select * from orders
select * from product

begin tran
declare @oldData varchar(100)
declare @newData varchar(100)
SELECT @oldData = product_name
FROM product
WHERE product_id = 10

UPDATE product
SET product_name = 'Name2'
WHERE product_id = 10

SELECT @newData = product_name
FROM product
WHERE product_id = 10
waitfor delay '00:00:10'
exec sp_log_changes @oldData, @newData, 'Update Conflict 1: update'
exec sp_log_locks 'Update Conflict 1: after update'
select * from product
commit tran
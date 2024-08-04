SET TRANSACTION ISOLATION LEVEL SNAPSHOT
set transaction isolation level read uncommitted -- solution 
ALTER DATABASE [Sales Management] SET ALLOW_SNAPSHOT_ISOLATION ON

begin tran
declare @oldData varchar(100)
declare @newData varchar(100)
SELECT @oldData = product_name
FROM product
WHERE product_id = 10

UPDATE product
SET product_name = 'Name3'
WHERE product_id = 10

SELECT @newData = product_name
FROM product
WHERE product_id = 10
exec sp_log_changes @oldData, @newData, 'Update Conflict 2: update'
exec sp_log_locks 'Update Conflict 2: after update'
select * from product
commit tran
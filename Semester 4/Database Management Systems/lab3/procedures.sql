
go
create or alter procedure addRowOrders(@date date) as
	DECLARE @maxId INT
	SET @maxId = 0
	Select TOP 1 @maxId = order_id + 1 FROM orders ORDER BY order_id DESC
	if (@date is null)
	BEGIN
		RAISERROR('Order date must not be null', 24, 1);
	END

	Insert into orders(order_id, order_date) Values(@maxId, @date);
	EXEC sp_log_changes null, @date, 'Added row to orders'
go

create or alter procedure addRowProduct(@name varchar(30), @price int) as
	DECLARE @maxId INT
	SET @maxId = 0
	Select TOP 1 @maxId = product_id + 1 FROM product ORDER BY product_id DESC
	if (@name is null)
	BEGIN
		RAISERROR('Product name must not be null', 24, 1);
	END
	if (@price < 0)
	Begin
		RAISERROR('Product price must not be negative', 24, 1);
	End

	Insert into product (product_id, product_name, unit_price) values (@maxId, @name, @price)
	exec sp_log_changes null, @name, 'Added row to product'
go

create or alter procedure addRowOrder_item(@orderDate date, @product_name varchar(30)) as
	If (@orderDate is null)
	BEGIN
		RAISERROR('Order date must not be null', 24, 1);
	END

	if (@product_name is null)
	BEGIN
		RAISERROR('Product name must not be null', 24, 1);
	END

	Declare @OrderId INT
	SET @OrderId  = (SELECT order_id from orders Where order_date = @orderDate)
	Declare @ProductId INT
	SET @ProductId = (Select product_id from product where product_name = @product_name)
	IF (@OrderId is null)
	BEGIN
		RAISERROR('Order does not exist', 24, 1);
	END
	IF (@ProductId is null)
	BEGIN
		RAISERROR('Product does not exist', 24, 1);
	END

	Insert into order_item(order_id, product_id, quantity) Values (@OrderId, @ProductId, 10)
	declare @newData varchar(100)
    SET @newData = @product_name + ' ' + CONVERT(VARCHAR, @orderDate, 120)
	exec sp_log_changes null, @newData, 'Connected order with product'
GO


CREATE OR ALTER PROCEDURE rollbackScenarioNoFail
AS
	BEGIN TRAN
	BEGIN TRY
		EXEC addRowOrders '2020-1-1'
		EXEC addRowProduct 'Product', 300
		EXEC addRowOrder_item '2020-1-1', 'Product'
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		RETURN
	END CATCH
	COMMIT TRAN
GO

CREATE OR ALTER PROCEDURE rollbackScenarioFail
AS
	BEGIN TRAN
	BEGIN TRY
		EXEC addRowOrders '2020-1-1'
		EXEC addRowProduct 'Product Fail', 300
		EXEC addRowOrder_item '2020-1-1', 'Product'
	END TRY
	BEGIN CATCH
		ROLLBACK TRAN
		RETURN
	END CATCH
	COMMIT TRAN
GO

CREATE OR ALTER PROCEDURE noRollbackScenarioManyToManyNoFail
AS
	BEGIN TRY
		BEGIN TRANSACTION
		EXEC addRowOrders '2020-1-1'
		COMMIT TRANSACTION
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
			ROLLBACK TRANSACTION
	END CATCH

	BEGIN TRY
		BEGIN TRANSACTION
		EXEC addRowProduct 'Product', 300
		COMMIT TRANSACTION
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
			ROLLBACK TRANSACTION
	END CATCH

	BEGIN TRY
        BEGIN TRANSACTION
        EXEC addRowOrder_item '2020-1-1', 'Product'
        COMMIT TRANSACTION
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION
    END CATCH


GO
CREATE OR ALTER PROCEDURE noRollbackScenarioManyToManyFail
AS

	BEGIN TRY
		BEGIN TRANSACTION
		EXEC addRowOrders '2020-1-1'
		COMMIT TRANSACTION
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
			ROLLBACK TRANSACTION
	END CATCH

	BEGIN TRY
		BEGIN TRANSACTION
		EXEC addRowProduct 'Product', 300
		COMMIT TRANSACTION
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
			ROLLBACK TRANSACTION
	END CATCH

	BEGIN TRY
        BEGIN TRANSACTION
        EXEC addRowOrder_item '2020-1-1', 'Produc'
        COMMIT TRANSACTION
    END TRY
    BEGIN CATCH
        IF @@TRANCOUNT > 0
            ROLLBACK TRANSACTION
    END CATCH
GO

Select * from orders
select * from order_item
select * from product

delete from orders where order_id = 3
delete from product where product_name = 'Product'
delete from order_item where order_id = 3

exec rollbackScenarioFail
exec rollbackScenarioNoFail
exec noRollbackScenarioManyToManyFail
exec noRollbackScenarioManyToManyNoFail
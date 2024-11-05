CREATE TABLE [dbo].[Sales] (

	[OrderNo] bigint NULL, 
	[ItemID] bigint NULL, 
	[SalesDate] date NULL, 
	[DeilveryDate] date NULL, 
	[CustomerId] bigint NULL, 
	[CityId] bigint NULL, 
	[Qty] bigint NULL, 
	[Price] bigint NULL, 
	[cost] bigint NULL, 
	[DiscountPercent] bigint NULL, 
	[Gross Amount] float NULL, 
	[COGSAmount] float NULL, 
	[Discount Amount] float NULL
);


GO
ALTER TABLE [dbo].[Sales] ADD CONSTRAINT FK_654b3bf6_930a_4201_a3c8_8810918fff77 FOREIGN KEY ([CustomerId]) REFERENCES [dbo].[Customer]([CustomerId]);
GO
ALTER TABLE [dbo].[Sales] ADD CONSTRAINT FK_85d613ae_b494_46fd_ab89_1e2fe7e6ca3d FOREIGN KEY ([ItemID]) REFERENCES [dbo].[Item]([ItemId]);
GO
ALTER TABLE [dbo].[Sales] ADD CONSTRAINT FK_f5b0f8dc_cf66_4c42_803c_20d4443ea8bb FOREIGN KEY ([CityId]) REFERENCES [dbo].[Geography]([CityId]);
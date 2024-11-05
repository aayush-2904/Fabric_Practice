CREATE TABLE [dbo].[Item] (

	[ItemId] bigint NULL, 
	[Name] varchar(8000) NULL, 
	[BrandId] bigint NULL, 
	[CategoryId] bigint NULL, 
	[SubCategoryId] bigint NULL, 
	[Brand] varchar(8000) NULL, 
	[Category] varchar(8000) NULL, 
	[SubCategory] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[Item] ADD CONSTRAINT UQ_5f34251a_b724_4619_8f28_bb58413b3a28 unique NONCLUSTERED ([ItemId]);
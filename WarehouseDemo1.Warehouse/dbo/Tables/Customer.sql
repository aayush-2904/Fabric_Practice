CREATE TABLE [dbo].[Customer] (

	[CustomerId] bigint NULL, 
	[Age] bigint NULL, 
	[City] varchar(8000) NULL, 
	[State] varchar(8000) NULL, 
	[Name] varchar(8000) NULL, 
	[Category] varchar(10) NULL, 
	[Category1] varchar(10) NULL
);


GO
ALTER TABLE [dbo].[Customer] ADD CONSTRAINT UQ_f006a86d_01eb_46b4_9e1f_83662b4976e0 unique NONCLUSTERED ([CustomerId]);
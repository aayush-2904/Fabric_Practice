CREATE TABLE [dbo].[Geography] (

	[CityId] bigint NULL, 
	[City] varchar(8000) NULL, 
	[State] varchar(8000) NULL
);


GO
ALTER TABLE [dbo].[Geography] ADD CONSTRAINT UQ_cbbf6755_e7b0_4c86_b34f_18f4d58b603a unique NONCLUSTERED ([CityId]);
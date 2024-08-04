create Table Author(
	 AuthorID int primary key,
	 AuthorName varchar(30)
)

create Table Book(
	BookID int,
	AuthorID int foreign key references Author(AuthorID),
	BookTitle varchar(30)
)

insert into Author values(2, 'Petrescu')
insert into Book values(2, 2, 'Ultima Noapte')
select * from Book
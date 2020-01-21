use sqldb;
create table memberTbl
(userId char(10) PRIMARY KEY NOT NULL,
password char(8) NOT NULL,
email char(20) NOT NULL,
joinDate DATETIME DEFAULT now()
);

insert into memberTbl (userId, password, email)
VALUES ('cherry','4321','cherry@google.com');

select * from memberTbl;
\c llin15

drop table ostudent cascade;
create table ostudent (
  sid   int primary key,
  fname varchar(20),
  lname varchar(20),
  email varchar(40),
  degree varchar(10) check (degree in ('MS','PhD'))
);

drop table ocourse cascade;
create table ocourse (
  cprefix   char(4) default 'CSC',
  cno       int,
  ctitle    varchar(40),
  hours     int,
  primary key (cprefix,cno)
);


drop table oenroll cascade;
create table oenroll (
  sid      int,
  term     char(2) check (term in ('FA','SP','SU')),
  year     int,
  cprefix  char(4),
  cno      int,
  grade    char(2) check (grade in ('A','B','C','D','F','I','IP','S','U')),
  primary key (sid,term,year,cprefix,cno),
  foreign key (sid) references ostudent,
  foreign key (cprefix,cno) references ocourse
);

drop table oassistantship cascade;
create table oassistantship (
  sid    int,
  term   char(2) check (term in ('FA','SP','SU')),
  year   int,
  assistantship char(1) check (assistantship in ('Y', 'N')),
  primary key (sid,term,year),
  foreign key (sid) references ostudent
);

drop table ograde cascade;
create table ograde (
  sid    int,
  term   char(2) check (term in ('FA','SP','SU')),
  year   int,
  grade    char(2) check (grade in ('A','B','C','D','F','I','IP','S','U')),
  primary key (sid,term,year),
  foreign key (sid) references ostudent
);


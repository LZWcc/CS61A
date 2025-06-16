create table animals as
    select "dog" as kind, 4 as legs  , 20 as weight union
    select "cat"           , 4       , 10           union
    select "ferret"        , 4       , 10           union
    select "parrot"        , 2       , 6            union
    select "penguin"       , 2       , 10           union
    select "t-rex"         , 2       , 12000;

select max(legs) from animals;
select max(weight) from animals;
select max(weight), kind from animals;
select min(kind), legs, weight from animals;
select avg(weight) from animals;
select avg(weight), kind from animals;

select legs from animals group by legs;
select legs, count(*) from animals group by legs;

create table primes(n, prime);
drop table if exists primes;

create table primes (n UNIQUE, prime DEFAULT 1);
INSERT INTO primes VALUES (2, 1), (3, 1);
INSERT INTO primes(n) VALUES (4), (5), (6), (7);
-- 这里的 (n) 表示只向 n 这一列插入数据
INSERT INTO primes(n) SELECT n+6 FROM primes;


UPDATE primes SET prime = 0 WHERE n > 2 AND n % 2 = 0;
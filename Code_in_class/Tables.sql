create table cities as
    select 38 as latitude, 122 as longitude, "Berkeley" as name union
    select 42,              71,              "Cambridge"        union
    select 45,              93,              "Minneapolis"      union
    select 33,             117,              "San Diego"        union
    select 26,              80,              "Miami"            union
    select 90,               0,              "North Pole";
create table cold as
    select name from cities where latitude >= 43;

create table distances as
    select a.name as first, b.name as second,
        60 * (b.latitude - a.latitude) as distance
        from cities as a, cities as b;

select "hello," ||  " world";

create table nouns as
    select "dog" as phrase union
    select "cat"           union
    select "bird";

select subject.phrase || " chased " || object.phrase
    from nouns as subject, nouns as object
    where subject.phrase <> object.phrase;

create table ands as
    select first.phrase || " and " || second.phrase
           from nouns as first, nouns as second
           where first.phrase <> second.phrase;
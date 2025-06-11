--select "abraham" as parents, "barack" as child;

create table parent as
	select "abraham" as parent, "barack" as child union
	select "abraham"		  , "clinton"		  union
	select "delano"		  	  , "herbert";

--select [expression] as [name], [expression] as [name]

--select [columns] from [table] where [condition] order by [order]

--select * from parents
-- FROM 指定要查询的数据表, 从table中查询数据
-- where 指定查询条件, 只查询满足条件的数据
-- order by 指定查询结果的排序方式, 按照order的顺序进行排序

-- Given the table ints that describes how to sum powers of 2 to form various integers,
-- 展示了如何用 1、2、4、8 这些 2 的幂相加，来组成不同的整数
--                      2的0次方,  2的1次方,   2的2次方,   2的3次方
create table ints as
    select "zero" as word, 0 as one, 0 as two, 0 as four, 0 as eight union
    select "one"         , 1       , 0       , 0       ,  0          union
    select "two"         , 0       , 2       , 0       ,  0          union
    select "three"       , 1       , 2       , 0       ,  0          union
    select "four"        , 0       , 0       , 4       ,  0          union
    select "five"        , 1       , 0       , 4       ,  0          union
    select "six"         , 0       , 2       , 4       ,  0          union
    select "seven"       , 1       , 2       , 4       ,  0          union
    select "eight"       , 0       , 0       , 0       ,  8          union
    select "nine"        , 1       , 0       , 0       ,  8;
--select 后面可以写列名，也可以写表达式（比如加法、乘法等）。
--as value 是给表达式结果起一个别名，这里 value 就是新列的名字。
-- select word, one+two+four+eight as value
-- from ints;

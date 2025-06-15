CREATE TABLE parents AS
  SELECT "ace" AS parent, "bella" AS child UNION
  SELECT "ace"          , "charlie"        UNION
  SELECT "daisy"        , "hank"           UNION
  SELECT "finn"         , "ace"            UNION
  SELECT "finn"         , "daisy"          UNION
  SELECT "finn"         , "ginger"         UNION
  SELECT "ellie"        , "finn";

CREATE TABLE dogs AS
  SELECT "ace" AS name, "long" AS fur, 26 AS height UNION
  SELECT "bella"      , "short"      , 52           UNION
  SELECT "charlie"    , "long"       , 47           UNION
  SELECT "daisy"      , "long"       , 46           UNION
  SELECT "ellie"      , "short"      , 35           UNION
  SELECT "finn"       , "curly"      , 32           UNION
  SELECT "ginger"     , "short"      , 28           UNION
  SELECT "hank"       , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
-- 1. 选择child列, 从parents表和dogs表中查询
-- 2. 连接条件是parent等于dogs表中的name, WHRER 条件
-- 3. 按照height列降序排序
CREATE TABLE by_parent_height AS
  SELECT child FROM parents, dogs
  WHERE parent = name
  ORDER BY height DESC;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes
  WHERE height > min AND height <= max;


-- [Optional] Filling out this helper table is recommended
CREATE TABLE siblings AS
  SELECT a.child AS sibling1, b.child AS sibling2
  FROM parents AS a, parents AS b
  WHERE a.parent = b.parent AND a.child < b.child;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings, " || sibling1 || " and " || sibling2 || ", have the same size: " || a.size
  FROM siblings, size_of_dogs AS a, size_of_dogs AS b
  WHERE a.name = sibling1 AND b.name = sibling2 AND a.size = b.size;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height
CREATE TABLE low_variance AS
  SELECT DISTINCT fur, MAX(height) - MIN(height) AS range
  FROM dogs
  GROUP BY fur
  HAVING MAX(height) < 1.3 * AVG(height) AND MIN(height) > 0.7 * AVG(height)
  ;

--HAVING 是 SQL 里的一个关键字，用于对分组后的结果进行筛选。

--详细解释
--WHERE 是在分组（GROUP BY）之前筛选行。
--HAVING 是在分组（GROUP BY）之后，对每一组的聚合结果（比如 MAX、MIN、AVG）进行筛选。

--DISTINCT 是 SQL 里的一个关键字，用于从查询结果中去除重复的行。
--在这个查询中，DISTINCT 用于确保每种毛发类型（fur）只出现一次。

--GROUP BY 是 SQL 里的一个关键字，用于将查询结果按指定的列进行分组。
--在这个查询中，GROUP BY fur 将 dogs 表中的数据按毛发类型进行分组。
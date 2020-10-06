# SQL



### 1. 준비 단계

- tutorial 이라는 SQLite 파일 생성

```sqlite
sqlite3 tutorial.sqlite3
```

- 외부 데이터를 참고할 때?
  - CSV 파일을 가지고 와서 examples라는 table로 만들기

```sqlite
sqlite>.mode csv
sqlite>.import hellodb.csv examples
```

- 깔끔하게 보고 싶을 때?
  - headers on 사용하기
  - .mode column 사용하기

```sqlite
sqlite>.headers on
sqlite>SELECT * FROM examples;
```

```sqlite
id,first_name,last_name,age,country,phone
1,"길동","홍",600,"충청도",010-2424-1232
```



```sqlite
sqlite>.mode column
sqlite>SELECT * FROM examples;
```

```sqlite
id  first_name  last_name  age  country  phone
--  ----------  ---------  ---  -------  -------------
1   길동          홍          600  충청도      010-2424-1232
```



### 2. 만들어보자

> Datatype에는 INTEGER, TEXT, REAL, NUMERIC, BLOB 등이 있다.

#### 1. table 생성

```sqlite
sqlite>CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );
```

- id는 숫자, name은 문자로 이루어진 classmates라는 table 생성



#### 2. Table 조회: .tables

```sqlite
sqlite>.tables
```

```sqlite
classmates  examples
```



#### 3. Schema 조회: .schema (table name)

```sqlite
sqlite>.schema classmates
```

```sqlite
CREATE TABLE classmates(
id INTEGER PRIMARY KEY,
name TEXT
);
```



#### 4. 테이블 이름 변경

```sqlite
sqlite> ALTER TABLE classmates RENAME TO school;
```



#### 5. 새로운 컬럼 추가

- 새롭게 행을 추가할 때는 default 값을 넣어주어야 한다.

```sqlite
sqlite> ALTER TABLE news ADD COLUMN created_at TEXT NOT NULL;
Error: Cannot add a NOT NULL column with default value NULL
```

- 디폴트 값 추가 

```sqlite
sqlite> ALTER TABLE school
   ...> ADD COLUMN subtitle TEXT NOT NULL DEFAULT 1;
```



#### 6. Table 삭제(DROP): DROP TABLE (table);

```sqlite
sqlite>DROP TABLE school;
sqlite>.tables
```

```sqlite
examples
```



#### 7. 지웠으니 다시 만들자...만들고 나선 제대로 만들어졌는지 확인!

```sqlite
sqlite>CREATE TABLE classmates (
   ...> name TEXT,
   ...> age INT,
   ...> address TEXT
   ...> );
sqlite>.schema classmates
CREATE TABLE classmates (
name TEXT,
age INT,
address TEXT
);
```



#### 8. Table의 내용을 넣어보자(INSERT)

1. 이름이랑 나이만!

```sqlite
sqlite>INSERT INTO classmates (name, age)
   ...> VALUES ('오민택', 27);
sqlite>SELECT * FROM classmates;
name  age  address
----  ---  ------
오민택   27
```

2. 주소까지 넣어보자.

```sqlite
sqlite>INSERT INTO classmates (name, age, address)
   ...> VALUES ('아이유', 28, '서울');
sqlite>SELECT * FROM classmates;
name  age  address
----  ---  ------
오민택   27
아이유   28   서울
```

3. 그냥 적어도 된다.

```sqlite
sqlite>INSERT INTO classmates
   ...> VALUES ('아이유', 28, '서울')
```

4. id까지 표시하고 싶으면?

```sqlite
sqlite>SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  ------
1      오민택   27
2      아이유   28   서울
3      아이유   28   서울
```

5. 4번에서 1번의 주소가 없는데 필요한 정보라면 비워두면 안된다. 공백 없이 새로 만들어보자

```sqlite
sqlite>CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
sqlite>.schema classmates
CREATE TABLE classmates (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);
```

6. 여기에서 인자를 하나 빼고 넣으면?

```sqlite
sqlite> INSERT INTO classmates
   ...> VALUES ('아이유', 28, '서울');
Error: table classmates has 4 columns but 3 values were supplied
```

7. 해결 방법 1

```sqlite
sqlite> INSERT INTO classmates (name, age, address)
   ...> VALUES ('아이유', 28, '서울');
sqlite> SELECT * FROM classmates;
id  name  age  address
--  ----  ---  -------
1   아이유   28   서울
```

8. 해결 방법 2

```sqlite
sqlite>INSERT INTO classmates 
   ...> VALUES (2, '아이유', 28, '서울');
sqlite> SELECT * FROM classmates;
id  name  age  address
--  ----  ---  -------
1   아이유   28   서울
2   아이유   28   서울
```

※ 이렇게 하면 id 값을 매번 신경써줘야 하니깐 rowid를 사용하자!

9. rowid 사용해서 만들기

```sqlite
sqlite> DROP TABLE classmates;
sqlite> CREATE TABLE classmates (
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
sqlite> .tables
classmates  examples
sqlite> .schema classmates
CREATE TABLE classmates (
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);
```

10. 내용 넣기

```sqlite
sqlite> INSERT INTO classmates VALUES ('오민택', 27, '구미'),
   ...> ('김민수', 26, '광주'), ('이지은', 28, '서울'), ('정소민', 27, '부산');
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
오민택   27   구미
김민수   26   광주
이지은   28   서울
정소민   27   부산
sqlite> SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      오민택   27   구미
2      김민수   26   광주
3      이지은   28   서울
4      정소민   27   부산
```



#### 9. Table의 내용 삭제(DELETE)

- data 삭제(DELETE): DELETE FROM table WHERE condition;
- 무엇을 기준으로 삭제할까? -> 중복이 불가능한 Unique한 값!
- rowid로 삭제하자: DELETE FROM table WHERE rowid=?;

```sqlite
sqlite> DELETE FROM classmates WHERE rowid=4;
sqlite> SELECT * FROM classmates;
name  age  address
----  ---  -------
오민택   27   구미
김민수   26   광주
이지은   28   서울
```

- SQLite는 기본적으로 이전에 삭제 된 행의 값을 재사용한다.

```sqlite
sqlite> INSERT INTO classmates VALUES ('이주원', 27, '대구');
sqlite> SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      오민택   27   구미
2      김민수   26   광주
3      이지은   28   서울
4      이주원   27   대구
```

- 이전에 삭제 된 행의 값을 재사용하지 않고 사용하지 않은 다음 행 값으로 사용하게 하려면?
  - AUTOINCREMENT를 사용(django에서는 기본적으로 사용)
  - django에서는 삭제된 행위 자체를 중요하게 생각하기 때문에 비워둔다.

#### 10. 데이터 수정

- id가 4인 레코드에서 이름을 이대호, 주소를 부산으로 바꾸자

```sqlite
sqlite> UPDATE classmates SET name='이대호', address='부산'
   ...> WHERE rowid=4;
sqlite> SELECT rowid, * FROM classmates;
rowid  name  age  address
-----  ----  ---  -------
1      오민택   27   구미
2      김민수   26   광주
3      이지은   28   서울
4      이대호   27   부산
```



#### 11. Table의 내용을 조건대로 조회하기(SELECT)

1. 이름만 조회하자

```sqlite
sqlite> SELECT rowid, name FROM classmates;
rowid  name
-----  ----
1      오민택
2      김민수
3      이지은
4      이주원
```

2. 1번의 이름만 가져오려면?
   - LIMIT를 사용!

```sqlite
sqlite> SELECT rowid, name FROM classmates LIMIT 1;
rowid  name
-----  ----
1      오민택
```

3. 그럼 3번을 불러오려면 LIMIT 3?

```sqlite
sqlite> SELECT rowid, name FROM classmates LIMIT 3;
rowid  name
-----  ----
1      오민택
2      김민수
3      이지은
```

4. OFFSET을 사용해보자

```sqlite
sqlite> SELECT rowid, name FROM classmates LIMIT 1
   ...> OFFSET 2;
rowid  name
-----  ----
3      이지은
```

5. 주소가 서울인 사람만 가져오려면?
   - WHERE 사용!

```sqlite
sqlite> SELECT rowid, name FROM classmates
   ...> WHERE address='서울';
rowid  name
-----  ----
3      이지은
```

6. Table에서 특정 column 값을 중복없이 가져와보자
   - SELECT DISTINCT column FROM table;
   - rowid에는 사용 불가능

```sqlite
sqlite> SELECT DISTINCT age FROM classmates;
sqlite> age
---
27
26
28
```

7. 나이가 27 이상인 사람만 가져온다면?

```sqlite
sqlite> SELECT * FROM users WHERE age >= 27;
rowid  name  age  address
-----  ----  ---  -------
1      오민택   27   구미
3      이지은   28   서울
4      이대호   27   부산
```

8. 레코드의 개수를 반환: COUNT(column)

```sqlite
sqlite> SELECT count(*) FROM users;
```

9. 숫자일 때만 가능한 method
   - AVG(), SUM(), MIN(), MAX()
   - 30살 이상인 사람들의 평균 나이는?

```sqlite
sqlite> SELECT AVG(age) FROM users WHERE age>=30;
```

10. LIKE(wild card)

    1. `_ `: 반드시 이 자리에 한 개의 문자가 존재해야 한다.
       1. `1_ _ _` : 1로 시작하고 4자리인 값
    2. `%` : 이 자리에 문자열이 있을수도, 없을수도 있다.
       1. `2%` : 2로 시작하는 값
       2. `%2` : 2로 끝나는 값
       3. `%2%` : 2가 들어가는 값
    3. 둘 다 활용
       1. `_2%` : 아무 값이나 들어가고 두 번째가 2로 시작하는 값
       2. `2_%_%`/`2_ _%` : 2로 시작하고 적어도 3자리인 값

    - users에서 20대인 사람은?

    - ```sqlite
      sqlite> SELECT * FROM users WHERE age LIKE '2_';
      ```

    - 이름이 준으로 끝나는 사람은?

    - ```sqlite
      sqlite> SELECT * FROM users WHERE first_name LIKE '%준';
      ```

11. 정렬해보자(ORDER)

    - ORDER BY col1, col2 ASC|DESC;(오름/내림차순)

    - 나이 순으로 오름차순 상위 10명?

    - ```sqlite
      sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;
      ```

    - 나이순, 성 순으로 오름차순 상위 10명?

    - ```sqlite
      sqlite> SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
      ```

12. 그룹을 만들어보자(GROUP BY)

    - 지정된 기준에 따라 행 세트를 그룹으로 결합, 데이터를 요약하는 상황에 주로 사용
    - 각 성씨가 몇 명씩 있는지 조회

```sqlite
sqlite> SELECT last_name, COUNT(*) FROM users
   ...> GROUP BY last_name;
```


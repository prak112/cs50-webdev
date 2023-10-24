# Contents
 - [Overview](#overview)
 - [Fundamentals](#fundamentals)
 - [SQLite](#sqlite)
    - [Syntax](#syntax)
    - [Workflow](#workflow)
    - [Working in Command Line](#working-in-command-line)
    - [JOIN tables](#join-tables)
- [Possible Issues](#possible-issues)
    - [SQL Injection](#sql-injection)
    - [Race Conditions](#race-conditions)


<br>
<hr>

# Overview
- To learn Database essentials in *SQLite*, *Django Models*, managing table relationships and *Django Admin*
- CS50W Notes on [Lecture 4 - SQL, Models and Migrations](https://cs50.harvard.edu/web/2020/notes/4/)

# Fundamentals
- Forms of databases - 
    - **Relational Databases** - for structured or tabulated data
    - **NoSQL** - for non-structured data
- Most popular forms of **Relational Databases** : *MySQL*, *PostgreSQL(Postgres)*, *SQLite*
- *SQLite* stores data as a single file instead of database servers as in *MySQL*, *Postgres* or *Microsoft SQL Server*
- *SQLite* also happends to be *Django's* default database
- Data types supported by *SQLite* :
    - Text
    - Numeric - any kind of data including numbers, such as dates, boolean values, etc.
    - Integer
    - Real - floats and decimals
    - BLOB (Binary Large OBject) - pure binary data of audio, images or videos

- Column constraints for database design and data integrity :

<table border>
    <th>Constraint</th>
    <th>Description</th>
    <th>Example (part of <code>CREATE TABLE</code> query syntax)</th>
    <tr>
        <td><b>PRIMARY KEY</b></td>
        <td>to uniquely identify each row in the table</td>
        <td><code>id INTEGER PRIMARY KEY</code></td>
    </tr>
    <tr>
        <td><b>AUTOINCREMENT</b></td>
        <td>to automate unique value generation for each row</td>
        <td><code>id INTEGER PRIMARY KEY AUTOINCREMENT</code></td>
    </tr>
    <tr>
        <td><b>NOT NULL</b></td>
        <td>to ensure column cannot have NULL values</td>
        <td><code>name TEXT NOT NULL</code></td>
    </tr>
    <tr>
        <td><b>UNIQUE</b></td>
        <td>to ensure unqueness of values in the column</td>
        <td><code>name TEXT UNIQUE</code></td>
    </tr>
    <tr>
        <td><b>CHECK</b></td>
        <td>to define a condition that column values must fulfill</td>
        <td><code>birthyear INTEGER CHECK(birthyear >= 1999)</code></td>
    </tr>
    <tr>
        <td><b>DEFAULT</b></td>
        <td>to set a default value when no value is provided</td>
        <td><code>gender TEXT DEFAULT "non-binary"</code></td>
    </tr>
    <tr>
        <td><b>REFERENCES</b></td>
        <td>to create foreign key relationship/s with other table/s</td>
        <td><code>user_id INTEGER REFERENCES Users(id)</code></td>
    </tr>
</table>

<br>

# SQLite
## Syntax
- Create table with columns
    ```sql
    CREATE TABLE users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname TEXT NOT NULL UNIQUE,
        birthyear INTEGER CHECK(birthyear >= 1900),
        gender TEXT DEFAULT "non-binary",
        email TEXT NOT NULL UNIQUE
    );
    ```

- Insert data into table columns
    ```sql
    INSERT INTO users
        (fullname, birthyear, gender, email)
        VALUES ("Rama Rao", 1960, "male", "ntr@dvsk.com");
    ```

- Read data from tables in the database
    ```sql
    SELECT * FROM users LIMIT 10; /* displays 10 rows with all columns
    ```

## Workflow
- SQL databases and tables can be managed in 2 ways :
1. **Command Line** ( *IDEAL, (my situation) but project and PATH directories mismatch* )
    - Go To [SQLite Download page](https://www.sqlite.org/download.html)
    - Download *sqlite-tools*
    - Set your system's PATH Environment Variables to *sqlite-tools* PATH
    - Build, manage, execute databases and tables from Command Line

2. **VS Code Extension** (*NOT IDEAL for learning fundamentals, maybe to build development workflow*)
    - Install 3rd-Party SQLite Extension by alexcvzz
    - Build, manage, execute databases and tables from VS Code

3. **Conda Virtual Environment** (*IDEAL, all in one place!*)
    - Create a virtual environment for Web Development with Python - 
        ```cmd
        conda create --name  py311-webdev
        ```
    - Activate the created virtual environment -
        ```cmd
        conda activate py311-webdev
        ```
    - Install *python 3.11* and other libraries including *sqlite3* required for development workflow - 
        ```cmd
        conda install sqlite3
        ```
    - Access sqlite3 and start creating and managing databases and tables -
        ```cmd
        sqlite3
        ```

## Working in Command Line
- `sqlite` runs as an application inside the terminal
- Tables can be created using the regular SQL syntax, 
    ```sql
    CREATE TABLE
    ...
    ```
- Default query output for the `users` table is as follows :
    ```sql
    sqlite> SELECT * FROM users;

    id|fullname|birthyear|email
    1|Pikachu|2023|pika@pokemon.com
    2|Charmander|2022|char@pokemon.com
    3|Squirtle|2021|squirtle@pokemon.com
    4|Bulbasaur|2018|bulba@pokemon.com
    5|Eevee|2015|eevee@pokemon.com
    6|Jigglypuff|2020|jiggly@pokemon.com
    ```
- To format the output, we execute the following :
    ```sql
    sqlite> .mode columns
    sqlite> .headers yes 
    ```
- Now the same query returns a formatted table, as follows :
    ```sql
    sqlite> SELECT * FROM users;

    id  fullname    birthyear  email
    --  ----------  ---------  --------------------
    1   Pikachu     2023       pika@pokemon.com
    2   Charmander  2022       char@pokemon.com
    3   Squirtle    2021       squirtle@pokemon.com
    4   Bulbasaur   2018       bulba@pokemon.com
    5   Eevee       2015       eevee@pokemon.com
    6   Jigglypuff  2020       jiggly@pokemon.com
    ```
- Once closed, the `sqlite` application returns to its default settings
- To open the `.sql` files created earlier :
    ```sql
    sqlite> .open users.sql
    sqlite> .tables
    users
    ```

## JOIN tables
- INNER JOIN 
    - displays the data between LEFT(`users`) and RIGHT(`roles`) tables where only the referenced columns have matching data
        ```sql
        sqlite> SELECT fullname, birthyear, role 
        ...>    FROM users JOIN roles
        ...>    ON users.id = roles.user_id;

        fullname    birthyear  role
        ----------  ---------  --------
        Bulbasaur   2018       Blogger
        Pikachu     2023       Blogger
        Charmander  2022       Gamer
        Jigglypuff  2020       Designer
        Eevee       2015       Designer
        ```

- LEFT OUTER JOIN
    - LEFT table - displays all data from LEFT table,
    - RIGHT table - displays only matched data with LEFT table column reference
        ```sql
            sqlite> SELECT * FROM users LEFT JOIN roles ON users.id = roles.user_id;

            id  fullname    birthyear  email               age  id  role      user_id
            --  ----------  ---------  ------------------  ---  --  --------  -------
            1   Pikachu     2023       pika@pokemon.com    0    3   Blogger   1
            2   Charmander  2022       char@pokemon.com    1    4   Gamer     2
            4   Bulbasaur   2018       bulba@pokemon.com   5    2   Blogger   4
            5   Eevee       2015       eevee@pokemon.com   8    6   Designer  5
            6   Jigglypuff  2020       jiggly@pokemon.com  3    5   Designer  6
            7   Squirtle    2015       squirt@pokemon.com  8
        ```

- RIGHT OUTER JOIN
    - LEFT table - displays only matched data with RIGHT table column reference,
    - RIGHT table - displays all data from RIGHT table
        ```sql
            sqlite> SELECT * FROM users RIGHT JOIN roles ON users.id = roles.user_id;
            id  fullname    birthyear  email               age  id  role      user_id
            --  ----------  ---------  ------------------  ---  --  --------  -------
            1   Pikachu     2023       pika@pokemon.com    0    3   Blogger   1
            2   Charmander  2022       char@pokemon.com    1    4   Gamer     2
            4   Bulbasaur   2018       bulba@pokemon.com   5    2   Blogger   4
            5   Eevee       2015       eevee@pokemon.com   8    6   Designer  5
            6   Jigglypuff  2020       jiggly@pokemon.com  3    5   Designer  6
                                                                1   Gamer     3        
        ```

- FULL OUTER JOIN
    - displays all data combined from LEFT and RIGHT tables either matched or unmatched
        ```sql
            sqlite> SELECT * FROM users FULL JOIN roles ON users.id = roles.user_id;

            id  fullname    birthyear  email               age  id  role      user_id
            --  ----------  ---------  ------------------  ---  --  --------  -------
            1   Pikachu     2023       pika@pokemon.com    0    3   Blogger   1
            2   Charmander  2022       char@pokemon.com    1    4   Gamer     2
            4   Bulbasaur   2018       bulba@pokemon.com   5    2   Blogger   4
            5   Eevee       2015       eevee@pokemon.com   8    6   Designer  5
            6   Jigglypuff  2020       jiggly@pokemon.com  3    5   Designer  6
            7   Squirtle    2015       squirt@pokemon.com  8
                                                                1   Gamer     3
        ```

# Possible Issues
## SQL Injection
- SQL query syntax if deployed in its raw form would lead to exposure to hackers
- For example, consider the following simple query for a user accessing the application :
    ```sql
    SELECT * FROM users WHERE username="pikachu" AND password="pika123";
    ```
- If a hacker wanted to gain access to application without logging in, they could just enter username as "hacker" --", which results in the following :
    ```sql
    SELECT * FROM users WHERE username="hacker"--" AND password="";
    ```
    - Here SQL is considering the query post "--" as a comment and hence provides access to the application
- Strategies to solve could be to use :
    - *Stored Procedures* in Database Management Systems
    - *Django Models* in Django


## Race Conditions
- Events happening on parallel threads could conflict database operations
- Locking database during a transaction until it is done, would be strategic
# Databases

## Fundamentals
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

## SQLite syntax
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



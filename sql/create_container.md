# Creation and execution of a MA SQL server in docker

<https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver16&pivots=cs1-bash> (Accessed 06-2023)

<https://hub.docker.com/_/microsoft-mssql-server>  

> For bash instructions

## Preliminary

* Create a `.env` file with the sensitive information. The syntax is `VAR="Value"`

* Read from .env file. In order to hide sensitive information

```bash
export $(cat .env | xargs)
```

## Pull and run the SQL Server Linux container image

* Pull the image from docker hub

```bash
docker pull mcr.microsoft.com/mssql/server:2022-latest
```

* Run the container. In this case the password declared in the .env file

```bash
docker run -e ACCEPT_EULA=Y -e MSSQL_SA_PASSWORD=$MY_SQL_PASS \
   -p 1433:1433 --name sql1 --hostname sql1 \
   -d mcr.microsoft.com/mssql/server:2022-latest
```

* View the container with `docker ps -a`  

* If needed, the error log of the server is in  

```bash
docker exec -t sql1 cat /var/opt/mssql/log/errorlog | grep connection
```

> **Important!**: For security improvements see links above.

## Connect to the SQL server

* Enter to the container

```bash
docker exec -it sql1 "bash"
```

* Inside the container, connect locally using **sqlcmd**

```sqlcmd
/opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P $MY_SQL_PASS
```

## Subsequent connections to the SQL server

* Outside the container, we must first enter into the cotainer and then to de sqlcmd terminal. It can be done in a single step. 

```bash
docker exec -it sql1 /opt/mssql-tools/bin/sqlcmd \
-S localhost \
-U SA \
-P $MY_SQL_PASS
```

## Create and query data

* Create a new database  

```sql
-- Warning, pasting multiple lines is not allowed in sql
-- Creates a new database
CREATE DATABASE TestDB;
-- Lists the existing databases. The natabase abose should appear
SELECT Name from sys.databases;
GO
```

* Insert data  

```sql
USE TestDB;
CREATE TABLE Inventory (id INT, name NVARCHAR(50), quantity INT);
INSERT INTO Inventory VALUES (1, 'banana', 150); INSERT INTO Inventory VALUES (2, 'orange', 154);
INSERT INTO Inventory VALUES (3, 'apple', 160); INSERT INTO Inventory VALUES (4, 'melon', 200);
GO
```

* Select the data

```sql
SELECT * FROM Inventory WHERE quantity > 152;
GO
```

* Exit the **sqlcmd** promt

```sql
QUIT
```

## Connect from outside the container

```bash
sqlcmd -S <ip_address>,1433 -U SA -P "<Password>"
```

## Remove the container

```bash
docker stop sql1
docker rm sql1
```

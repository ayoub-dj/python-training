import mysql.connector
from decimal import Decimal
from datetime import date


con = mysql.connector.connect(
  host="localhost",
  user="root",
  password="admin",
  database="mydb",
)

cr = con.cursor()

# sql = "create table employees (id int, name varchar(100), salary decimal(5, 2), hire_date date)"
# sql = "drop table members;"
# sql = "rename table employees to members;"
# sql = "alter table members rename column id to pk;"
# sql = "alter table members modify column name varchar(120)"
# sql = "INSERT INTO members (pk, name, salary, hire_date, email) VALUES (%s, %s, %s, %s, %s)"

# pk, name, salary, hire_date, email  = 2, 'James', Decimal('99.50'), date(2024, 8, 2), 'james@aol.com'

# cr.execute(sql, (pk, name, salary, hire_date, email))

# sql = 'delete from members where pk = 1;'

# sql = "INSERT INTO members (pk, name, salary, hire_date, email) VALUES (%s, %s, %s, %s, %s)"
# data = [
#     (1, 'James', 99.50, date(2024, 8, 2), 'james@example.com'),
#     (2, 'John', 150.75, date(2023, 10, 15), 'john@example.com'),
#     (3, 'Emily', 120.00, date(2022, 12, 5), 'emily@example.com'),
#     (4, 'Michael', 110.25, date(2023, 5, 20), 'michael@example.com'),
#     (5, 'Sophia', 135.80, date(2024, 3, 12), 'sophia@example.com')
# ]

# cr.executemany(sql, data)


# sql = "SELECT * FROM members;"


cr.execute("""CREATE TABLE IF NOT EXISTS Product (
            id INTEGER primary key auto_increment,
            product_name varchar(200) NOT NULL,
            price decimal(5, 2),
            description TEXT
           )
           """)

cr.execute("""CREATE TABLE IF NOT EXISTS ProductImage (
            id INTEGER primary key auto_increment,
            product_id INTEGER,
            image_url VARCHAR(255),
            FOREIGN KEY (product_id) REFERENCES Product(id)
           )
           """)
 
cr.execute("""CREATE TABLE IF NOT exists Category (
            id int primary key auto_increment,
            product_id INTEGER,
            name varchar(200),
            FOREIGN KEY (product_id) REFERENCES Product(id)
           )
           """)

# sql = "INSERT INTO Product (product_name, price, description) VALUES (%s, %s, %s)"

# product_name, price, description = 'Smartphone', Decimal(599.99), 'A powerful smartphone with advanced features.'

# cr.execute(sql, (product_name, price, description))

# sql = "INSERT INTO ProductImage (product_id, image_url) VALUES (%s, %s)"
# data = [
#     (1, 'https://example.com/product1-image1.jpg'),
#     (1, 'https://example.com/product1-image2.jpg'),
#     (1, 'https://example.com/product1-image3.jpg'),
#     (1, 'https://example.com/product1-image4.jpg')
# ]

# cr.executemany(sql, data)

# phones
# sql = "INSERT INTO Category (product_id, name) VALUES (1, 'Phones')"

# cr.execute(sql)

con.commit()
# cr.close()
# con.close()

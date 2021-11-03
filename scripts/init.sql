DROP DATABASE IF EXISTS sql11445855;
CREATE DATABASE sql11445855;
USE sql11445855;

DROP TABLE IF EXISTS Products;
CREATE TABLE Products (product_id INTEGER AUTO_INCREMENT, owner_id INTEGER, name TINYTEXT, description MEDIUMTEXT, price INTEGER, state INTEGER, image LONGBLOB, category_id INTEGER, PRIMARY KEY (product_id));
INSERT INTO Products (owner_id, name, price) VALUES (1, "Product1", 20);
INSERT INTO Products (owner_id, name, price) VALUES (2, "Product2", 200);
INSERT INTO Products (owner_id, name, price) VALUES (1, "Product3", 290);

DROP TABLE IF EXISTS Users;
CREATE TABLE Users (user_id INTEGER AUTO_INCREMENT, username TINYTEXT, password MEDIUMTEXT, admin BOOLEAN, mail MEDIUMTEXT, location MEDIUMTEXT, userphoto LONGBLOB, PRIMARY KEY (user_id));
INSERT INTO Users (username, password, admin, mail, location) VALUES ("test", "1234", 1, "test@gmail.com", "Barcelona");

DROP TABLE IF EXISTS ProductsFollowing;
CREATE TABLE ProductsFollowing (product_id INTEGER, user_id INTEGER);

DROP TABLE IF EXISTS Category;
CREATE TABLE IF NOT EXISTS Category (category_id INTEGER AUTO_INCREMENT, name TINYTEXT, PRIMARY KEY (category_id));

INSERT INTO Category (name) VALUES ("Cars");
INSERT INTO Category (name) VALUES ("Bikes");
INSERT INTO Category (name) VALUES ("Home");
INSERT INTO Category (name) VALUES ("Toys");
INSERT INTO Category (name) VALUES ("Sports");
INSERT INTO Category (name) VALUES ("Phones");

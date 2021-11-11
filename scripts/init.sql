DROP DATABASE IF EXISTS sql11445855;
CREATE DATABASE sql11445855;
USE sql11445855;

DROP TABLE IF EXISTS Products;
CREATE TABLE Products (product_id INTEGER AUTO_INCREMENT, owner_id INTEGER NOT NULL, name TINYTEXT NOT NULL, description MEDIUMTEXT, price INTEGER NOT NULL, state INTEGER NOT NULL, image LONGBLOB, category_id INTEGER NOT NULL, PRIMARY KEY (product_id));
INSERT INTO Products (owner_id, name, price) VALUES (1, "Product1", 20);
INSERT INTO Products (owner_id, name, price) VALUES (2, "Product2", 200);
INSERT INTO Products (owner_id, name, price) VALUES (1, "Product3", 290);

DROP TABLE IF EXISTS Users;
CREATE TABLE Users (user_id INTEGER AUTO_INCREMENT, username TINYTEXT NOT NULL, password MEDIUMTEXT NOT NULL, admin BOOLEAN NOT NULL, mail MEDIUMTEXT NOT NULL, location MEDIUMTEXT, userphoto LONGBLOB, PRIMARY KEY (user_id));
INSERT INTO Users (username, password, admin, mail, location) VALUES ("test", "1234", 1, "test@gmail.com", "Barcelona");

DROP TABLE IF EXISTS ProductsFollowing;
CREATE TABLE ProductsFollowing (product_id INTEGER NOT NULL, user_id INTEGER NOT NULL);

DROP TABLE IF EXISTS Category;
CREATE TABLE IF NOT EXISTS Category (category_id INTEGER AUTO_INCREMENT, name TINYTEXT, PRIMARY KEY (category_id));

DROP TABLE IF EXISTS Chat;
CREATE TABLE IF NOT EXISTS Chat (chat_id INTEGER AUTO_INCREMENT, seller_id INTEGER NOT NULL, buyer_id INTEGER NOT NULL, PRIMARY KEY (chat_id));

DROP TABLE IF EXISTS Messages;
CREATE TABLE IF NOT EXISTS Messages (message_id INTEGER AUTO_INCREMENT, sender_id INTEGER NOT NULL, message MEDIUMTEXT NOT NULL, PRIMARY KEY (message_id));

INSERT INTO Category (name) VALUES ("Cars");
INSERT INTO Category (name) VALUES ("Bikes");
INSERT INTO Category (name) VALUES ("Home");
INSERT INTO Category (name) VALUES ("Toys");
INSERT INTO Category (name) VALUES ("Sports");
INSERT INTO Category (name) VALUES ("Phones");

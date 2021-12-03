DROP TABLE IF EXISTS Products;
CREATE TABLE Products (product_id INTEGER AUTO_INCREMENT, owner_id INTEGER NOT NULL, name TINYTEXT NOT NULL, description MEDIUMTEXT, price INTEGER NOT NULL, state INTEGER NOT NULL, image TINYTEXT, category_id INTEGER NOT NULL, buyed INTEGER NOT NULL, buyer_id INTEGER, PRIMARY KEY (product_id));

DROP TABLE IF EXISTS Users;
CREATE TABLE Users (user_id INTEGER AUTO_INCREMENT, username TINYTEXT NOT NULL, password MEDIUMTEXT NOT NULL, admin BOOLEAN NOT NULL, mail MEDIUMTEXT NOT NULL, location MEDIUMTEXT, userphoto TINYTEXT, PRIMARY KEY (user_id));

DROP TABLE IF EXISTS ProductsFollowing;
CREATE TABLE ProductsFollowing (product_id INTEGER NOT NULL, user_id INTEGER NOT NULL);

DROP TABLE IF EXISTS Ratings;
CREATE TABLE Ratings (product_id INTEGER NOT NULL, user_id INTEGER NOT NULL, buyer_id INTEGER NOT NULL, rating INTEGER NOT NULL);

DROP TABLE IF EXISTS Category;
CREATE TABLE IF NOT EXISTS Category (category_id INTEGER AUTO_INCREMENT, name TINYTEXT, PRIMARY KEY (category_id));

INSERT INTO Category (name) VALUES ("Cars");
INSERT INTO Category (name) VALUES ("Bikes");
INSERT INTO Category (name) VALUES ("Toys");
INSERT INTO Category (name) VALUES ("Home");
INSERT INTO Category (name) VALUES ("Sports");
INSERT INTO Category (name) VALUES ("Technology");
INSERT INTO Category (name) VALUES ("Videogames");
INSERT INTO Category (name) VALUES ("Clothes");
INSERT INTO Category (name) VALUES ("Plants");
INSERT INTO Category (name) VALUES ("Books & Music");
INSERT INTO Category (name) VALUES ("Cinema");
INSERT INTO Category (name) VALUES ("Pet adoption");

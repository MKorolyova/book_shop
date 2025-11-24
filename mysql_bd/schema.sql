-- Creating the Books table
CREATE TABLE Genre (
    genre_id INTEGER NOT NULL,
    genre  VARCHAR(50) NOT NULL,
    description TEXT,
    PRIMARY KEY (genre_id)
);
CREATE TABLE Books (
    book_id INTEGER NOT NULL,
    author_name VARCHAR(255),
    book_name VARCHAR(255),
    price NUMERIC(6,2),                 
    publication_year INTEGER,           
    publication_city VARCHAR(255),
    genre_id  INTEGER NOT NULL,
    genre TEXT,
    description TEXT,
    author_info TEXT,
    review TEXT,
    PRIMARY KEY (book_id),
    FOREIGN KEY (genre_id) REFERENCES Genre(genre_id)
);

--  Creating the Storage table
CREATE TABLE Storage (
    book_id INTEGER NOT NULL,
    floor_number INTEGER NOT NULL,
    aisle INTEGER NOT NULL,
    shelf INTEGER NOT NULL,
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Creating the Customers table
CREATE TABLE Customers (
    customer_id INTEGER NOT NULL,
    password VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL CHECK (email LIKE '%@%'), 
    PRIMARY KEY (customer_id),
    UNIQUE (password)
);

-- Creating the Orders table
CREATE TABLE Orders (
    order_id INTEGER NOT NULL,
    customer_id INTEGER NOT NULL, 
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    address VARCHAR(255) ,
    postal_zip VARCHAR(10),
    city VARCHAR(50),
    country VARCHAR(50),
    total NUMERIC(6,2),
    create_date DATE NOT NULL,
    update_date DATE NOT NULL,
    status VARCHAR(10) DEFAULT 'inprocess' CHECK (status IN ('inprocess', 'complete')) NOT NULL,
    shipment_date DATE,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- Creating the Order_item table
CREATE TABLE Order_item (
    order_item_id INTEGER NOT NULL,  
    order_id INTEGER NOT NULL, 
    book_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    price NUMERIC(6,2) NOT NULL,
    PRIMARY KEY (order_item_id),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);


-- Trigger to update order total after new order item was added
DELIMITER //
CREATE TRIGGER update_order_total AFTER INSERT ON Order_item FOR EACH ROW
BEGIN
    UPDATE Orders
    SET total = total + (NEW.quantity * NEW.price)
    WHERE order_id = NEW.order_id;
END//

DELIMITER ;

SHOW TRIGGERS;

DROP TRIGGER IF EXISTS update_order_total;


-- Inserting data into the Customers table
INSERT INTO Customers (customer_id, password, email)
VALUES
  (1, '1bd2book', 'johndoe@example.com'),
  (2, '123456789jane', 'janesmith@example.com'),
  (3, 'michael_2005', 'michaeljohnson@example.com');

  
-- Inserting data into the Orders table
INSERT INTO Orders (order_id, customer_id, first_name, last_name, address, postal_zip, city, country, total, create_date, update_date, status)
VALUES
  (1, 1, 'John', 'Doe', '123 Main St', '12345', 'Anytown', 'USA', 0, '2023-11-22', '2023-11-22', 'complete'),
  (2, 3, 'Jane', 'Smith', '456 Elm St', '67890', 'Othertown', 'USA', 0, '2023-11-23', '2023-11-23', 'inprocess'),
  (3, 3, 'Michael', 'Johnson', '789 Oak St', '13579', 'Sometown', 'USA', 0, '2023-11-24', '2023-11-24', 'inprocess');

-- Inserting data into the Order_item table
INSERT INTO Order_item (order_item_id, order_id, book_id, quantity, price)
VALUES
  (1, 1, 158632962, 2, 14.99),
  (2, 2, 158632962, 1, 29.99),
  (3, 3, 158632962, 1, 19.99);


-- Inserting sample genres into Genre table
INSERT INTO Genre (genre_id, genre, description)
VALUES
  (1, 'Fiction', 'Literary works invented by the imagination'),
  (2, 'Non-Fiction', 'Factual books, biographies, history, science, etc.'),
  (3, 'Sci-Fi', 'Science fiction, futuristic or speculative stories'),
  (4, 'Fantasy', 'Magical or fantastical stories'),
  (5, 'Mystery', 'Stories involving crime or investigation');


-- Inserting 10 books into Books table
INSERT INTO Books (book_id, author_name, book_name, price, publication_year, publication_city, genre_id, genre, description, author_info, review)
VALUES
  (1, 'George Orwell', '1984', 15.99, 1949, 'London', 1, 'Fiction', 'Dystopian novel', 'George Orwell was an English novelist.', 'Excellent'),
  (2, 'J.K. Rowling', 'Harry Potter and the Sorcerer''s Stone', 12.99, 1997, 'London', 1, 'Fiction', 'Fantasy novel', 'British author, best known for Harry Potter series.', 'Amazing'),
  (3, 'Isaac Asimov', 'Foundation', 14.50, 1951, 'New York', 3, 'Sci-Fi', 'Science fiction series', 'Isaac Asimov was an American writer.', 'Outstanding'),
  (4, 'F. Scott Fitzgerald', 'The Great Gatsby', 10.99, 1925, 'New York', 1, 'Fiction', 'Classic novel about the Jazz Age', 'F. Scott Fitzgerald was an American novelist.', 'Excellent'),
  (5, 'Yuval Noah Harari', 'Sapiens', 19.99, 2011, 'Jerusalem', 2, 'Non-Fiction', 'A Brief History of Humankind', 'Historian and author.', 'Very Informative'),
  (6, 'Mary Shelley', 'Frankenstein', 9.99, 1818, 'London', 1, 'Fiction', 'Gothic novel', 'Mary Shelley was an English novelist.', 'Classic'),
  (7, 'J.R.R. Tolkien', 'The Hobbit', 13.99, 1937, 'London', 1, 'Fiction', 'Fantasy adventure novel', 'English writer, poet, and philologist.', 'Excellent'),
  (8, 'Douglas Adams', 'The Hitchhiker''s Guide to the Galaxy', 11.50, 1979, 'London', 3, 'Sci-Fi', 'Science fiction comedy', 'English author and humorist.', 'Hilarious'),
  (9, 'Ernest Hemingway', 'The Old Man and the Sea', 8.99, 1952, 'New York', 1, 'Fiction', 'Short novel', 'American novelist.', 'Excellent'),
  (10, 'Stephen Hawking', 'A Brief History of Time', 16.99, 1988, 'Cambridge', 2, 'Non-Fiction', 'Cosmology book', 'English theoretical physicist.', 'Very Informative');

-- Author Table
CREATE TABLE author (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(50) NOT NULL
);

-- Publisher Table
CREATE TABLE publisher (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    location VARCHAR(255),
    email VARCHAR(100)
);

-- Book Table
CREATE TABLE book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    publication_year INT,
    genre VARCHAR(50),
    publisher_id INT,
    page_count INT,
    language VARCHAR(50),
    edition INT,
    synopsis TEXT,
    FOREIGN KEY (publisher_id) REFERENCES publisher(id)
);

-- Book-Author Relationship Table
CREATE TABLE book_author (
    book_id INT,
    author_id INT,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES book(id),
    FOREIGN KEY (author_id) REFERENCES author(id)
);

-- Copy Table (to track individual copies of each book)
CREATE TABLE book_copy (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    barcode VARCHAR(20) UNIQUE NOT NULL,
    status ENUM('Available', 'Borrowed', 'Missing') DEFAULT 'Available' NOT NULL,
    FOREIGN KEY (book_id) REFERENCES book(id)
);

-- Visitor Table
CREATE TABLE visitor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    middle_name VARCHAR(50),
    last_name VARCHAR(50) NOT NULL,
    contact_email VARCHAR(100),
    registration_date DATE
);

-- Library Card Table
CREATE TABLE library_card (
    id INT AUTO_INCREMENT PRIMARY KEY,
    card_number VARCHAR(20) UNIQUE NOT NULL,
    visitor_id INT,
    member_type ENUM('Student', 'Teacher') NOT NULL,
    issue_date DATE,
    expiration_date DATE,
    FOREIGN KEY (visitor_id) REFERENCES visitor(id)
);

-- Borrowed Table (Junction Table for Many-to-Many Relationship)
CREATE TABLE borrowed (
    id INT AUTO_INCREMENT PRIMARY KEY,
    book_copy_id INT,
    library_card_id INT,
    borrowed_date DATE,
    returned_date DATE,
    FOREIGN KEY (book_copy_id) REFERENCES book_copy(id),
    FOREIGN KEY (library_card_id) REFERENCES library_card(id)
);

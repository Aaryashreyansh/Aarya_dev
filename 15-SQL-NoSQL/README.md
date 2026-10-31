# 15. SQL and NoSQL
SQL topics: tables, rows, primary/foreign keys, SELECT, WHERE, JOIN, indexes and transactions.

NoSQL topics: document, key-value, wide-column and graph models; consistency and access patterns.

## Safe SQL exercise
    CREATE TABLE services (
      id INTEGER PRIMARY KEY,
      name VARCHAR(100) NOT NULL,
      status VARCHAR(30) NOT NULL
    );
    INSERT INTO services (id, name, status)
    VALUES (1, 'demo-api', 'healthy');
    SELECT name, status FROM services;

Use a local practice database. Learn parameterized queries; do not concatenate untrusted input into SQL.
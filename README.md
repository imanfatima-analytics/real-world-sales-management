

# Real-World Sales Management & Business Analytics

## Project Overview

This project is an end-to-end **Sales Management and Business Analytics solution** developed using **PostgreSQL and Python**.

The project simulates a real-world business environment in which raw sales data is transformed into a structured relational database, validated for data quality, analyzed using SQL, and further processed with Python and Pandas to generate actionable business insights.

The complete analytical workflow follows:

**Raw Data → Data Profiling → Data Cleaning → Entity Identification → Schema Design → PostgreSQL Database → Data Validation → SQL Analysis → Advanced SQL → Views & Indexes → Python Integration → Pandas Analysis → KPI Development → Business Insights**

The project demonstrates practical skills in **relational database design, SQL analytics, data validation, database optimization, Python integration, and business intelligence**.

---

# Business Problem

A company needs a reliable analytical system to understand its sales performance across multiple business dimensions, including:

* Customers
* Products
* Product categories
* Brands
* Cities and regions
* Sales channels
* Order statuses
* Payment methods
* Payment activity
* Sales trends

The objective is to transform transactional sales data into meaningful information that can support **data-driven business decisions**.

### Key Business Questions

The analysis is designed to answer questions such as:

* Which products generate the highest revenue?
* Which product categories perform best?
* Which customers contribute the most revenue?
* Which cities generate the highest sales?
* Which sales channel performs best?
* What is the Average Order Value (AOV)?
* How do sales change month over month?
* Which products have the highest quantity sold?
* What is the distribution of order statuses?
* Which payment methods are used most frequently?
* Which products and categories generate the highest profit?
* Which customers represent the highest-value segment?

---

# Project Objectives

The primary objectives of this project are to:

1. Design a structured and normalized relational database.
2. Import external CSV data into PostgreSQL.
3. Profile and clean the source data.
4. Identify business entities and relationships.
5. Define primary keys and foreign-key relationships.
6. Validate data quality and referential integrity.
7. Perform exploratory and business analysis using SQL.
8. Apply advanced SQL techniques for analytical queries.
9. Use CTEs and subqueries to solve complex business problems.
10. Apply window functions for ranking and trend analysis.
11. Create reusable SQL views for reporting.
12. Add indexes to improve query performance.
13. Connect PostgreSQL with Python.
14. Retrieve and process database data using Pandas.
15. Calculate important business KPIs.
16. Perform customer, product, category, geographic, and sales-channel analysis.
17. Implement Python logging, testing, and exception handling.
18. Generate actionable business recommendations from analytical findings.

---

# Technologies Used

## Database & Data Management

* **PostgreSQL**
* **pgAdmin 4**
* **SQL**

## SQL Concepts

The project demonstrates practical implementation of:

* `SELECT`
* `WHERE`
* `ORDER BY`
* `GROUP BY`
* Aggregate Functions
* `CASE`
* `INNER JOIN`
* `LEFT JOIN`
* Subqueries
* Common Table Expressions (CTEs)
* Window Functions
* `RANK()`
* `ROW_NUMBER()`
* `DENSE_RANK()`
* Running Totals
* Views
* Indexes
* Primary Keys
* Foreign Keys
* Referential Integrity
* Data Validation
* Relational Database Design

## Python

* **Python**
* **Pandas**
* **SQLAlchemy**
* **psycopg2**
* **Pytest**
* **Logging**
* **Exception Handling**

---

# Database Architecture

## Database Name

```text
real_world_sales
```

The database is structured around five core relational tables:

1. `customers`
2. `products`
3. `orders`
4. `order_items`
5. `payments`

The schema separates customer, product, order, order-line, and payment information to reduce data redundancy and maintain data integrity.

---

# Database Schema

## 1. Customers

The `customers` table stores customer master information.

### Columns

| Column          | Description                |
| --------------- | -------------------------- |
| `customer_id`   | Unique customer identifier |
| `customer_name` | Customer's name            |
| `email`         | Customer email address     |
| `city`          | Customer city              |
| `region`        | Customer region            |

**Primary Key:**

```text
customer_id
```

---

## 2. Products

The `products` table stores product master data and pricing information.

### Columns

| Column         | Description               |
| -------------- | ------------------------- |
| `product_id`   | Unique product identifier |
| `product_name` | Product name              |
| `category`     | Product category          |
| `brand`        | Product brand             |
| `unit_price`   | Selling price per unit    |
| `cost_price`   | Product cost              |

**Primary Key:**

```text
product_id
```

The difference between `unit_price` and `cost_price` can also be used to analyze product-level profitability.

---

## 3. Orders

The `orders` table stores information about customer orders.

### Columns

| Column          | Description                                |
| --------------- | ------------------------------------------ |
| `order_id`      | Unique order identifier                    |
| `customer_id`   | Customer who placed the order              |
| `order_date`    | Date of order                              |
| `order_status`  | Current order status                       |
| `sales_channel` | Channel through which the order was placed |
| `shipping_city` | Order delivery city                        |

**Primary Key:**

```text
order_id
```

**Foreign Key:**

```text
customer_id → customers.customer_id
```

This establishes a **one-to-many relationship** between customers and orders.

---

## 4. Order Items

The `order_items` table stores the individual products contained within each order.

### Columns

| Column          | Description                  |
| --------------- | ---------------------------- |
| `order_item_id` | Unique order-line identifier |
| `order_id`      | Associated order             |
| `product_id`    | Purchased product            |
| `quantity`      | Number of units purchased    |
| `unit_price`    | Selling price per unit       |
| `discount_pct`  | Discount percentage applied  |

**Primary Key:**

```text
order_item_id
```

**Foreign Keys:**

```text
order_id → orders.order_id
product_id → products.product_id
```

This table acts as the transactional **order-line table**, connecting orders with products.

---

## 5. Payments

The `payments` table stores payment transactions associated with customer orders.

### Columns

| Column           | Description               |
| ---------------- | ------------------------- |
| `payment_id`     | Unique payment identifier |
| `order_id`       | Associated order          |
| `payment_date`   | Date of payment           |
| `payment_method` | Payment method used       |
| `payment_status` | Payment status            |
| `amount`         | Payment amount            |

**Primary Key:**

```text
payment_id
```

**Foreign Key:**

```text
order_id → orders.order_id
```

---

# Database Relationships

The relational structure can be represented as follows:

```text
                    ┌──────────────┐
                    │  CUSTOMERS   │
                    │──────────────│
                    │ customer_id  │
                    │ customer_name│
                    │ city         │
                    │ region       │
                    └──────┬───────┘
                           │
                         1 │
                           │
                         Many
                           │
                    ┌──────▼───────┐
                    │    ORDERS    │
                    │──────────────│
                    │ order_id     │
                    │ customer_id  │
                    │ order_date   │
                    │ order_status │
                    │ sales_channel│
                    └───┬──────┬───┘
                        │      │
                      1 │      │ 1
                        │      │
                     Many     Many
                        │      │
             ┌──────────▼─┐  ┌─▼───────────┐
             │ ORDER_ITEMS│  │  PAYMENTS   │
             │────────────│  │─────────────│
             │ order_item │  │ payment_id  │
             │ order_id   │  │ order_id    │
             │ product_id │  │ payment_date│
             │ quantity   │  │ method      │
             │ unit_price │  │ status      │
             │ discount   │  │ amount      │
             └──────┬─────┘  └─────────────┘
                    │
                  Many
                    │
                    │
                    │ 1
             ┌──────▼──────┐
             │  PRODUCTS   │
             │─────────────│
             │ product_id  │
             │ product_name│
             │ category    │
             │ brand       │
             │ unit_price  │
             │ cost_price  │
             └─────────────┘
```

### Relationship Summary

| Relationship           | Cardinality | Purpose                                       |
| ---------------------- | ----------- | --------------------------------------------- |
| Customers → Orders     | 1 : Many    | One customer can place multiple orders        |
| Orders → Order Items   | 1 : Many    | One order can contain multiple products       |
| Products → Order Items | 1 : Many    | One product can appear in many order lines    |
| Orders → Payments      | 1 : Many*   | An order can have one or more payment records |

> *The actual cardinality should reflect the business rules and data model implemented in PostgreSQL. If the system guarantees exactly one payment per order, this can instead be modeled as **1:1** with an appropriate uniqueness constraint.

---

# Analytical Workflow

The project follows a structured analytics pipeline:

```text
Raw CSV Data
     ↓
Data Profiling
     ↓
Data Cleaning
     ↓
Entity Identification
     ↓
Relational Schema Design
     ↓
PostgreSQL Database
     ↓
Data Import
     ↓
Data Validation
     ↓
SQL Analysis
     ↓
Advanced SQL
     ↓
Views & Index Optimization
     ↓
Python + SQLAlchemy
     ↓
Pandas Analysis
     ↓
KPI Calculation
     ↓
Business Insights
     ↓
Actionable Recommendations
```

---

# Expected Business KPIs

The project can calculate key sales-performance metrics including:

### Total Revenue

Total value generated from sales transactions.

### Total Orders

Number of unique customer orders.

### Total Quantity Sold

Total number of product units sold.

### Average Order Value

Average revenue generated per order.

```text
AOV = Total Revenue / Total Orders
```

### Gross Profit

```text
Gross Profit = Sales Revenue - Product Cost
```

### Profit Margin

```text
Profit Margin = Gross Profit / Sales Revenue × 100
```

### Customer Revenue

Total revenue generated by each customer.

### Product Revenue

Total sales generated by each product.

### Category Revenue

Revenue contribution of each product category.

### Monthly Sales

Sales performance grouped by month to identify trends and seasonality.

---

# Advanced Analytics

The project goes beyond basic SQL aggregation by implementing advanced analytical techniques.

### Ranking Analysis

Window functions such as:

```sql
RANK()
ROW_NUMBER()
DENSE_RANK()
```

can be used to identify:

* Top products
* Top customers
* Top cities
* Top categories
* Regional rankings

### Running Totals

Running totals can be used to understand cumulative revenue over time.

### Common Table Expressions

CTEs can break complex analytical queries into logical and reusable stages.

### Views

Database views can provide reusable datasets for:

* Sales reporting
* Customer analysis
* Product performance
* Monthly trends
* Management dashboards

### Indexing

Indexes can be added to frequently queried columns to improve database query performance, particularly on:

* Foreign keys
* Order dates
* Customer IDs
* Product IDs
* Frequently filtered business attributes

---

# Python Integration

After completing the SQL analysis, PostgreSQL is connected to Python using tools such as **SQLAlchemy and psycopg2**.

Python is used to:

1. Establish a secure database connection.
2. Execute SQL queries.
3. Retrieve analytical datasets.
4. Load results into Pandas DataFrames.
5. Perform additional data analysis.
6. Calculate KPIs.
7. Validate analytical outputs.
8. Generate business insights.

Example workflow:

```text
PostgreSQL
     ↓
SQL Query
     ↓
SQLAlchemy / psycopg2
     ↓
Python
     ↓
Pandas DataFrame
     ↓
Analysis
     ↓
Business Insights
```

---

# Testing & Error Handling

The Python component also incorporates software-engineering practices rather than relying only on exploratory analysis.

The project includes:

* Exception handling
* Logging
* Database connection validation
* Query error handling
* Data validation
* Pandas validation
* Automated testing with Pytest

This helps make the analytical pipeline more reliable, reproducible, and maintainable.

---

# Final Outcome

The completed project demonstrates an end-to-end ability to work with real-world business data, starting from raw transactional data and progressing toward structured analysis and business decision-making.

The project showcases practical capabilities in:

* **Relational database design**
* **PostgreSQL**
* **Advanced SQL**
* **Data cleaning and validation**
* **ETL concepts**
* **Database optimization**
* **Business KPI development**
* **Python**
* **Pandas**
* **SQL-to-Python integration**
* **Data testing**
* **Error handling**
* **Business intelligence**
* **Analytical problem solving**



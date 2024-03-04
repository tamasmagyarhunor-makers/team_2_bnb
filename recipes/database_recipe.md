# Two Tables Design Recipe Template

_Copy this recipe template to design and create two related database tables from a specification._

## 1. Extract nouns from the user stories or specification

```
As a user, 
I want to view a list of all spaces on MakersBnb
So that I can decide where I want to stay

As a user, 
I want to view a specific space from the list of all spaces on MakersBnb
So that I can decide where I want to stay

As a user,
I want to list a new space giving it a name, a description, a price and availability
So that I can find a booker to stay there

As a user,
I want to request to hire a space for one night
So that I can start planning my holiday

As a user,
I want to see pending requests to hire my spaces in a single place
So that I can easily respond to people who want to book my spaces

As a user,
I want to see a list of booking requests that I’ve sent to hire other people’s spaces and their status (pending/approved/not accepted)
So that I can keep track of my upcoming trips

As a user,
I want to see the availability of a space
So that I can check whether I can book it for the dates I want

As a user,
I want to be blocked from requesting a space on nights it’s unavailable
So that I don’t waste my time

As a user, 
I want to be able to sign up with an email and a password
So that I can create I account

As a user,
I want to I want to be able to login into MakersBnB with my email and password
So that I can access my account


```

```
Nouns:

user, space, name, description, price, availibility, booker, requests, status, dates, email, password, account
```

## 2. Infer the Table Name and Columns

Put the different nouns in this table. Replace the example with your own nouns.

| Record                | Properties          |
| --------------------- | ------------------  |
| album                 | title, release year
| artist                | name

1. Name of the first table (always plural): `users` 

    Column names: `ID`, `email_address`, `password`

2. Name of the second table (always plural): `spaces` 

    Column names: `ID`, `user_id`, `name`, `location`, `description`, `price`

3. Name of the third table (always plural): `requests` 

    Column names: `id`, `space_id`, `booker_id`, `request_status`, `date`

4. Name of the fourth table (always plural): `availability` 

    Column names: `space_id`, `date 1`, `date 2`, `date 3` ...

## 3. Decide the column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

Most of the time, you'll need either `text`, `int`, `bigint`, `numeric`, or `boolean`. If you're in doubt, do some research or ask your peers.

Remember to **always** have the primary key `id` as a first column. Its type will always be `SERIAL`.

```
# EXAMPLE:

Table: users
ID: int
email_address: varchar(100)
password: varchar(100)

Table: spaces
id: int
user_id: int
name: varchar(100)
location: varchar(100)
description: text
price: float

Table: requests
id: int
space_id: int
booker_id: int
request_status: varchar(100)
date: date

Table: availability
space_id: int
date 1: boolean
date 2: boolean
date 3: boolean
(and so on)

```

## 4. Decide on The Tables Relationship

Most of the time, you'll be using a **one-to-many** relationship, and will need a **foreign key** on one of the two tables.

To decide on which one, answer these two questions:

1. Can one user have many spaces? (Yes)
2. Can one user have many requests? (Yes)
3. Can one user have many availibility? (No)
4. Can one space have many requests? (Yes)
5. Can one space have many availability? (Yes)
6. Can one request have many availablity? (No)

You'll then be able to say that:

1. **One user has many spaces**
2. And on the other side, **a space belongs to one user**
3. In that case, the foreign key is in the table spaces

1. **One user has many requests**
2. And on the other side, **a request belongs to one user**
3. In that case, the foreign key is in the table requests

1. **One space has many requests**
2. And on the other side, **a request belongs to one space**
3. In that case, the foreign key is in the table requests

1. **One space has many availabilities**
2. And on the other side, **an availability belongs to one space**
3. In that case, the foreign key is in the table availability

## 5. Write the SQL

```sql

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  email_address varchar(100),
  password varchar(100)
);

CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name varchar(100),
  location varchar(100),
  description text,
  price float
  user_id int,
  constraint fk_owner_id foreign key(user_id)
    references users(id)
    on delete cascade
);

CREATE TABLE requests (
  id SERIAL PRIMARY KEY,
  request_status varchar(100),
  date date
  constraint fk_space_id foreign key(space_id)
    references spaces(id)
    on delete cascade
  constraint fk_booker_id foreign key(booker_id)
    references users(id)
    on delete cascade
);

CREATE TABLE availability (
  date_1 boolean,
  date_2 boolean,
  date_3 boolean,
  constraint fk_space_id foreign key(space_id)
    references spaces(id)
    on delete cascade
);

```

## 6. Create the tables

```bash
psql -h 127.0.0.1 pokemonbnb < pokemon_bnb_seed.sql
```
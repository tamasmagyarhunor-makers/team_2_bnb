-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.

-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users cascade;
DROP TABLE IF EXISTS spaces cascade;
DROP TABLE IF EXISTS bookings cascade;
DROP TABLE IF EXISTS space_availability cascade;

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  title varchar(15),
  first_name varchar(40),
  last_name varchar(40),
  email_address varchar(100),
  password varchar(100),
  phone_number varchar(11)
);

CREATE TABLE spaces (
  id SERIAL PRIMARY KEY,
  name varchar(100),
  location varchar(100),
  description text,
  price float,
  user_id int,
  constraint fk_user_id foreign key(user_id)
    references users(id)
    on delete cascade
);


CREATE TABLE bookings (
  id SERIAL PRIMARY KEY,
  space_name varchar(100),
  booking_status varchar(100),
  start_date date,
  end_date date,
  space_id int,
  constraint fk_space_id foreign key(space_id)
    references spaces(id)
    on delete cascade,
  user_id int,
  constraint fk_user_id foreign key(user_id)
    references users(id)
    on delete cascade
);

-- SQL to make availability table if functionality is implemented

-- CREATE TABLE space_availability (
--   id SERIAL PRIMARY KEY,
--   space_id int,
--   date_1 boolean,
--   date_2 boolean,
--   date_3 boolean,
--   constraint fk_space_id foreign key(space_id)
--     references spaces(id)
--     on delete cascade
-- );

-- Inserting users
INSERT INTO users (title, first_name, last_name, email_address, password, phone_number) VALUES
('Mr', 'John', 'Smith', 'email@testmail.com', 'Password1', '07926345037'),
('Miss', 'Regina', 'Phalange', 'Regina_phalange@testmail.com', 'Password2', '07926345048'),
('Mr', 'Ken', 'Adams', 'ken_adams@testmail.com', 'Password3', '07926345081');

-- Inserting spaces
INSERT INTO spaces (name, location, description, price, user_id) VALUES
('Cozy Studio Apartment', 'New York', 'A small but comfortable studio in downtown.', 100.00, 1),
('Spacious Loft', 'Los Angeles', 'A modern loft with city views.', 150.00, 2),
('Beach House', 'Miami', 'A beautiful house steps away from the beach.', 200.00, 3);

-- Inserting bookings
INSERT INTO bookings (space_name, booking_status, start_date, end_date, space_id, user_id) VALUES
('Cozy Studio Apartment', 'Pending', '2024-03-04', '2024-03-06', 1, 1),
('Spacious Loft', 'Approved', '2024-03-05', '2024-03-08', 2, 2),
('Beach House', 'Pending', '2024-04-06', '2024-04-10', 3, 3);

-- SQL to add availability data to table if functionality is implemented
-- -- Inserting availability
-- INSERT INTO space_availability (date_1, date_2, date_3, space_id) VALUES
-- (true, false, true, 1),
-- (false, true, true, 2),
-- (true, true, false, 3);
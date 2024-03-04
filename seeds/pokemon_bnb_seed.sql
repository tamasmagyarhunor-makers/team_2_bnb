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
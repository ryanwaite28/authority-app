CREATE SCHEMA IF NOT EXISTS authority;

CREATE TABLE IF NOT EXISTS authority.users (
  id SERIAL NOT NULL,

  displayname varchar(255) NOT NULL,
  username varchar(255) NOT NULL UNIQUE,
  email varchar(255) NOT NULL UNIQUE,
  pswrd varchar(255) NOT NULL,
  bio varchar(1000),
  weblink varchar(1000),
  icon_id varchar(500),
  icon_link varchar(500),
  wallpaper_id varchar(500),
  wallpaper_link varchar(500),
  uuid varchar(255) UNIQUE,
  is_private BOOLEAN NOT NULL DEFAULT FALSE,
  date_created TIMESTAMP,

  PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS authority.user_fields (
  id SERIAL NOT NULL,
  
  user_id int NOT NULL,
  field_name varchar(255) NOT NULL,
  field_type varchar(255) NOT NULL,
  field_value varchar(500) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT field_owner FOREIGN KEY (user_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.user_reviews (
  id SERIAL NOT NULL,
  
  user_id int NOT NULL,
  writer_id int NOT NULL,
  rating int NOT NULL,
  summary varchar(255) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT user_review_user FOREIGN KEY (user_id) REFERENCES authority.users (id),
  CONSTRAINT user_review_writer FOREIGN KEY (writer_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.followings (
  id SERIAL NOT NULL,
  
  user_id int NOT NULL,
  follows_id int NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT followings_user FOREIGN KEY (user_id) REFERENCES authority.users (id),
  CONSTRAINT followings_follow FOREIGN KEY (follows_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.following_requests (
  id SERIAL NOT NULL,
  
  user_id int NOT NULL,
  follows_id int NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT following_requests_user FOREIGN KEY (user_id) REFERENCES authority.users (id),
  CONSTRAINT following_requests_follow FOREIGN KEY (follows_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.subscriptions (
  id SERIAL NOT NULL,
  
  user_id int NOT NULL,
  subscribes_to_id int NOT NULL,
  subscribe_content_type varchar(255) NOT NULL,
  deliver_sms boolean NOT NULL,
  deliver_email boolean NOT NULL,
  deliver_notification boolean NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT subscriber_user FOREIGN KEY (user_id) REFERENCES authority.users (id),
  CONSTRAINT subscribee_user FOREIGN KEY (subscribes_to_id) REFERENCES authority.users (id)
);



CREATE TABLE IF NOT EXISTS authority.poems (
  id SERIAL NOT NULL,
  
  owner_id int NOT NULL,
  title varchar(255) NOT NULL,
  body TEXT NOT NULL,
  image_id varchar(500),
  image_link varchar(500),
  tags varchar(500),
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,
  last_edited TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT poem_owner FOREIGN KEY (owner_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.stories (
  id SERIAL NOT NULL,
  
  owner_id int NOT NULL,
  title varchar(255) NOT NULL,
  body TEXT NOT NULL,
  image_id varchar(500),
  image_link varchar(500),
  tags varchar(500),
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,
  last_edited TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT story_owner FOREIGN KEY (owner_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.books (
  id SERIAL NOT NULL,
  
  owner_id int NOT NULL,
  title varchar(255) NOT NULL,
  summary text NOT NULL,
  cover_image_id varchar(500),
  cover_image_link varchar(500),
  back_image_id varchar(500),
  back_image_link varchar(500),
  tags varchar(500),
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,
  last_edited TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT book_owner FOREIGN KEY (owner_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.book_pages (
  id SERIAL NOT NULL,
  
  owner_id int NOT NULL,
  book_id int NOT NULL,
  body TEXT NOT NULL,
  image_id varchar(500),
  image_link varchar(500),
  tags varchar(500),
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,
  last_edited TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT book FOREIGN KEY (book_id) REFERENCES authority.books (id),
  CONSTRAINT book_page_owner FOREIGN KEY (owner_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.poem_likes (
  id SERIAL NOT NULL,
  
  user_id int NOT NULL,
  poem_id int NOT NULL,
  like_type int NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT poem_like_user FOREIGN KEY (user_id) REFERENCES authority.users (id),
  CONSTRAINT poem_like_poem FOREIGN KEY (poem_id) REFERENCES authority.poems (id)
);

CREATE TABLE IF NOT EXISTS authority.story_likes (
  id SERIAL NOT NULL,
  
  user_id int NOT NULL,
  story_id int NOT NULL,
  like_type int NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT story_like_user FOREIGN KEY (user_id) REFERENCES authority.users (id),
  CONSTRAINT story_like_story FOREIGN KEY (story_id) REFERENCES authority.stories (id)
);

CREATE TABLE IF NOT EXISTS authority.book_likes (
  id SERIAL NOT NULL,
  
  user_id int NOT NULL,
  book_id int NOT NULL,
  like_type int NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT book_like_user FOREIGN KEY (user_id) REFERENCES authority.users (id),
  CONSTRAINT book_like_book FOREIGN KEY (book_id) REFERENCES authority.books (id)
);

CREATE TABLE IF NOT EXISTS authority.book_page_likes (
  id SERIAL NOT NULL,
  
  user_id int NOT NULL,
  book_page_id int NOT NULL,
  like_type int NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT book_page_like_user FOREIGN KEY (user_id) REFERENCES authority.users (id),
  CONSTRAINT book_page_like_book_page FOREIGN KEY (book_page_id) REFERENCES authority.book_pages (id)
);

CREATE TABLE IF NOT EXISTS authority.poem_comments (
  id SERIAL NOT NULL,
  
  owner_id int NOT NULL,
  poem_id int NOT NULL,
  body varchar(500) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT poem_comment_owner FOREIGN KEY (owner_id) REFERENCES authority.users (id),
  CONSTRAINT comment_poem FOREIGN KEY (poem_id) REFERENCES authority.poems (id)
);

CREATE TABLE IF NOT EXISTS authority.story_comments (
  id SERIAL NOT NULL,
  
  owner_id int NOT NULL,
  story_id int NOT NULL,
  body varchar(500) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT story_comment_owner FOREIGN KEY (owner_id) REFERENCES authority.users (id),
  CONSTRAINT comment_story FOREIGN KEY (story_id) REFERENCES authority.stories (id)
);

CREATE TABLE IF NOT EXISTS authority.book_comments (
  id SERIAL NOT NULL,
  
  owner_id int NOT NULL,
  book_id int NOT NULL,
  body varchar(500) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT book_comment_owner FOREIGN KEY (owner_id) REFERENCES authority.users (id),
  CONSTRAINT comment_book FOREIGN KEY (book_id) REFERENCES authority.books (id)
);

CREATE TABLE IF NOT EXISTS authority.book_page_comments (
  id SERIAL NOT NULL,
  
  owner_id int NOT NULL,
  book_page_id int NOT NULL,
  body varchar(500) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT book_page_comment_owner FOREIGN KEY (owner_id) REFERENCES authority.users (id),
  CONSTRAINT comment_book_page FOREIGN KEY (book_page_id) REFERENCES authority.book_pages (id)
);

CREATE TABLE IF NOT EXISTS authority.book_page_comments (
  id SERIAL NOT NULL,
  
  owner_id int NOT NULL,
  book_page_id int NOT NULL,
  body varchar(500) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT book_page_comment_owner FOREIGN KEY (owner_id) REFERENCES authority.users (id),
  CONSTRAINT comment_book_page FOREIGN KEY (book_page_id) REFERENCES authority.book_pages (id)
);

CREATE TABLE IF NOT EXISTS authority.poem_reviews (
  id SERIAL NOT NULL,
  
  poem_id int NOT NULL,
  writer_id int NOT NULL,
  rating int NOT NULL,
  summary varchar(255) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT poem_review_poem FOREIGN KEY (poem_id) REFERENCES authority.poems (id),
  CONSTRAINT poem_review_writer FOREIGN KEY (writer_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.story_reviews (
  id SERIAL NOT NULL,
  
  story_id int NOT NULL,
  writer_id int NOT NULL,
  rating int NOT NULL,
  summary varchar(255) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT story_review_story FOREIGN KEY (story_id) REFERENCES authority.stories (id),
  CONSTRAINT story_review_writer FOREIGN KEY (writer_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.book_reviews (
  id SERIAL NOT NULL,
  
  book_id int NOT NULL,
  writer_id int NOT NULL,
  rating int NOT NULL,
  summary varchar(255) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT book_review_book FOREIGN KEY (book_id) REFERENCES authority.books (id),
  CONSTRAINT book_review_writer FOREIGN KEY (writer_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.book_page_reviews (
  id SERIAL NOT NULL,
  
  book_page_id int NOT NULL,
  writer_id int NOT NULL,
  rating int NOT NULL,
  summary varchar(255) NOT NULL,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT book_page_review_book_page FOREIGN KEY (book_page_id) REFERENCES authority.book_pages (id),
  CONSTRAINT book_page_review_writer FOREIGN KEY (writer_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.messages (
  id SERIAL NOT NULL,
  
  sender_id int NOT NULL,
  recipient_id int NOT NULL,
  content varchar(255) NOT NULL,
  date_sent TIMESTAMP,
  date_read TIMESTAMP,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT message_sender FOREIGN KEY (sender_id) REFERENCES authority.users (id),
  CONSTRAINT message_recipient FOREIGN KEY (recipient_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.notifications (
  id SERIAL NOT NULL,

  from_id int,
  user_id int NOT NULL,
  action_type varchar(255) NOT NULL,
  target_type varchar(255),
  target_id int,
  link varchar(255),
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id),
  CONSTRAINT notification_from FOREIGN KEY (from_id) REFERENCES authority.users (id),
  CONSTRAINT notification_user FOREIGN KEY (user_id) REFERENCES authority.users (id)
);

CREATE TABLE IF NOT EXISTS authority.api_keys (
  id SERIAL NOT NULL,

  name varchar(255) NOT NULL,
  email varchar(255) NOT NULL UNIQUE,
  verified BOOLEAN NOT NULL DEFAULT FALSE,
  request_count int NOT NULL DEFAULT 0,
  uuid varchar(255) UNIQUE,
  date_created TIMESTAMP,

  PRIMARY KEY (id)
);
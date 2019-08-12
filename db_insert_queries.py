import datetime, cgi
from chamber import run_db_action
from chamber import get_new_uuid1, make_password
from chamber import default_icon, default_wallpaper

def create_new_user(form_dict):
  def callback(cursor):
    displayname = str(form_dict['displayname']).encode()
    username = str(form_dict['username']).encode()
    email = str(form_dict['email']).encode()
    password = make_password(form_dict['password'])

    insert_tuple = (
      displayname, 
      username, 
      email, 
      password, 
      default_icon, 
      default_wallpaper
    )

    query = '''
    INSERT INTO authority.users 
    (displayname, username, email, pswrd, icon_link, wallpaper_link)
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_poem(form_dict, you_dict):
  def callback(cursor):
    you_id = you_dict['id']

    title = str(form_dict['title']).encode()
    body = cgi.escape(str(form_dict['body']).decode())
    image_id = str(form_dict['image_id']).encode()
    image_link = str(form_dict['image_link']).encode()
    tags = str(form_dict['tags']).encode()
    is_explicit = form_dict['is_explicit']
    is_private = form_dict['is_private']

    insert_tuple = (
      you_id, 
      title, 
      body, 
      image_id, 
      image_link, 
      tags, 
      is_explicit, 
      is_private,
    )

    query = '''
    INSERT INTO authority.poems 
    (owner_id, title, body, image_id, image_link, tags, is_explicit, is_private)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_story(form_dict, you_dict):
  def callback(cursor):
    you_id = you_dict['id']

    title = str(form_dict['title']).encode()
    body = cgi.escape(str(form_dict['body']).decode())
    image_id = str(form_dict['image_id']).encode()
    image_link = str(form_dict['image_link']).encode()
    tags = str(form_dict['tags']).encode()
    is_explicit = form_dict['is_explicit']
    is_private = form_dict['is_private']

    insert_tuple = (
      you_id, 
      title, 
      body, 
      image_id, 
      image_link, 
      tags, 
      is_explicit, 
      is_private,
    )

    query = '''
    INSERT INTO authority.stories 
    (owner_id, title, body, image_id, image_link, tags, is_explicit, is_private)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book(form_dict, you_dict):
  def callback(cursor):
    you_id = you_dict['id']

    title = str(form_dict['title']).encode()
    summary = cgi.escape(str(form_dict['summary']).decode())
    cover_id = str(form_dict['cover_image_id']).encode()
    cover_link = str(form_dict['cover_image_link']).encode()
    back_id = str(form_dict['back_image_id']).encode()
    back_link = str(form_dict['back_image_link']).encode()
    tags = str(form_dict['tags']).encode()
    is_explicit = form_dict['is_explicit']
    is_private = form_dict['is_private']

    insert_tuple = (
      you_id, 
      title, 
      summary, 
      cover_id, 
      cover_link, 
      back_id, 
      back_link, 
      tags, 
      is_explicit, 
      is_private,
    )

    query = '''
    INSERT INTO authority.stories 
    (owner_id, title, body, cover_id, cover_link, back_id, back_link, tags, is_explicit, is_private)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_page(form_dict, you_dict):
  def callback(cursor):
    you_id = you_dict['id']

    book_id = int(form_dict['book_id'])
    body = cgi.escape(str(form_dict['body']).decode())
    image_id = str(form_dict['image_id']).encode()
    image_link = str(form_dict['image_link']).encode()
    tags = str(form_dict['tags']).encode()
    is_explicit = form_dict['is_explicit']
    is_private = form_dict['is_private']

    insert_tuple = (
      you_id, 
      book_id, 
      body, 
      image_id, 
      image_link, 
      tags, 
      is_explicit, 
      is_private,
    )

    query = '''
    INSERT INTO authority.stories 
    (owner_id, book_id, body, image_id, image_link, tags, is_explicit, is_private)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

# 

def create_new_follow(user_id, follow_id):
  def callback(cursor):
    insert_tuple = (user_id, follow_id, )

    query = '''
    INSERT INTO authority.followings 
    (user_id, follows_id)
    VALUES (%s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_follow_request(user_id, follow_id):
  def callback(cursor):
    insert_tuple = (user_id, follow_id, )

    query = '''
    INSERT INTO authority.following_requests 
    (user_id, follows_id)
    VALUES (%s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

# 

def create_new_user_review(form_dict, you_dict):
  def callback(cursor):
    user_id = form_dict['user_id']
    writer_id = you_dict['id']
    rating = form_dict['rating']
    summary = form_dict['summary']

    insert_tuple = (
      user_id, 
      writer_id, 
      rating, 
      summary,
    )

    query = '''
    INSERT INTO authority.user_reviews 
    (user_id, writer_id, rating, summary)
    VALUES (%s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_poem_review(form_dict, you_dict):
  def callback(cursor):
    poem_id = form_dict['poem_id']
    writer_id = you_dict['id']
    rating = form_dict['rating']
    summary = form_dict['summary']

    insert_tuple = (
      poem_id, 
      writer_id, 
      rating, 
      summary,
    )

    query = '''
    INSERT INTO authority.poem_reviews 
    (poem_id, writer_id, rating, summary)
    VALUES (%s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_story_review(form_dict, you_dict):
  def callback(cursor):
    story_id = form_dict['story_id']
    writer_id = you_dict['id']
    rating = form_dict['rating']
    summary = form_dict['summary']

    insert_tuple = (
      story_id, 
      writer_id, 
      rating, 
      summary,
    )

    query = '''
    INSERT INTO authority.story_reviews 
    (story_id, writer_id, rating, summary)
    VALUES (%s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_review(form_dict, you_dict):
  def callback(cursor):
    book_id = form_dict['book_id']
    writer_id = you_dict['id']
    rating = form_dict['rating']
    summary = form_dict['summary']

    insert_tuple = (
      book_id, 
      writer_id, 
      rating, 
      summary,
    )

    query = '''
    INSERT INTO authority.book_reviews 
    (book_id, writer_id, rating, summary)
    VALUES (%s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_page_review(form_dict, you_dict):
  def callback(cursor):
    book_page_id = form_dict['book_page_id']
    writer_id = you_dict['id']
    rating = form_dict['rating']
    summary = form_dict['summary']

    insert_tuple = (
      book_page_id, 
      writer_id, 
      rating, 
      summary,
    )

    query = '''
    INSERT INTO authority.book_reviews 
    (book_page_id, writer_id, rating, summary)
    VALUES (%s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

# 

def create_new_poem_comment(form_dict, you_dict):
  def callback(cursor):
    owner_id = you_dict['id']
    poem_id = form_dict['poem_id']
    body = form_dict['body']

    insert_tuple = (
      owner_id, 
      poem_id, 
      body, 
    )

    query = '''
    INSERT INTO authority.poem_reviews 
    (owner_id, poem_id, body)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_story_comment(form_dict, you_dict):
  def callback(cursor):
    owner_id = you_dict['id']
    story_id = form_dict['story_id']
    body = form_dict['body']

    insert_tuple = (
      owner_id, 
      story_id, 
      body, 
    )

    query = '''
    INSERT INTO authority.poem_reviews 
    (owner_id, story_id, body)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_comment(form_dict, you_dict):
  def callback(cursor):
    owner_id = you_dict['id']
    book_id = form_dict['book_id']
    body = form_dict['body']

    insert_tuple = (
      owner_id, 
      book_id, 
      body, 
    )

    query = '''
    INSERT INTO authority.poem_reviews 
    (owner_id, book_id, body)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_page_comment(form_dict, you_dict):
  def callback(cursor):
    owner_id = you_dict['id']
    book_page_id = form_dict['book_page_id']
    body = form_dict['body']

    insert_tuple = (
      owner_id, 
      book_page_id, 
      body, 
    )

    query = '''
    INSERT INTO authority.poem_reviews 
    (owner_id, book_page_id, body)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

# 

def create_new_poem_like(user_id, poem_id, like_type):
  def callback(cursor):
    insert_tuple = (user_id, poem_id, like_type)

    query = '''
    INSERT INTO authority.poem_likes 
    (user_id, poem_id, like_type)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_story_like(user_id, story_id, like_type):
  def callback(cursor):
    insert_tuple = (user_id, story_id, like_type)

    query = '''
    INSERT INTO authority.story_likes 
    (user_id, story_id, like_type)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_like(user_id, book_id, like_type):
  def callback(cursor):
    insert_tuple = (user_id, book_id, like_type)

    query = '''
    INSERT INTO authority.book_likes 
    (user_id, book_id, like_type)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_page_like(user_id, book_page_id, like_type):
  def callback(cursor):
    insert_tuple = (user_id, book_page_id, like_type)

    query = '''
    INSERT INTO authority.book_page_likes 
    (user_id, book_page_id, like_type)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

# 

def create_new_poem_viewer(owner_id, user_id, poem_id):
  def callback(cursor):
    # owner_id = owner of the content (denormalize)
    insert_tuple = (owner_id, user_id, poem_id)

    query = '''
    INSERT INTO authority.poem_viewers 
    (owner_id, user_id, poem_id)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_story_viewer(owner_id, user_id, story_id):
  def callback(cursor):
    insert_tuple = (owner_id, user_id, story_id)

    query = '''
    INSERT INTO authority.story_viewers 
    (owner_id, user_id, story_id)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_viewer(owner_id, user_id, book_id):
  def callback(cursor):
    insert_tuple = (owner_id, user_id, book_id)

    query = '''
    INSERT INTO authority.book_viewers 
    (owner_id, user_id, book_id)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_page_viewer(owner_id, user_id, book_page_id):
  def callback(cursor):
    insert_tuple = (owner_id, user_id, book_page_id)

    query = '''
    INSERT INTO authority.book_page_viewers 
    (owner_id, user_id, book_page_id)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

# 

def create_new_poem_view_request(owner_id, user_id, poem_id):
  def callback(cursor):
    # owner_id = owner of the content (denormalize)
    insert_tuple = (owner_id, user_id, poem_id)

    query = '''
    INSERT INTO authority.poem_view_requests 
    (owner_id, user_id, poem_id)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_story_view_request(owner_id, user_id, story_id):
  def callback(cursor):
    insert_tuple = (owner_id, user_id, story_id)

    query = '''
    INSERT INTO authority.story_view_requests 
    (owner_id, user_id, story_id)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_view_request(owner_id, user_id, book_id):
  def callback(cursor):
    insert_tuple = (owner_id, user_id, book_id)

    query = '''
    INSERT INTO authority.book_view_requests 
    (owner_id, user_id, book_id)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

def create_new_book_page_view_request(owner_id, user_id, book_page_id):
  def callback(cursor):
    insert_tuple = (owner_id, user_id, book_page_id)

    query = '''
    INSERT INTO authority.book_page_view_requests 
    (owner_id, user_id, book_page_id)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

# 

def create_new_message(form_dict):
  def callback(cursor):
    sender_id = form_dict['sender_id']
    recipient_id = form_dict['recipient_id']
    content = form_dict['content'].decode()

    insert_tuple = (
      sender_id,
      recipient_id,
      content,
    )

    query = '''
    INSERT INTO authority.messages 
    (sender_id, recipient_id, content)
    VALUES (%s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)

# 

def create_new_notification(form_dict):
  def callback(cursor):
    from_id = form_dict['from_id']
    user_id = form_dict['user_id']
    action_type = form_dict['action_type']
    target_type = form_dict['target_type']
    target_id = form_dict['target_id']
    link = form_dict['link']

    insert_tuple = (
      from_id,
      user_id,
      action_type,
      target_type,
      target_id,
      link,
    )

    query = '''
    INSERT INTO authority.notifications 
    (from_id, user_id, action_type, target_type, target_id, link)
    VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
    '''

    print('insert query - ', query)

    cursor.execute(query, insert_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)
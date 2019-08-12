import datetime, cgi
from chamber import run_db_action
from chamber import get_new_uuid1, make_password
from chamber import default_icon, default_wallpaper



# utility fn

def proxy_delete(table_name, row_id):
  def callback(cursor):
    delete_tuple = (table_name, row_id, )
    query = '''
    DELETE FROM authority.'%s' WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

# 

def delete_user(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.users WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_poem(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.poems WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_story(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.stories WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.books WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_page(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.books WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

# 

def delete_follow(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.followings WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

def delete_follow_request(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.following_requests WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

# 

def delete_user_review(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.user_reviews WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_poem_review(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.poem_reviews WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_story_review(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.story_reviews WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_review(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_reviews WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_page_review(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_page_reviews WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

# 

def delete_poem_comment(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.poem_comments WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_story_comment(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.story_comments WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_comment(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_comments WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_page_comment(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_page_comments WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

# 

def delete_poem_like(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.poem_likes WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_story_like(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.story_likes WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_like(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_likes WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_page_like(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_likes WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

# 

def delete_poem_viewer(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.poem_viewers WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_story_viewer(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.story_viewers WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_viewer(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_viewers WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_page_viewer(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_page_viewers WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

# 

def delete_poem_view_request(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.poem_view_requests WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_story_view_request(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.story_view_requests WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_view_request(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_view_requests WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

def delete_book_page_view_request(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.book_page_view_requests WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

# 

def delete_message(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.messages WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)

# 

def delete_notification(row_id):
  def callback(cursor):
    delete_tuple = (row_id, )
    query = '''
    DELETE FROM authority.notifications WHERE id = %s
    '''

    print('delete query - ', query)

    cursor.execute(query, delete_tuple)
    return True 

  return run_db_action(callback)
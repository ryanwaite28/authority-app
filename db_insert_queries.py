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

def create_new_story(form_dict, you_dict):
  def callback(cursor):
    you_id = you_dict['id']

    title = str(form_dict['title']).encode()
    body = cgi.escape(str(form_dict['body']).encode())
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
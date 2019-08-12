from chamber import run_db_action, make_password

def update_account(form_dict, you_dict):
  print(form_dict, you_dict)
  def callback(cursor):
    query_list = []

    if 'displayname' in form_dict:
      query = '''
      UPDATE authority.users SET displayname = '%s' WHERE id = %s
      ''' % (form_dict['displayname'], you_dict["id"], )
      query_list.append(query)

    if 'username' in form_dict:
      query = '''
      UPDATE authority.users SET username = '%s' WHERE id = %s
      ''' % (form_dict['username'], you_dict["id"], )
      query_list.append(query)

    if 'email' in form_dict:
      query = '''
      UPDATE authority.users SET email = '%s' WHERE id = %s
      ''' % (form_dict['email'], you_dict["id"], )
      query_list.append(query)

    if 'weblink' in form_dict:
      query = '''
      UPDATE authority.users SET weblink = '%s' WHERE id = %s
      ''' % (form_dict['weblink'], you_dict["id"], )
      query_list.append(query)

    if 'tags' in form_dict:
      query = '''
      UPDATE authority.users SET tags = '%s' WHERE id = %s
      ''' % (form_dict['tags'], you_dict["id"], )
      query_list.append(query)

    if 'bio' in form_dict:
      query = '''
      UPDATE authority.users SET bio = '%s' WHERE id = %s
      ''' % (form_dict['bio'], you_dict["id"], )
      query_list.append(query)

    if 'visibility' in form_dict:
      query = '''
      UPDATE authority.users SET is_private = %s WHERE id = %s
      ''' % (form_dict['visibility'], you_dict["id"], )
      query_list.append(query)

    if 'icon_link' in form_dict and 'icon_id' in form_dict:
      query = '''
      UPDATE authority.users SET icon_link = '%s', icon_id = '%s' WHERE id = %s
      ''' % (form_dict['icon_link'], form_dict['icon_id'], you_dict["id"], )
      query_list.append(query)

    if 'wallpaper_link' in form_dict and 'wallpaper_id' in form_dict:
      query = '''
      UPDATE authority.users SET wallpaper_link = '%s', wallpaper_id = '%s' WHERE id = %s
      ''' % (form_dict['wallpaper_link'], form_dict['wallpaper_id'], you_dict["id"], )
      query_list.append(query)

    if 'password' in form_dict:
      password = make_password(form_dict['password'])
      query = '''
      UPDATE authority.users SET pswrd = '%s' WHERE id = %s
      ''' % (password, you_dict["id"], )
      query_list.append(query)

    for q in query_list:
      cursor.execute(q)

    return True 

  return run_db_action(callback)

# 

def update_poem(form_dict):
  def callback(cursor):
    query_list = []

    if 'title' in form_dict:
      query = '''
      UPDATE authority.poems SET title = '%s' WHERE id = %s
      ''' % (form_dict['title'], form_dict["poem_id"], )
      query_list.append(query)

    if 'body' in form_dict:
      query = '''
      UPDATE authority.poems SET body = '%s' WHERE id = %s
      ''' % (form_dict['body'], form_dict["poem_id"], )
      query_list.append(query)

    if 'image_id' in form_dict and 'image_link' in form_dict:
      query = '''
      UPDATE authority.poems SET image_id = '%s', image_link = '%s' WHERE id = %s
      ''' % (form_dict['image_id'], form_dict['image_link'], form_dict["poem_id"], )
      query_list.append(query)

    if 'tags' in form_dict:
      query = '''
      UPDATE authority.poems SET tags = '%s' WHERE id = %s
      ''' % (form_dict['tags'], form_dict["poem_id"], )
      query_list.append(query)

    if 'is_explicit' in form_dict:
      query = '''
      UPDATE authority.poems SET is_explicit = %s WHERE id = %s
      ''' % (form_dict['is_explicit'], form_dict["poem_id"], )
      query_list.append(query)

    if 'is_private' in form_dict:
      query = '''
      UPDATE authority.poems SET is_private = %s WHERE id = %s
      ''' % (form_dict['is_private'], form_dict["poem_id"], )
      query_list.append(query)

    for q in query_list:
      cursor.execute(q)

    return True 

  return run_db_action(callback)

def update_story(form_dict):
  def callback(cursor):
    query_list = []

    if 'title' in form_dict:
      query = '''
      UPDATE authority.stories SET title = '%s' WHERE id = %s
      ''' % (form_dict['title'], form_dict["story_id"], )
      query_list.append(query)

    if 'body' in form_dict:
      query = '''
      UPDATE authority.stories SET body = '%s' WHERE id = %s
      ''' % (form_dict['body'], form_dict["story_id"], )
      query_list.append(query)

    if 'image_id' in form_dict and 'image_link' in form_dict:
      query = '''
      UPDATE authority.stories SET image_id = '%s', image_link = '%s' WHERE id = %s
      ''' % (form_dict['image_id'], form_dict['image_link'], form_dict["story_id"], )
      query_list.append(query)

    if 'tags' in form_dict:
      query = '''
      UPDATE authority.stories SET tags = '%s' WHERE id = %s
      ''' % (form_dict['tags'], form_dict["story_id"], )
      query_list.append(query)

    if 'is_explicit' in form_dict:
      query = '''
      UPDATE authority.stories SET is_explicit = %s WHERE id = %s
      ''' % (form_dict['is_explicit'], form_dict["story_id"], )
      query_list.append(query)

    if 'is_private' in form_dict:
      query = '''
      UPDATE authority.stories SET is_private = %s WHERE id = %s
      ''' % (form_dict['is_private'], form_dict["story_id"], )
      query_list.append(query)

    for q in query_list:
      cursor.execute(q)

    return True 

  return run_db_action(callback)

def update_book(form_dict):
  def callback(cursor):
    query_list = []

    if 'title' in form_dict:
      query = '''
      UPDATE authority.books SET title = '%s' WHERE id = %s
      ''' % (form_dict['title'], form_dict["book_id"], )
      query_list.append(query)

    if 'summary' in form_dict:
      query = '''
      UPDATE authority.books SET summary = '%s' WHERE id = %s
      ''' % (form_dict['summary'], form_dict["book_id"], )
      query_list.append(query)

    if 'cover_image_id' in form_dict and 'cover_image_link' in form_dict:
      query = '''
      UPDATE authority.books SET cover_image_id = '%s', cover_image_link = '%s' WHERE id = %s
      ''' % (form_dict['cover_image_id'], form_dict['cover_image_link'], form_dict["book_id"], )
      query_list.append(query)

    if 'back_image_id' in form_dict and 'back_image_link' in form_dict:
      query = '''
      UPDATE authority.books SET back_image_id = '%s', back_image_link = '%s' WHERE id = %s
      ''' % (form_dict['back_image_id'], form_dict['back_image_link'], form_dict["book_id"], )
      query_list.append(query)

    if 'tags' in form_dict:
      query = '''
      UPDATE authority.books SET tags = '%s' WHERE id = %s
      ''' % (form_dict['tags'], form_dict["book_id"], )
      query_list.append(query)

    if 'is_explicit' in form_dict:
      query = '''
      UPDATE authority.books SET is_explicit = %s WHERE id = %s
      ''' % (form_dict['is_explicit'], form_dict["book_id"], )
      query_list.append(query)

    if 'is_private' in form_dict:
      query = '''
      UPDATE authority.books SET is_private = %s WHERE id = %s
      ''' % (form_dict['is_private'], form_dict["book_id"], )
      query_list.append(query)

    for q in query_list:
      cursor.execute(q)

    return True 

  return run_db_action(callback)

def update_book_page(form_dict):
  def callback(cursor):
    query_list = []

    if 'body' in form_dict:
      query = '''
      UPDATE authority.book_pages SET body = '%s' WHERE id = %s
      ''' % (form_dict['body'], form_dict["book_page_id"], )
      query_list.append(query)

    if 'image_id' in form_dict and 'image_link' in form_dict:
      query = '''
      UPDATE authority.book_pages SET image_id = '%s', image_link = '%s' WHERE id = %s
      ''' % (form_dict['image_id'], form_dict['image_link'], form_dict["book_page_id"], )
      query_list.append(query)

    if 'tags' in form_dict:
      query = '''
      UPDATE authority.book_pages SET tags = '%s' WHERE id = %s
      ''' % (form_dict['tags'], form_dict["book_page_id"], )
      query_list.append(query)

    if 'is_explicit' in form_dict:
      query = '''
      UPDATE authority.book_pages SET is_explicit = %s WHERE id = %s
      ''' % (form_dict['is_explicit'], form_dict["book_page_id"], )
      query_list.append(query)

    if 'is_private' in form_dict:
      query = '''
      UPDATE authority.book_pages SET is_private = %s WHERE id = %s
      ''' % (form_dict['is_private'], form_dict["book_page_id"], )
      query_list.append(query)

    for q in query_list:
      cursor.execute(q)

    return True 

  return run_db_action(callback)

# 

def proxy_update_comment(form_dict):
  def callback(cursor):
    query_list = []

    if 'body' in form_dict:
      query = '''
      UPDATE authority.'%s' SET body = %s WHERE id = %s
      ''' 
      cursor.execute(query, (form_dict['table_name'], form_dict['body'], form_dict["content_id"], ))

    return True 

  return run_db_action(callback)
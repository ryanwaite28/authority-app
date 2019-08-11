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
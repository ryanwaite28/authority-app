from chamber import run_db_action

def get_user_by_id(user_id):
  def callback(cursor):
    query = '''
    SELECT id, displayname, username, bio, icon_link, wallpaper_link, 
      weblink, date_created, email, is_private,
      icon_id, wallpaper_id
    FROM authority.users
    WHERE id = %s
    ''' % (user_id,)
    cursor.execute(query)
    result = cursor.fetchone()

    if not result:
      return None

    user = {
      "id": result[0],
      "displayname": result[1],
      "username": result[2],
      "bio": result[3],
      "icon_link": result[4],
      "wallpaper_link": result[5],
      "weblink": result[6],
      "date_created": str(result[7]),
      "email": str(result[8]),
      "is_private": result[9],
      "icon_id": result[10],
      "wallpaper_id": result[11],
    }
  
    return user

  return run_db_action(callback)

def get_user_by_username(username):
  def callback(cursor):
    query = '''
    SELECT id, displayname, username, bio, icon_link, wallpaper_link, 
      weblink, date_created, email, is_private,
      icon_id, wallpaper_id
    FROM authority.users
    WHERE username = '%s'
    ''' % (str(username).encode(), )
  
    cursor.execute(query)
    result = cursor.fetchone()

    if not result:
      return None

    user = {
      "id": result[0],
      "displayname": result[1],
      "username": result[2],
      "bio": result[3],
      "icon_link": result[4],
      "wallpaper_link": result[5],
      "weblink": result[6],
      "date_created": str(result[7]),
      "email": str(result[8]),
      "is_private": result[9],
      "icon_id": result[10],
      "wallpaper_id": result[11],
    }

    return user

  return run_db_action(callback)

def get_user_profile_by_id(user_id):
  def callback(cursor):
    query = '''
    SELECT users.id, users.displayname, users.username, 
      users.bio, users.icon_link, users.wallpaper_link, 
      users.weblink, users.date_created, users.email, 
      users.is_private, users.icon_id, users.wallpaper_id,
      (SELECT COUNT(followings.id) FROM authority.followings WHERE followings.user_id = users.id) AS following_count,
      (SELECT COUNT(followings.id) FROM authority.followings WHERE followings.follows_id = users.id) AS followers_count,
      (SELECT COUNT(user_reviews.id) FROM authority.user_reviews WHERE user_reviews.user_id = users.id) AS reviews_count,
      (SELECT COUNT(poems.id) FROM authority.poems WHERE poems.owner_id = users.id) AS poems_count,
      (SELECT COUNT(stories.id) FROM authority.stories WHERE stories.owner_id = users.id) AS stories_count,
      (SELECT COUNT(books.id) FROM authority.books WHERE books.owner_id = users.id) AS books_count
    FROM authority.users
    WHERE id = %s
    ''' % (user_id,)
    cursor.execute(query)
    result = cursor.fetchone()

    if not result:
      return None

    user = {
      "id": result[0],
      "displayname": result[1],
      "username": result[2],
      "bio": result[3],
      "icon_link": result[4],
      "wallpaper_link": result[5],
      "weblink": result[6],
      "date_created": str(result[7]),
      "email": str(result[8]),
      "is_private": result[9],
      "icon_id": result[10],
      "wallpaper_id": result[11],
      "following_count": result[12],
      "followers_count": result[13],
      "reviews_count": result[14],
      "poems_count": result[15],
      "stories_count": result[16],
      "books_count": result[17],
    }
  
    return user

  return run_db_action(callback)

def get_user_profile_by_username(username):
  def callback(cursor):
    query = '''
    SELECT users.id, users.displayname, users.username, 
      users.bio, users.icon_link, users.wallpaper_link, 
      users.weblink, users.date_created, users.email, 
      users.is_private, users.icon_id, users.wallpaper_id,
      (SELECT COUNT(followings.id) FROM authority.followings WHERE followings.user_id = users.id) AS following_count,
      (SELECT COUNT(followings.id) FROM authority.followings WHERE followings.follows_id = users.id) AS followers_count,
      (SELECT COUNT(user_reviews.id) FROM authority.user_reviews WHERE user_reviews.user_id = users.id) AS reviews_count,
      (SELECT COUNT(poems.id) FROM authority.poems WHERE poems.owner_id = users.id) AS poems_count,
      (SELECT COUNT(stories.id) FROM authority.stories WHERE stories.owner_id = users.id) AS stories_count,
      (SELECT COUNT(books.id) FROM authority.books WHERE books.owner_id = users.id) AS books_count
    FROM authority.users
    WHERE username = '%s'
    ''' % (str(username).encode(), )
  
    cursor.execute(query)
    result = cursor.fetchone()

    if not result:
      return None

    user = {
      "id": result[0],
      "displayname": result[1],
      "username": result[2],
      "bio": result[3],
      "icon_link": result[4],
      "wallpaper_link": result[5],
      "weblink": result[6],
      "date_created": str(result[7]),
      "email": str(result[8]),
      "is_private": result[9],
      "icon_id": result[10],
      "wallpaper_id": result[11],
      "following_count": result[12],
      "followers_count": result[13],
      "reviews_count": result[14],
      "poems_count": result[15],
      "stories_count": result[16],
      "books_count": result[17],
    }

    return user

  return run_db_action(callback)

def check_user_by_username(username):
  def callback(cursor):
    query = '''
    SELECT username, email, pswrd, id FROM authority.users WHERE username = '%s'
    ''' % (str(username).encode(), )

    cursor.execute(query)
    result = cursor.fetchone()

    if not result:
      return None

    return {
      "username": result[0],
      "email": result[1],
      "password": result[2],
      "id": result[3],
    }

  return run_db_action(callback)

def check_user_by_email(email):
  def callback(cursor):
    query = '''
    SELECT username, email, pswrd, id FROM authority.users WHERE email = '%s'
    ''' % (str(email).encode(), )

    cursor.execute(query)
    result = cursor.fetchone()

    if not result:
      return None

    return {
      "username": result[0],
      "email": result[1],
      "password": result[2],
      "id": result[3],
    }

  return run_db_action(callback)

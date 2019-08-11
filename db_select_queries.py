from chamber import run_db_action

def get_user_by_id(user_id):
  def callback(cursor):
    query = '''
    SELECT id, displayname, username, bio, icon_link, wallpaper_link, 
      weblink, date_created, email, is_private,
      icon_id, wallpaper_id, tags, uuid
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
      "tags": result[12],
      "uuid": result[13],
    }
  
    return user

  return run_db_action(callback)

def get_user_by_username(username):
  def callback(cursor):
    query = '''
    SELECT id, displayname, username, bio, icon_link, wallpaper_link, 
      weblink, date_created, email, is_private,
      icon_id, wallpaper_id, tags, uuid
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
      "tags": result[12],
      "uuid": result[13],
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
      users.tags, users.uuid,
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
      "tags": result[12],
      "uuid": result[13],
      "following_count": result[14],
      "followers_count": result[15],
      "reviews_count": result[16],
      "poems_count": result[17],
      "stories_count": result[18],
      "books_count": result[19],
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
      users.tags, users.uuid,
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
      "tags": result[12],
      "uuid": result[13],
      "following_count": result[14],
      "followers_count": result[15],
      "reviews_count": result[16],
      "poems_count": result[17],
      "stories_count": result[18],
      "books_count": result[19],
    }

    return user

  return run_db_action(callback)

def check_user_by_username(username):
  def callback(cursor):
    query = '''SELECT username, email, pswrd, id FROM authority.users WHERE username = %s''' 

    cursor.execute(query, (str(username).encode(), ))
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
    query = '''SELECT username, email, pswrd, id FROM authority.users WHERE email = %s'''

    cursor.execute(query, (str(email).encode(), ))
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

def get_story_full_by_id(story_id):
  def callback(cursor):
    query = '''
    SELECT stories.id AS StoryID, stories.owner_id AS StoryOwnerID, stories.title AS StoryTitle, 
      stories.body AS StoryBody, stories.image_id AS StoryImageID, stories.image_link AS StoryImageLink, 
      stories.tags AS StoryTags, stories.is_explicit AS StoryExplicit, stories.is_private AS StoryPrivate, 
      stories.uuid AS StoryUUID, stories.date_created AS StoryDateCreated, stories.last_edited AS StoryLastEdited, 
      
      users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
      users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
      users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
      users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID,
      
      (SELECT COUNT(story_viewers.id) FROM authority.story_viewers WHERE story_viewers.story_id = stories.id) AS StoryViewers,
      (SELECT COUNT(story_view_requests.id) FROM authority.story_view_requests WHERE story_view_requests.story_id = stories.id) AS StoryViewRequests,
      (SELECT COUNT(story_likes.id) FROM authority.story_likes WHERE story_likes.story_id = stories.id AND like_type = 1) AS StoryLikes,
      (SELECT COUNT(story_likes.id) FROM authority.story_likes WHERE story_likes.story_id = stories.id AND like_type = 0) AS StoryDislikes,
      (SELECT COUNT(story_comments.id) FROM authority.story_comments WHERE story_comments.story_id = stories.id) AS StoryComments,
      (SELECT COUNT(story_reviews.id) FROM authority.story_reviews WHERE story_reviews.story_id = stories.id) AS StoryReviews
    FROM authority.stories
    JOIN authority.users ON stories.owner_id = users.id
    WHERE stories.id = %s
    '''

    cursor.execute(query, (story_id, ))
    result = cursor.fetchone()

    if not result:
      return None

    story = {
      "id": result[0],
      "owner_id": result[1],
      "title": result[2],
      "body": result[3],
      "image_id": result[4],
      "image_link": result[5],
      "tags": result[6],
      "is_explicit": result[7],
      "is_private": result[8],
      "uuid": result[9],
      "date_created": result[10],
      "last_edited": result[11],
      "owner": {
        "id": result[12],
        "displayname": result[13],
        "username": result[14],
        "icon_link": result[15],
        "wallpaper_link": result[16],
        "date_created": str(result[17]),
        "email": str(result[18]),
        "is_private": result[19],
        "uuid": result[20],
      },
      "viewers_count": result[21],
      "view_requests_count": result[22],
      "likes_count": result[23],
      "dislikes_count": result[24],
      "comments_count": result[25],
      "reviews_count": result[26],
    }

    return story
  
  return run_db_action(callback)
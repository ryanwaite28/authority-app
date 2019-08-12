from chamber import run_db_action, apply_notification_message

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

def get_poem_full_by_id(poem_id):
  def callback(cursor):
    query = '''
    SELECT poems.id AS PoemID, poems.owner_id AS PoemOwnerID, poems.title AS PoemTitle, 
      poems.body AS PoemBody, poems.image_id AS PoemImageID, poems.image_link AS PoemImageLink, 
      poems.tags AS PoemTags, poems.is_explicit AS PoemExplicit, poems.is_private AS PoemPrivate, 
      poems.uuid AS PoemUUID, poems.date_created AS PoemDateCreated, poems.last_edited AS PoemLastEdited, 
      
      users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
      users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
      users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
      users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID,
      
      (SELECT COUNT(poem_viewers.id) FROM authority.poem_viewers WHERE poem_viewers.poem_id = stories.id) AS PoemViewers,
      (SELECT COUNT(poem_view_requests.id) FROM authority.poem_view_requests WHERE poem_view_requests.poem_id = stories.id) AS PoemViewRequests,
      (SELECT COUNT(poem_likes.id) FROM authority.poem_likes WHERE poem_likes.poem_id = stories.id AND like_type = 1) AS PoemLikes,
      (SELECT COUNT(poem_likes.id) FROM authority.poem_likes WHERE poem_likes.poem_id = stories.id AND like_type = 0) AS PoemDislikes,
      (SELECT COUNT(poem_comments.id) FROM authority.poem_comments WHERE poem_comments.poem_id = stories.id) AS PoemComments,
      (SELECT COUNT(poem_reviews.id) FROM authority.poem_reviews WHERE poem_reviews.poem_id = stories.id) AS PoemReviews
    FROM authority.poems
    JOIN authority.users ON poems.owner_id = users.id
    WHERE poems.id = %s
    '''

    cursor.execute(query, (poem_id, ))
    result = cursor.fetchone()

    if not result:
      return None

    poem = {
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

    return poem
  
  return run_db_action(callback)

def get_poem_slim_by_id(poem_id):
  def callback(cursor):
    query = '''
    SELECT poems.id AS PoemID, poems.owner_id AS PoemOwnerID, poems.title AS PoemTitle, 
      poems.body AS PoemBody, poems.image_id AS PoemImageID, poems.image_link AS PoemImageLink, 
      poems.tags AS PoemTags, poems.is_explicit AS PoemExplicit, poems.is_private AS PoemPrivate, 
      poems.uuid AS PoemUUID, poems.date_created AS PoemDateCreated, poems.last_edited AS PoemLastEdited, 
      
      users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
      users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
      users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
      users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
    FROM authority.poems
    JOIN authority.users ON poems.owner_id = users.id
    WHERE poems.id = %s
    '''

    cursor.execute(query, (poem_id, ))
    result = cursor.fetchone()

    if not result:
      return None

    poem = {
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
      }
    }

    return poem
  
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

def get_story_slim_by_id(story_id):
  def callback(cursor):
    query = '''
    SELECT stories.id AS StoryID, stories.owner_id AS StoryOwnerID, stories.title AS StoryTitle, 
      stories.body AS StoryBody, stories.image_id AS StoryImageID, stories.image_link AS StoryImageLink, 
      stories.tags AS StoryTags, stories.is_explicit AS StoryExplicit, stories.is_private AS StoryPrivate, 
      stories.uuid AS StoryUUID, stories.date_created AS StoryDateCreated, stories.last_edited AS StoryLastEdited, 
      
      users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
      users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
      users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
      users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
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
      }
    }

    return story
  
  return run_db_action(callback)

def get_book_full_by_id(book_id):
  def callback(cursor):
    query = '''
    SELECT books.id AS BookID, books.owner_id AS BookOwnerID, books.title AS BookTitle, 
      books.summary AS BookSummary, 
      books.cover_image_id AS BookCoverImageID, books.cover_image_link AS BookCoverImageLink, 
      books.back_image_id AS BookBackImageID, books.back_image_link AS BookBackImageLink, 
      books.tags AS BookTags, books.is_explicit AS BookExplicit, books.is_private AS BookPrivate, 
      books.uuid AS BookUUID, books.date_created AS BookDateCreated, books.last_edited AS BookLastEdited, 
      
      users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
      users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
      users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
      users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID,
      
      (SELECT COUNT(book_viewers.id) FROM authority.book_viewers WHERE book_viewers.book_id = books.id) AS BookViewers,
      (SELECT COUNT(book_view_requests.id) FROM authority.book_view_requests WHERE book_view_requests.book_id = books.id) AS BookViewRequests,
      (SELECT COUNT(book_likes.id) FROM authority.book_likes WHERE book_likes.book_id = books.id AND like_type = 1) AS BookLikes,
      (SELECT COUNT(book_likes.id) FROM authority.book_likes WHERE book_likes.book_id = books.id AND like_type = 0) AS BookDislikes,
      (SELECT COUNT(book_comments.id) FROM authority.book_comments WHERE book_comments.book_id = books.id) AS BookComments,
      (SELECT COUNT(book_reviews.id) FROM authority.book_reviews WHERE book_reviews.book_id = books.id) AS BookReviews
    FROM authority.books
    JOIN authority.users ON books.owner_id = users.id
    WHERE books.id = %s
    '''

    cursor.execute(query, (book_id, ))
    result = cursor.fetchone()

    if not result:
      return None

    book = {
      "id": result[0],
      "owner_id": result[1],
      "title": result[2],
      "summary": result[3],
      "cover_image_id": result[4],
      "cover_image_link": result[5],
      "back_image_id": result[6],
      "back_image_link": result[7],
      "tags": result[8],
      "is_explicit": result[9],
      "is_private": result[10],
      "uuid": result[11],
      "date_created": result[12],
      "last_edited": result[13],
      "owner": {
        "id": result[14],
        "displayname": result[15],
        "username": result[16],
        "icon_link": result[17],
        "wallpaper_link": result[18],
        "date_created": str(result[19]),
        "email": str(result[20]),
        "is_private": result[21],
        "uuid": result[22],
      },
      "viewers_count": result[23],
      "view_requests_count": result[24],
      "likes_count": result[25],
      "dislikes_count": result[26],
      "comments_count": result[27],
      "reviews_count": result[28],
    }

    return book
  
  return run_db_action(callback)

def get_book_slim_by_id(book_id):
  def callback(cursor):
    query = '''
    SELECT books.id AS BookID, books.owner_id AS BookOwnerID, books.title AS BookTitle, 
      books.summary AS BookSummary, 
      books.cover_image_id AS BookCoverImageID, books.cover_image_link AS BookCoverImageLink, 
      books.back_image_id AS BookBackImageID, books.back_image_link AS BookBackImageLink, 
      books.tags AS BookTags, books.is_explicit AS BookExplicit, books.is_private AS BookPrivate, 
      books.uuid AS BookUUID, books.date_created AS BookDateCreated, books.last_edited AS BookLastEdited, 
      
      users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
      users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
      users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
      users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
    FROM authority.books
    JOIN authority.users ON books.owner_id = users.id
    WHERE books.id = %s
    '''

    cursor.execute(query, (book_id, ))
    result = cursor.fetchone()

    if not result:
      return None

    book = {
      "id": result[0],
      "owner_id": result[1],
      "title": result[2],
      "summary": result[3],
      "cover_image_id": result[4],
      "cover_image_link": result[5],
      "back_image_id": result[6],
      "back_image_link": result[7],
      "tags": result[8],
      "is_explicit": result[9],
      "is_private": result[10],
      "uuid": result[11],
      "date_created": result[12],
      "last_edited": result[13],
      "owner": {
        "id": result[14],
        "displayname": result[15],
        "username": result[16],
        "icon_link": result[17],
        "wallpaper_link": result[18],
        "date_created": str(result[19]),
        "email": str(result[20]),
        "is_private": result[21],
        "uuid": result[22],
      }
    }

    return book
  
  return run_db_action(callback)

def get_book_page_full_by_id(book_page_id):
  def callback(cursor):
    query = '''
    SELECT book_pages.id AS BookPageID, book_pages.owner_id AS BookPageOwnerID, book_pages.book_id AS BookID, 
      book_pages.body AS BookPageBody, book_pages.image_id AS BookPageImageID, book_pages.image_link AS BookPageImageLink, 
      book_pages.tags AS BookPageTags, book_pages.is_explicit AS BookPageExplicit, book_pages.is_private AS BookPagePrivate, 
      book_pages.uuid AS BookPageUUID, book_pages.date_created AS BookPageDateCreated, book_pages.last_edited AS BookPageLastEdited, 
      
      users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
      users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
      users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
      users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID,
      
      (SELECT COUNT(book_page_viewers.id) FROM authority.book_page_viewers WHERE book_page_viewers.book_page_id = book_pages.id) AS BookPageViewers,
      (SELECT COUNT(book_page_view_requests.id) FROM authority.book_page_view_requests WHERE book_page_view_requests.book_page_id = book_pages.id) AS BookPageViewRequests,
      (SELECT COUNT(book_page_likes.id) FROM authority.book_page_likes WHERE book_page_likes.book_page_id = book_pages.id AND like_type = 1) AS BookPageLikes,
      (SELECT COUNT(book_page_likes.id) FROM authority.book_page_likes WHERE book_page_likes.book_page_id = book_pages.id AND like_type = 0) AS BookPageDislikes,
      (SELECT COUNT(book_page_comments.id) FROM authority.book_page_comments WHERE book_page_comments.book_page_id = book_pages.id) AS BookPageComments,
      (SELECT COUNT(book_page_reviews.id) FROM authority.book_page_reviews WHERE book_page_reviews.book_page_id = book_pages.id) AS BookPageReviews
    FROM authority.book_pages
    JOIN authority.users ON book_pages.owner_id = users.id
    WHERE book_pages.id = %s
    '''

    cursor.execute(query, (book_page_id, ))
    result = cursor.fetchone()

    if not result:
      return None

    book_page = {
      "id": result[0],
      "owner_id": result[1],
      "book_id": result[2],
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

    return book_page
  
  return run_db_action(callback)

def get_book_page_slim_by_id(book_page_id):
  def callback(cursor):
    query = '''
    SELECT book_pages.id AS BookPageID, book_pages.owner_id AS BookPageOwnerID, book_pages.book_id AS BookID, 
      book_pages.body AS BookPageBody, book_pages.image_id AS BookPageImageID, book_pages.image_link AS BookPageImageLink, 
      book_pages.tags AS BookPageTags, book_pages.is_explicit AS BookPageExplicit, book_pages.is_private AS BookPagePrivate, 
      book_pages.uuid AS BookPageUUID, book_pages.date_created AS BookPageDateCreated, book_pages.last_edited AS BookPageLastEdited, 
      
      users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
      users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
      users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
      users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
    FROM authority.book_pages
    JOIN authority.users ON book_pages.owner_id = users.id
    WHERE book_pages.id = %s
    '''

    cursor.execute(query, (book_page_id, ))
    result = cursor.fetchone()

    if not result:
      return None

    book_page = {
      "id": result[0],
      "owner_id": result[1],
      "book_id": result[2],
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
      }
    }

    return book_page
  
  return run_db_action(callback)

# 

def check_follow(user_id, follows_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.followings WHERE user_id = %s AND follows_id = %s
    '''

    cursor.execute(query, (user_id, follows_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

def check_follow_request(user_id, follows_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.following_requests WHERE user_id = %s AND follows_id = %s
    '''

    cursor.execute(query, (user_id, follows_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

# 

def get_user_followings(user_id, follow_id):
  def callback(cursor):
    if follow_id:
      query = '''
      SELECT followings.id AS FollowID, followings.user_id AS UserID, followings.follows_id AS FollowsID, 
        users.id, users.displayname, users.username, 
        users.icon_link, users.wallpaper_link, 
        users.date_created, users.email, 
        users.is_private, users.uuid
      FROM authority.followings
      JOIN authority.users ON followings.follows_id = users.id
      WHERE followings.user_id = %s AND followings.id < %s
      ORDER BY poem_comments.id DESC
      LIMIT 5
      ''' % (user_id, follow_id, )
    else:
      query = '''
      SELECT followings.id AS FollowID, followings.user_id AS UserID, followings.follows_id AS FollowsID, 
        users.id, users.displayname, users.username, 
        users.icon_link, users.wallpaper_link, 
        users.date_created, users.email, 
        users.is_private, users.uuid
      FROM authority.followings
      JOIN authority.users ON followings.follows_id = users.id
      WHERE followings.user_id = %s
      ORDER BY poem_comments.id DESC
      LIMIT 5
      ''' % (user_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    followings = []

    for record in results:
      follow = {
        "id": record[0],
        "user_id": record[1],
        "follows_id": record[2],
        "user": {
          "id": record[3],
          "displayname": record[4],
          "username": record[5],
          "icon_link": record[6],
          "wallpaper_link": record[7],
          "date_created": str(record[8]),
          "email": str(record[9]),
          "is_private": record[10],
          "uuid": record[11],
        }
      }
      followings.append(follow)

    return followings

  return run_db_action(callback)

def get_user_followers(user_id, follow_id):
  def callback(cursor):
    if follow_id:
      query = '''
      SELECT followings.id AS FollowID, followings.user_id AS UserID, followings.follows_id AS FollowsID, 
        users.id, users.displayname, users.username, 
        users.icon_link, users.wallpaper_link, 
        users.date_created, users.email, 
        users.is_private, users.uuid
      FROM authority.followings
      JOIN authority.users ON followings.user_id = users.id
      WHERE followings.follows_id = %s AND followings.id < %s
      ORDER BY poem_comments.id DESC
      LIMIT 5
      ''' % (user_id, follow_id, )
    else:
      query = '''
      SELECT followings.id AS FollowID, followings.user_id AS UserID, followings.follows_id AS FollowsID, 
        users.id, users.displayname, users.username, 
        users.icon_link, users.wallpaper_link, 
        users.date_created, users.email, 
        users.is_private, users.uuid
      FROM authority.followings
      JOIN authority.users ON followings.user_id = users.id
      WHERE followings.follows_id = %s
      ORDER BY poem_comments.id DESC
      LIMIT 5
      ''' % (user_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    followers = []

    for record in results:
      follow = {
        "id": record[0],
        "user_id": record[1],
        "follows_id": record[2],
        "user": {
          "id": record[3],
          "displayname": record[4],
          "username": record[5],
          "icon_link": record[6],
          "wallpaper_link": record[7],
          "date_created": str(record[8]),
          "email": str(record[9]),
          "is_private": record[10],
          "uuid": record[11],
        }
      }
      followers.append(follow)

    return followers

  return run_db_action(callback)

# 

def check_view_poem_permission(user_id, poem_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.poem_viewers WHERE user_id = %s AND poem_id = %s
    '''

    cursor.execute(query, (user_id, poem_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

def check_view_story_permission(user_id, story_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.story_viewers WHERE user_id = %s AND story_id = %s
    '''

    cursor.execute(query, (user_id, story_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

def check_view_book_permission(user_id, book_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.book_viewers WHERE user_id = %s AND book_id = %s
    '''

    cursor.execute(query, (user_id, book_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

def check_view_book_page_permission(user_id, book_page_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.book_page_viewers WHERE user_id = %s AND book_page_id = %s
    '''

    cursor.execute(query, (user_id, book_page_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

# 

def check_view_poem_request(user_id, poem_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.poem_view_requests WHERE user_id = %s AND poem_id = %s
    '''

    cursor.execute(query, (user_id, poem_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

def check_view_story_request(user_id, story_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.story_view_requests WHERE user_id = %s AND story_id = %s
    '''

    cursor.execute(query, (user_id, story_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

def check_view_book_request(user_id, book_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.book_view_requests WHERE user_id = %s AND book_id = %s
    '''

    cursor.execute(query, (user_id, book_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

def check_view_book_page_request(user_id, book_page_id):
  def callback(cursor):
    query = '''
    SELECT * FROM authority.book_page_view_requests WHERE user_id = %s AND book_page_id = %s
    '''

    cursor.execute(query, (user_id, book_page_id, ))
    result = cursor.fetchone()

    return result

  return run_db_action(callback)

# 

def get_poem_likes(poem_id, poem_like_id):
  def callback(cursor):
    if poem_like_id:
      query = '''
      SELECT poem_likes.id AS PoemLikeID, poem_likes.poem_id AS PoemID, poem_likes.like_type AS PoemLikeType,
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.poem_likes
      JOIN authority.users ON poem_likes.user_id = users.id
      WHERE poem_likes.poem_id = %s AND poem_likes.id < %s
      ORDER BY poem_likes.id DESC
      LIMIT 5
      ''' % (poem_id, poem_like_id, )
    else:
      query = '''
      SELECT poem_likes.id AS PoemLikeID, poem_likes.poem_id AS PoemID, poem_likes.like_type AS PoemLikeType,
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.poem_likes
      JOIN authority.users ON poem_likes.user_id = users.id
      WHERE poem_likes.id = %s
      ORDER BY poem_likes.id DESC
      LIMIT 5
      ''' % (poem_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    likes = []
    for record in results:
      like = {
        "id": record[0],
        "poem_id": record[1],
        "like_type": record[2],
        "user": {
          "id": record[3],
          "displayname": record[4],
          "username": record[5],
          "icon_link": record[6],
          "wallpaper_link": record[7],
          "date_created": str(record[8]),
          "email": str(record[9]),
          "is_private": record[10],
          "uuid": record[11],
        }
      }
      likes.append(like)

    return likes

  return run_db_action(callback)

def get_story_likes(story_id, story_like_id):
  def callback(cursor):
    if story_like_id:
      query = '''
      SELECT story_likes.id AS StoryLikeID, story_likes.story_id AS StoryID, story_likes.like_type AS StoryLikeType,
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.story_likes
      JOIN authority.users ON story_likes.user_id = users.id
      WHERE story_likes.story_id = %s AND story_likes.id < %s
      ORDER BY story_likes.id DESC
      LIMIT 5
      ''' % (story_id, story_like_id, )
    else:
      query = '''
      SELECT story_likes.id AS StoryLikeID, story_likes.story_id AS StoryID, story_likes.like_type AS StoryLikeType,
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.story_likes
      JOIN authority.users ON story_likes.user_id = users.id
      WHERE story_likes.story_id = %s AND story_likes.id < %s
      ORDER BY story_likes.id DESC
      LIMIT 5
      ''' % (story_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    likes = []
    for record in results:
      like = {
        "id": record[0],
        "story_id": record[1],
        "like_type": record[2],
        "user": {
          "id": record[3],
          "displayname": record[4],
          "username": record[5],
          "icon_link": record[6],
          "wallpaper_link": record[7],
          "date_created": str(record[8]),
          "email": str(record[9]),
          "is_private": record[10],
          "uuid": record[11],
        }
      }
      likes.append(like)

    return likes

  return run_db_action(callback)

def get_book_likes(book_id, book_like_id):
  def callback(cursor):
    if book_like_id:
      query = '''
      SELECT book_likes.id AS BookLikeID, book_likes.book_id AS BookID, book_likes.like_type AS BookLikeType,
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_likes
      JOIN authority.users ON book_likes.user_id = users.id
      WHERE book_likes.book_id = %s AND book_likes.id < %s
      ORDER BY book_likes.id DESC
      LIMIT 5
      ''' % (book_id, book_like_id, )
    else:
      query = '''
      SELECT book_likes.id AS BookLikeID, book_likes.book_id AS BookID, book_likes.like_type AS BookLikeType,
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_likes
      JOIN authority.users ON book_likes.user_id = users.id
      WHERE book_likes.book_id = %s AND book_likes.id < %s
      ORDER BY book_likes.id DESC
      LIMIT 5
      ''' % (book_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    likes = []
    for record in results:
      like = {
        "id": record[0],
        "book_id": record[1],
        "like_type": record[2],
        "user": {
          "id": record[3],
          "displayname": record[4],
          "username": record[5],
          "icon_link": record[6],
          "wallpaper_link": record[7],
          "date_created": str(record[8]),
          "email": str(record[9]),
          "is_private": record[10],
          "uuid": record[11],
        }
      }
      likes.append(like)

    return likes

  return run_db_action(callback)

def get_book_page_likes(book_page_id, book_page_like_id):
  def callback(cursor):
    if book_page_like_id:
      query = '''
      SELECT book_page_likes.id AS BookPageLikeID, book_page_likes.book_page_id AS BookPageID, book_page_likes.like_type AS BookPageLikeType,
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_page_likes
      JOIN authority.users ON book_page_likes.user_id = users.id
      WHERE book_page_likes.book_page_id = %s AND book_page_likes.id < %s
      ORDER BY book_page_likes.id DESC
      LIMIT 5
      ''' % (book_page_id, book_page_like_id, )
    else:
      query = '''
      SELECT book_page_likes.id AS BookPageLikeID, book_page_likes.book_page_id AS BookPageID, book_page_likes.like_type AS BookPageLikeType,
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_page_likes
      JOIN authority.users ON book_page_likes.user_id = users.id
      WHERE book_page_likes.book_page_id = %s AND book_page_likes.id < %s
      ORDER BY book_page_likes.id DESC
      LIMIT 5
      ''' % (book_page_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    likes = []
    for record in results:
      like = {
        "id": record[0],
        "book_page_id": record[1],
        "like_type": record[2],
        "user": {
          "id": record[3],
          "displayname": record[4],
          "username": record[5],
          "icon_link": record[6],
          "wallpaper_link": record[7],
          "date_created": str(record[8]),
          "email": str(record[9]),
          "is_private": record[10],
          "uuid": record[11],
        }
      }
      likes.append(like)

    return likes

  return run_db_action(callback)

# 

def get_poem_comments(poem_id, comment_id):
  def callback(cursor):
    if comment_id:
      query = '''
      SELECT poem_comments.id AS PoemCommentID, poem_comments.owner_id AS PoemCommentOwnerID, 
        poem_comments.poem_id AS PoemID, poem_comments.date_created AS PoemCommentDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.poem_comments
      JOIN authority.users ON poem_comments.owner_id = users.id
      WHERE poem_comments.poem_id = %s AND poem_comments.id < %s
      ORDER BY poem_comments.id DESC
      LIMIT 5
      ''' % (poem_id, comment_id, )
    else:
      query = '''
      SELECT poem_comments.id AS PoemCommentID, poem_comments.owner_id AS PoemCommentOwnerID, 
        poem_comments.poem_id AS PoemID, poem_comments.date_created AS PoemCommentDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.poem_comments
      JOIN authority.users ON poem_comments.owner_id = users.id
      WHERE poem_comments.poem_id = %s
      ORDER BY poem_comments.id DESC
      LIMIT 5
      ''' % (poem_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    comments = []
    for record in results:
      comment = {
        "id": record[0],
        "poem_id": record[1],
        "body": record[2],
        "date_created": record[3],
        "user": {
          "id": record[4],
          "displayname": record[5],
          "username": record[6],
          "icon_link": record[7],
          "wallpaper_link": record[8],
          "date_created": str(record[9]),
          "email": str(record[10]),
          "is_private": record[11],
          "uuid": record[12],
        }
      }
      comments.append(comment)

    return comments

  return run_db_action(callback)

def get_story_comments(story_id, comment_id):
  def callback(cursor):
    if comment_id:
      query = '''
      SELECT story_comments.id AS StoryCommentID, story_comments.owner_id AS StoryCommentOwnerID, 
        story_comments.story_id AS StoryID, story_comments.date_created AS StoryCommentDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.story_comments
      JOIN authority.users ON story_comments.owner_id = users.id
      WHERE story_comments.story_id = %s AND story_comments.id < %s
      ORDER BY story_comments.id DESC
      LIMIT 5
      ''' % (story_id, comment_id, )
    else:
      query = '''
      SELECT story_comments.id AS StoryCommentID, story_comments.owner_id AS StoryCommentOwnerID, 
        story_comments.story_id AS StoryID, story_comments.date_created AS StoryCommentDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.story_comments
      JOIN authority.users ON story_comments.owner_id = users.id
      WHERE story_comments.story_id = %s
      ORDER BY story_comments.id DESC
      LIMIT 5
      ''' % (story_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    comments = []
    for record in results:
      comment = {
        "id": record[0],
        "story_id": record[1],
        "body": record[2],
        "date_created": record[3],
        "user": {
          "id": record[4],
          "displayname": record[5],
          "username": record[6],
          "icon_link": record[7],
          "wallpaper_link": record[8],
          "date_created": str(record[9]),
          "email": str(record[10]),
          "is_private": record[11],
          "uuid": record[12],
        }
      }
      comments.append(comment)

    return comments

  return run_db_action(callback)

def get_book_comments(book_id, comment_id):
  def callback(cursor):
    if comment_id:
      query = '''
      SELECT book_comments.id AS BookCommentID, book_comments.owner_id AS BookCommentOwnerID, 
        book_comments.book_id AS BookID, book_comments.date_created AS BookCommentDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_comments
      JOIN authority.users ON book_comments.owner_id = users.id
      WHERE book_comments.book_id = %s AND book_comments.id < %s
      ORDER BY book_comments.id DESC
      LIMIT 5
      ''' % (book_id, comment_id, )
    else:
      query = '''
      SELECT book_comments.id AS BookCommentID, book_comments.owner_id AS BookCommentOwnerID, 
        book_comments.book_id AS BookID, book_comments.date_created AS BookCommentDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_comments
      JOIN authority.users ON book_comments.owner_id = users.id
      WHERE book_comments.book_id = %s
      ORDER BY book_comments.id DESC
      LIMIT 5
      ''' % (book_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    comments = []
    for record in results:
      comment = {
        "id": record[0],
        "book_id": record[1],
        "body": record[2],
        "date_created": record[3],
        "user": {
          "id": record[4],
          "displayname": record[5],
          "username": record[6],
          "icon_link": record[7],
          "wallpaper_link": record[8],
          "date_created": str(record[9]),
          "email": str(record[10]),
          "is_private": record[11],
          "uuid": record[12],
        }
      }
      comments.append(comment)

    return comments

  return run_db_action(callback)

def get_book_page_comments(book_page_id, comment_id):
  def callback(cursor):
    if comment_id:
      query = '''
      SELECT book_page_comments.id AS BookPageCommentID, book_page_comments.owner_id AS BookPageCommentOwnerID, 
        book_page_comments.book_page_id AS BookPageID, book_page_comments.date_created AS BookPageCommentDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_page_comments
      JOIN authority.users ON book_page_comments.owner_id = users.id
      WHERE book_page_comments.book_page_id = %s AND book_page_comments.id < %s
      ORDER BY book_page_comments.id DESC
      LIMIT 5
      ''' % (book_page_id, comment_id, )
    else:
      query = '''
      SELECT book_page_comments.id AS BookPageCommentID, book_page_comments.owner_id AS BookPageCommentOwnerID, 
        book_page_comments.book_page_id AS BookPageID, book_page_comments.date_created AS BookPageCommentDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_page_comments
      JOIN authority.users ON book_page_comments.owner_id = users.id
      WHERE book_page_comments.book_page_id = %s
      ORDER BY book_page_comments.id DESC
      LIMIT 5
      ''' % (book_page_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    comments = []
    for record in results:
      comment = {
        "id": record[0],
        "book_page_id": record[1],
        "body": record[2],
        "date_created": record[3],
        "user": {
          "id": record[4],
          "displayname": record[5],
          "username": record[6],
          "icon_link": record[7],
          "wallpaper_link": record[8],
          "date_created": str(record[9]),
          "email": str(record[10]),
          "is_private": record[11],
          "uuid": record[12],
        }
      }
      comments.append(comment)

    return comments

  return run_db_action(callback)

# 

def get_poem_reviews(poem_id, review_id):
  def callback(cursor):
    if review_id:
      query = '''
      SELECT poem_reviews.id AS PoemReviewID, poem_reviews.poem_id AS PoemID, 
        poem_reviews.writer_id AS PoemReviewWriterId, poem_reviews.rating AS PoemReviewRating, 
        poem_reviews.summary AS PoemReviewSummary, poem_reviews.date_created AS PoemReviewDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.poem_reviews
      JOIN authority.users ON poem_reviews.owner_id = users.id
      WHERE poem_reviews.book_page_id = %s AND poem_reviews.id < %s
      ORDER BY poem_reviews.id DESC
      LIMIT 5
      ''' % (poem_id, review_id, )
    else:
      query = '''
      SELECT poem_reviews.id AS PoemReviewID, poem_reviews.poem_id AS PoemID, 
        poem_reviews.writer_id AS PoemReviewWriterId, poem_reviews.rating AS PoemReviewRating, 
        poem_reviews.summary AS PoemReviewSummary, poem_reviews.date_created AS PoemReviewDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.poem_reviews
      JOIN authority.users ON poem_reviews.owner_id = users.id
      WHERE poem_reviews.book_page_id = %s
      ORDER BY poem_reviews.id DESC
      LIMIT 5
      ''' % (poem_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    reviews = []
    for record in results:
      review = {
        "id": record[0],
        "poem_id": record[1],
        "writer_id": record[2],
        "rating": record[3],
        "summary": record[4],
        "date_created": record[5],
        "writer": {
          "id": record[6],
          "displayname": record[7],
          "username": record[8],
          "icon_link": record[9],
          "wallpaper_link": record[10],
          "date_created": str(record[11]),
          "email": str(record[12]),
          "is_private": record[13],
          "uuid": record[14],
        }
      }
      reviews.append(review)

    return reviews

  return run_db_action(callback)

def get_story_reviews(story_id, review_id):
  def callback(cursor):
    if review_id:
      query = '''
      SELECT story_reviews.id AS StoryReviewID, story_reviews.story_id AS StoryID, 
        story_reviews.writer_id AS StoryReviewWriterId, story_reviews.rating AS StoryReviewRating, 
        story_reviews.summary AS StoryReviewSummary, story_reviews.date_created AS StoryReviewDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.story_reviews
      JOIN authority.users ON story_reviews.owner_id = users.id
      WHERE story_reviews.book_page_id = %s AND story_reviews.id < %s
      ORDER BY story_reviews.id DESC
      LIMIT 5
      ''' % (story_id, review_id, )
    else:
      query = '''
      SELECT story_reviews.id AS StoryReviewID, story_reviews.story_id AS StoryID, 
        story_reviews.writer_id AS StoryReviewWriterId, story_reviews.rating AS StoryReviewRating, 
        story_reviews.summary AS StoryReviewSummary, story_reviews.date_created AS StoryReviewDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.story_reviews
      JOIN authority.users ON story_reviews.owner_id = users.id
      WHERE story_reviews.book_page_id = %s
      ORDER BY story_reviews.id DESC
      LIMIT 5
      ''' % (story_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    reviews = []
    for record in results:
      review = {
        "id": record[0],
        "story_id": record[1],
        "writer_id": record[2],
        "rating": record[3],
        "summary": record[4],
        "date_created": record[5],
        "writer": {
          "id": record[6],
          "displayname": record[7],
          "username": record[8],
          "icon_link": record[9],
          "wallpaper_link": record[10],
          "date_created": str(record[11]),
          "email": str(record[12]),
          "is_private": record[13],
          "uuid": record[14],
        }
      }
      reviews.append(review)

    return reviews

  return run_db_action(callback)

def get_book_reviews(book_id, review_id):
  def callback(cursor):
    if review_id:
      query = '''
      SELECT book_reviews.id AS BookReviewID, book_reviews.book_id AS BookID, 
        book_reviews.writer_id AS BookReviewWriterId, book_reviews.rating AS BookReviewRating, 
        book_reviews.summary AS BookReviewSummary, book_reviews.date_created AS BookReviewDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_reviews
      JOIN authority.users ON book_reviews.owner_id = users.id
      WHERE book_reviews.book_page_id = %s AND book_reviews.id < %s
      ORDER BY book_reviews.id DESC
      LIMIT 5
      ''' % (book_id, review_id, )
    else:
      query = '''
      SELECT book_reviews.id AS BookReviewID, book_reviews.book_id AS BookID, 
        book_reviews.writer_id AS BookReviewWriterId, book_reviews.rating AS BookReviewRating, 
        book_reviews.summary AS BookReviewSummary, book_reviews.date_created AS BookReviewDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_reviews
      JOIN authority.users ON book_reviews.owner_id = users.id
      WHERE book_reviews.book_page_id = %s
      ORDER BY book_reviews.id DESC
      LIMIT 5
      ''' % (book_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    reviews = []
    for record in results:
      review = {
        "id": record[0],
        "book_id": record[1],
        "writer_id": record[2],
        "rating": record[3],
        "summary": record[4],
        "date_created": record[5],
        "writer": {
          "id": record[6],
          "displayname": record[7],
          "username": record[8],
          "icon_link": record[9],
          "wallpaper_link": record[10],
          "date_created": str(record[11]),
          "email": str(record[12]),
          "is_private": record[13],
          "uuid": record[14],
        }
      }
      reviews.append(review)

    return reviews

  return run_db_action(callback)
def get_book_page_reviews(book_page_id, review_id):
  def callback(cursor):
    if review_id:
      query = '''
      SELECT book_page_reviews.id AS BookPageReviewID, book_page_reviews.book_page_id AS BookPageID, 
        book_page_reviews.writer_id AS BookPageReviewWriterId, book_page_reviews.rating AS BookPageReviewRating, 
        book_page_reviews.summary AS BookPageReviewSummary, book_page_reviews.date_created AS BookPageReviewDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_page_reviews
      JOIN authority.users ON book_page_reviews.owner_id = users.id
      WHERE book_page_reviews.book_page_page_id = %s AND book_page_reviews.id < %s
      ORDER BY book_page_reviews.id DESC
      LIMIT 5
      ''' % (book_page_id, review_id, )
    else:
      query = '''
      SELECT book_page_reviews.id AS BookPageReviewID, book_page_reviews.book_page_id AS BookPageID, 
        book_page_reviews.writer_id AS BookPageReviewWriterId, book_page_reviews.rating AS BookPageReviewRating, 
        book_page_reviews.summary AS BookPageReviewSummary, book_page_reviews.date_created AS BookPageReviewDateCreated, 
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_page_reviews
      JOIN authority.users ON book_page_reviews.owner_id = users.id
      WHERE book_page_reviews.book_page_page_id = %s
      ORDER BY book_page_reviews.id DESC
      LIMIT 5
      ''' % (book_page_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    reviews = []
    for record in results:
      review = {
        "id": record[0],
        "book_page_id": record[1],
        "writer_id": record[2],
        "rating": record[3],
        "summary": record[4],
        "date_created": record[5],
        "writer": {
          "id": record[6],
          "displayname": record[7],
          "username": record[8],
          "icon_link": record[9],
          "wallpaper_link": record[10],
          "date_created": str(record[11]),
          "email": str(record[12]),
          "is_private": record[13],
          "uuid": record[14],
        }
      }
      reviews.append(review)

    return reviews

  return run_db_action(callback)

# 

def get_message_senders(user_id, message_id):
  def callback(cursor):
    if not message_id:
      query = '''
      SELECT messages.id AS MsgID, messages.sender_id AS MsgSenderID,
        users.displayname AS SenderDisplayname, users.username AS SenderUsername, 
        users.icon_link AS SenderIconLink, users.date_created AS SenderDateCreated
      FROM authority.messages
      JOIN authority.users ON messages.sender_id = users.id 
      WHERE messages.recipient_id = %s
      GROUP BY messages.sender_id
      ORDER BY messages.id DESC
      LIMIT 5
      ''' % (user_id,)
    else:
      query = '''
      SELECT messages.id AS MsgID, messages.sender_id AS MsgSenderID,
        users.displayname AS SenderDisplayname, users.username AS SenderUsername, 
        users.icon_link AS SenderIconLink, users.date_created AS SenderDateCreated
      FROM authority.messages
      JOIN authority.users ON messages.sender_id = users.id 
      WHERE messages.recipient_id = %s AND messages.id < %s
      GROUP BY messages.sender_id
      ORDER BY messages.id DESC
      LIMIT 5
      ''' % (user_id, message_id)

    cursor.execute(query)
    results = cursor.fetchall()
    data_list = []

    for row in results:
      message_sender = {
        "id": row[0],
        "sender_id": row[1],
        "sender": {
          "id": row[1],
          "displayname": row[2],
          "username": row[3],
          "icon_link": row[4],
          "date_created": row[5],
        }
      }
      data_list.append(message_sender)

    return data_list

  return run_db_action(callback)

def get_messages_by_sender(user_id, sender_id, message_id):
  def callback(cursor):
    if not message_id:
      query = '''
      SELECT messages.id AS MsgID, messages.sender_id AS MsgSenderID, messages.recipient_id AS MsgRecipientID,
        messages.content AS MsgContent, messages.date_sent AS MsgDateSent, messages.date_read AS MsgDateRead,
        messages.uuid AS MsgUuid, messages.date_created AS MsgDateCreated,
        users.displayname AS SenderDisplayname, users.username AS SenderUsername, 
        users.icon_link AS SenderIconLink, users.date_created AS SenderDateCreated
      FROM authority.messages
      JOIN authority.users ON messages.sender_id = users.id 
      WHERE ((messages.recipient_id = %s AND messages.sender_id = %s) 
        OR (messages.recipient_id = %s AND messages.sender_id = %s))
      ORDER BY messages.id DESC
      LIMIT 5;
      ''' % (user_id, sender_id, sender_id, user_id)
    else:
      query = '''
      SELECT messages.id AS MsgID, messages.sender_id AS MsgSenderID, messages.recipient_id AS MsgRecipientID,
        messages.content AS MsgContent, messages.date_sent AS MsgDateSent, messages.date_read AS MsgDateRead,
        messages.uuid AS MsgUuid, messages.date_created AS MsgDateCreated,
        users.displayname AS SenderDisplayname, users.username AS SenderUsername, 
        users.icon_link AS SenderIconLink, users.date_created AS SenderDateCreated
      FROM authority.messages
      JOIN authority.users ON messages.sender_id = users.id 
      WHERE ((messages.recipient_id = %s AND messages.sender_id = %s) 
        OR (messages.recipient_id = %s AND messages.sender_id = %s)) 
        AND messages.id < %s 
      ORDER BY messages.id DESC
      LIMIT 5;
      ''' % (user_id, sender_id, sender_id, user_id, message_id)

    cursor.execute(query)
    results = cursor.fetchall()
    data_list = []

    for row in results:
      message = {
        "id": row[0],
        "sender_id": row[1],
        "recipient_id": row[2],
        "content": row[3],
        "date_sent": row[4],
        "date_read": row[5],
        "uuid": row[6],
        "date_created": row[7],
        "sender": {
          "id": row[1],
          "displayname": row[8],
          "username": row[9],
          "icon_link": row[10],
          "date_created": row[11],
        }
      }
      data_list.append(message)
      
    return data_list

  return run_db_action(callback)

# 
def get_latest_notifications(user_id, notification_id):
  def callback(cursor):
    if not notification_id:
      query = '''
      SELECT notifications.id AS NotesID, notifications.from_id AS NotesFromID, notifications.user_id AS NotesUserID,
        notifications.action_type AS NotesActionType, notifications.target_type AS NotesTargetType, 
        notifications.target_id AS NotesTargetID, notifications.link AS NotesLink,
        notifications.uuid AS NotesUuid, notifications.date_created AS NotesDateCreated,
        users.displayname AS FromDisplayname, users.username AS FromUsername, 
        users.icon_link AS FromIconLink, users.date_created AS FromDateCreated
      FROM notifications
      JOIN users ON notifications.from_id = users.id 
      WHERE notifications.user_id = %s
      ORDER BY notifications.id DESC
      LIMIT 5
      ''' % (user_id,)
    else:
      query = '''
      SELECT notifications.id AS NotesID, notifications.from_id AS NotesFromID, notifications.user_id AS NotesUserID,
        notifications.action_type AS NotesActionType, notifications.target_type AS NotesTargetType, 
        notifications.target_id AS NotesTargetID, notifications.link AS NotesLink,
        notifications.uuid AS NotesUuid, notifications.date_created AS NotesDateCreated,
        users.displayname AS FromDisplayname, users.username AS FromUsername, 
        users.icon_link AS FromIconLink, users.date_created AS FromDateCreated
      FROM notifications
      JOIN users ON notifications.from_id = users.id 
      WHERE notifications.user_id = %s AND notifications.id < %s
      ORDER BY notifications.id DESC
      LIMIT 5
      ''' % (user_id, notification_id)

    cursor.execute(query)
    results = cursor.fetchall()
    data_list = []

    for notes_row in results:
      data = {
        "id": notes_row[0],
        "from_id": notes_row[1],
        "user_id": notes_row[2],
        "action_type": notes_row[3],
        "target_type": notes_row[4],
        "target_id": notes_row[5],
        "link": notes_row[6],
        "uuid": notes_row[7],
        "date_created": notes_row[8],
        "from": {
          "id": notes_row[1],
          "displayname": notes_row[9],
          "username": notes_row[10],
          "icon_link": notes_row[11],
          "date_created": notes_row[12],
        },
      }

      apply_notification_message(data)
      data_list.append(data)

    return data_list

  return run_db_action(callback)

# 

def get_poems_slim_by_user(user_id, poem_id):
  def callback(cursor):
    if poem_id:
      query = '''
      SELECT poems.id AS PoemID, poems.owner_id AS PoemOwnerID, poems.title AS PoemTitle, 
        poems.body AS PoemBody, poems.image_id AS PoemImageID, poems.image_link AS PoemImageLink, 
        poems.tags AS PoemTags, poems.is_explicit AS PoemExplicit, poems.is_private AS PoemPrivate, 
        poems.uuid AS PoemUUID, poems.date_created AS PoemDateCreated, poems.last_edited AS PoemLastEdited, 
        
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.poems
      JOIN authority.users ON poems.owner_id = users.id
      WHERE poems.owner_id = %s AND poems.id < %s
      ORDER BY poems.id DESC
      LIMIT 5
      ''' % (user_id, poem_id, )
    else:
      query = '''
      SELECT poems.id AS PoemID, poems.owner_id AS PoemOwnerID, poems.title AS PoemTitle, 
        poems.body AS PoemBody, poems.image_id AS PoemImageID, poems.image_link AS PoemImageLink, 
        poems.tags AS PoemTags, poems.is_explicit AS PoemExplicit, poems.is_private AS PoemPrivate, 
        poems.uuid AS PoemUUID, poems.date_created AS PoemDateCreated, poems.last_edited AS PoemLastEdited, 
        
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.poems
      JOIN authority.users ON poems.owner_id = users.id
      WHERE poems.owner_id = %s
      ORDER BY poems.id DESC
      LIMIT 5
      ''' % (user_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    poems = []

    for result in results:
      poem = {
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
        }
      }
      poems.append(poem)

    return poems
  
  return run_db_action(callback)

def get_stories_slim_by_user(user_id, story_id):
  def callback(cursor):
    if story_id:
      query = '''
      SELECT stories.id AS StoryID, stories.owner_id AS StoryOwnerID, stories.title AS StoryTitle, 
        stories.body AS StoryBody, stories.image_id AS StoryImageID, stories.image_link AS StoryImageLink, 
        stories.tags AS StoryTags, stories.is_explicit AS StoryExplicit, stories.is_private AS StoryPrivate, 
        stories.uuid AS StoryUUID, stories.date_created AS StoryDateCreated, stories.last_edited AS StoryLastEdited, 
        
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.stories
      JOIN authority.users ON stories.owner_id = users.id
      WHERE stories.owner_id = %s AND stories.id < %s
      ORDER BY stories.id DESC
      LIMIT 5
      ''' % (user_id, story_id, )
    else:
      query = '''
      SELECT stories.id AS StoryID, stories.owner_id AS StoryOwnerID, stories.title AS StoryTitle, 
        stories.body AS StoryBody, stories.image_id AS StoryImageID, stories.image_link AS StoryImageLink, 
        stories.tags AS StoryTags, stories.is_explicit AS StoryExplicit, stories.is_private AS StoryPrivate, 
        stories.uuid AS StoryUUID, stories.date_created AS StoryDateCreated, stories.last_edited AS StoryLastEdited, 
        
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.stories
      JOIN authority.users ON stories.owner_id = users.id
      WHERE stories.owner_id = %s
      ORDER BY stories.id DESC
      LIMIT 5
      ''' % (user_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    stories = []

    for result in results:
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
        }
      }
      stories.append(story)

    return stories
  
  return run_db_action(callback)

def get_books_slim_by_user(user_id, book_id):
  def callback(cursor):
    if book_id:
      query = '''
      SELECT books.id AS BookID, books.owner_id AS BookOwnerID, books.title AS BookTitle, 
        books.body AS BookBody, books.image_id AS BookImageID, books.image_link AS BookImageLink, 
        books.tags AS BookTags, books.is_explicit AS BookExplicit, books.is_private AS BookPrivate, 
        books.uuid AS BookUUID, books.date_created AS BookDateCreated, books.last_edited AS BookLastEdited, 
        
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.books
      JOIN authority.users ON books.owner_id = users.id
      WHERE books.owner_id = %s AND books.id < %s
      ORDER BY books.id DESC
      LIMIT 5
      ''' % (user_id, book_id, )
    else:
      query = '''
      SELECT books.id AS BookID, books.owner_id AS BookOwnerID, books.title AS BookTitle, 
        books.body AS BookBody, books.image_id AS BookImageID, books.image_link AS BookImageLink, 
        books.tags AS BookTags, books.is_explicit AS BookExplicit, books.is_private AS BookPrivate, 
        books.uuid AS BookUUID, books.date_created AS BookDateCreated, books.last_edited AS BookLastEdited, 
        
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.books
      JOIN authority.users ON books.owner_id = users.id
      WHERE books.owner_id = %s
      ORDER BY books.id DESC
      LIMIT 5
      ''' % (user_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    books = []

    for result in results:
      book = {
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
        }
      }
      books.append(book)

    return books
  
  return run_db_action(callback)

def get_book_pages_slim_by_book(book_id, book_page_id):
  def callback(cursor):
    if book_page_id:
      query = '''
      SELECT book_pages.id AS BookPageID, book_pages.owner_id AS BookPageOwnerID, book_pages.title AS BookPageTitle, 
        book_pages.body AS BookPageBody, book_pages.image_id AS BookPageImageID, book_pages.image_link AS BookPageImageLink, 
        book_pages.tags AS BookPageTags, book_pages.is_explicit AS BookPageExplicit, book_pages.is_private AS BookPagePrivate, 
        book_pages.uuid AS BookPageUUID, book_pages.date_created AS BookPageDateCreated, book_pages.last_edited AS BookPageLastEdited, 
        
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_pages
      JOIN authority.users ON book_pages.owner_id = users.id
      WHERE book_pages.book_id = %s AND book_pages.id > %s
      ORDER BY book_pages.id ASC
      LIMIT 5
      ''' % (book_id, book_page_id, )
    else:
      query = '''
      SELECT book_pages.id AS BookPageID, book_pages.owner_id AS BookPageOwnerID, book_pages.book_id AS BookID, 
        book_pages.body AS BookPageBody, book_pages.image_id AS BookPageImageID, book_pages.image_link AS BookPageImageLink, 
        book_pages.tags AS BookPageTags, book_pages.is_explicit AS BookPageExplicit, book_pages.is_private AS BookPagePrivate, 
        book_pages.uuid AS BookPageUUID, book_pages.date_created AS BookPageDateCreated, book_pages.last_edited AS BookPageLastEdited, 
        
        users.id AS OwnerID, users.displayname AS OwnerDisplayname, users.username AS OwnerUsername, 
        users.icon_link AS OwnerIconLink, users.wallpaper_link AS OwnerWallpaperLink, 
        users.date_created AS OwnerDateCreated, users.email AS OwnerEmail, 
        users.is_private AS OwnerPrivate, users.uuid AS OwnerUUID
      FROM authority.book_pages
      JOIN authority.users ON book_pages.owner_id = users.id
      WHERE book_pages.book_id = %s
      ORDER BY book_pages.id ASC
      LIMIT 5
      ''' % (book_id, )

    cursor.execute(query)
    results = cursor.fetchall()
    book_pages = []

    for result in results:
      book_page = {
        "id": result[0],
        "owner_id": result[1],
        "book_id": result[2],
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
        }
      }
      book_pages.append(book_page)

    return book_pages
  
  return run_db_action(callback)
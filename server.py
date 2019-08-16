import sqlite3, json, random, string, os, json

from functools import wraps
from datetime import timedelta
from threading import Timer
from werkzeug.utils import secure_filename

from flask import Flask
from flask import request, redirect, jsonify, send_from_directory
from flask import session as user_session, make_response, render_template

from flask_socketio import SocketIO

from chamber import uniqueValue, check_password, check_value_type, uploadFile
from chamber import allowed_photo, VALID_RATINGS, VALID_CONTENT_TYPES

import db_select_queries
import db_insert_queries
import db_update_queries
import db_delete_queries



# --- ----- --- #
# --- Setup --- #
# --- ----- --- #

app = Flask(__name__)
app.config['SECRET_KEY'] = 'DF6Y#6G15$B^*R&&NT*Y(U)I_+DF&D((A-_*DFj/YR'
socketio = SocketIO(app)

def login_required(f):
  ''' Checks If User Is Logged In '''
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if 'session_id' in user_session:
      return f(*args, **kwargs)
    else:
      # flash('Please Log In To Use This Site.')
      return redirect('/signin')
  return decorated_function

def ajax_login_required(f):
  ''' Checks If User Is Logged In '''
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if 'session_id' in user_session:
      return f(*args, **kwargs)
    else:
      return jsonify(error = True, message = 'Not signed in')
  return decorated_function

# --- ------ --- #
# --- Routes --- #
# --- ------ --- #



# --- GET --- #

# Pages

def error_page(error_message):
  user_session['error_message'] = error_message
  return redirect('/error')

def get_user_by_value(user_value):
  is_int = isinstance(user_value, int)
  is_str = isinstance(user_value, str)

  if is_int:
    return db_select_queries.get_user_by_id(user_value)
  if is_str:
    return db_select_queries.get_user_by_username(user_value)
  return None

def process_image(request_files, input_name):
  if input_name not in request_files:
    return False

  input_file = request_files[input_name]

  if input_file:
    is_image_valid = input_file and input_file.filename != '' and allowed_photo(input_file.filename)
    if not is_image_valid:
      raise
    else:
      icon_res = uploadFile(input_file)
      image_dict = {
        "image_id": icon_res["upload_result"]["public_id"],
        "image_link": icon_res["upload_result"]["secure_url"]
      }
      return image_dict
  else:
    return False




@app.route('/', methods=['GET'])
def welcome():
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  if logged_in:
    home_page_route = '/users/' + user_session['you_username']
    return redirect(home_page_route)
  return render_template('welcome.html', logged_in = logged_in, you_id = you_id)

@app.route('/error', methods=['GET'])
def error():
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  
  return render_template(
    'error-page.html', 
    logged_in = logged_in, 
    you_id = you_id,
    error_message = user_session['error_message'],
  )

@app.route('/signin', methods=['GET'])
def signin():
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  if logged_in:
    home_page_route = '/users/' + user_session['you_username']
    return redirect(home_page_route)
  return render_template('signin.html', logged_in = logged_in, you_id = you_id)

@app.route('/signup', methods=['GET'])
def signup():
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  if logged_in:
    home_page_route = '/users/' + user_session['you_username']
    return redirect(home_page_route)
  return render_template('signup.html', logged_in = logged_in, you_id = you_id)

@app.route('/signout', methods=['GET'])
def signout():
  user_session.clear()
  return redirect('/')


@app.route('/settings', methods=['GET'])
@login_required
def settings_page():
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('settings-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/create/poem', methods=['GET'])
@login_required
def create_poem_page():
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('create-poem-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/create/story', methods=['GET'])
@login_required
def create_story_page():
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('create-story-page.html', logged_in = logged_in, you_id = you_id)

# @app.route('/create/book', methods=['GET'])
# @login_required
# def create_book_page():
#   logged_in = True if 'session_id' in user_session else False
#   you_id = user_session['you_id'] if 'you_id' in user_session else False
#   return render_template('create-book-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/create/book/<int:book_id>/page', methods=['GET'])
@login_required
def create_book_page_page(book_id):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('create-book-page-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/users/<user_value>', methods=['GET'])
def users_home_page(user_value):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('user-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/users/<user_value>/poems', methods=['GET'])
def users_poems_list_page(user_value):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('user-poems-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/users/<user_value>/stories', methods=['GET'])
def users_stories_list_page(user_value):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('user-stories-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/users/<user_value>/books', methods=['GET'])
def users_books_list_page(user_value):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('user-books-page.html', logged_in = logged_in, you_id = you_id)



@app.route('/poems', methods=['GET'])
def poems_list_page():
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('poems-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/poems/<int:poem_id>', methods=['GET'])
def poem_page(poem_id):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('poem-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/stories', methods=['GET'])
def stories_list_page():
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('stories-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/stories/<int:story_id>', methods=['GET'])
def story_page(story_id):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('story-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/books', methods=['GET'])
def books_list_page(user_value):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('books-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/books/<int:book_id>', methods=['GET'])
def book_page(user_value, book_id):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('book-page.html', logged_in = logged_in, you_id = you_id)

@app.route('/books/<int:book_id>/pages/<int:book_page_id>', methods=['GET'])
def book_page_page(user_value, book_id, book_page_id):
  logged_in = True if 'session_id' in user_session else False
  you_id = user_session['you_id'] if 'you_id' in user_session else False
  return render_template('book-page-page.html', logged_in = logged_in, you_id = you_id)


# AJAX

@app.route('/check_session', methods=['GET'])
def check_session():
  if 'session_id' in user_session:
    return jsonify(online = True, user = user_session['you'])
  else:
    return jsonify(online = False)

@app.route('/get_user_by_username/<string:username>', methods=['GET'])
def get_user_by_username(username):
  user = db_select_queries.get_user_by_username(username)
  return jsonify(user = user)

@app.route('/get_user_by_id/<int:user_id>', methods=['GET'])
def get_user_by_id(user_id):
  user = db_select_queries.get_user_by_id(user_id)
  return jsonify(user = user)

@app.route('/get_user_profile_by_username/<string:username>', methods=['GET'])
def get_user_profile_by_username(username):
  user = db_select_queries.get_user_profile_by_username(username)
  return jsonify(user = user)

@app.route('/get_user_profile_by_id/<int:user_id>', methods=['GET'])
def get_user_profile_by_id(user_id):
  user = db_select_queries.get_user_profile_by_id(user_id)
  return jsonify(user = user)

@app.route('/get_user_by_username_or_id/<value>', methods=['GET'])
def get_user_by_username_or_id(value):
  val = str(value).encode('utf-8')
  try:
    user = db_select_queries.get_user_by_id(int(val))
  except Exception as err1:
    print('error: ', err1)
    try:
      user = db_select_queries.get_user_by_username(val)
    except Exception as err2:
      print('error: ', err2)
      pass

  return jsonify(user = user)

@app.route('/get_poem_full_by_id/<int:poem_id>', methods=['GET'])
def get_poem_full_by_id(poem_id):
  poem = db_select_queries.get_poem_full_by_id(poem_id)
  return jsonify(poem = poem)

@app.route('/get_story_full_by_id/<int:story_id>', methods=['GET'])
def get_story_full_by_id(story_id):
  story = db_select_queries.get_story_full_by_id(story_id)
  return jsonify(story = story)

@app.route('/get_random_users', methods=['GET'])
def get_random_users():
  users = db_select_queries.get_random_users()
  return jsonify(users = users)

@app.route('/get_random_poems', methods=['GET'])
def get_random_poems():
  poems = db_select_queries.get_random_poems()
  return jsonify(poems = poems)

@app.route('/get_random_stories', methods=['GET'])
def get_random_stories():
  stories = db_select_queries.get_random_stories()
  return jsonify(stories = stories)

@app.route('/search_users_by_criteria/<string:field>/<string:value>', methods=['GET'])
def search_users_by_criteria(field, value):
  users = db_select_queries.search_users_by_criteria(field, value)
  return jsonify(users = users)

@app.route('/get_random/<string:content_type>', methods=['GET'])
def get_random_content_by_type(content_type):
  if content_type not in VALID_CONTENT_TYPES:
    return jsonify(
      error = True,
      message = '''Unknown content type: '%s' ''' % (content_type, )
    )

  if content_type == 'poems':
    poems = db_select_queries.get_random_poems()
    return jsonify(poems = poems)

  if content_type == 'stories':
    stories = db_select_queries.get_random_stories()
    return jsonify(stories = stories)

  if content_type == 'books':
    books = db_select_queries.get_random_books()
    return jsonify(books = books)

@app.route('/search_by_title/<string:content_type>', methods=['GET'])
def get_random_content_by_title(content_type):
  if content_type not in VALID_CONTENT_TYPES:
    return jsonify(
      error = True,
      message = '''Unknown content type: '%s' ''' % (content_type, )
    )

  title_query = request.args.get('title')
  if not title_query:
    return jsonify(
      error = True,
      message = "'title' was empty from url query param"
    )

  if content_type == 'poems':
    poems = db_select_queries.get_random_poems_by_title(title_query)
    return jsonify(poems = poems)

  if content_type == 'stories':
    stories = db_select_queries.get_random_stories_by_title(title_query)
    return jsonify(stories = stories)

  if content_type == 'books':
    books = db_select_queries.get_random_books_by_title(title_query)
    return jsonify(books = books)

@app.route('/search_by_tag/<string:content_type>', methods=['GET'])
def get_random_content_by_tag(content_type):
  if content_type not in VALID_CONTENT_TYPES:
    return jsonify(
      error = True,
      message = '''Unknown content type: '%s' ''' % (content_type, )
    )

  tag_query = request.args.get('tag')
  if not tag_query:
    return jsonify(
      error = True,
      message = "'tag' was empty from url query param"
    )

  if content_type == 'poems':
    poems = db_select_queries.get_random_poems_by_tag(tag_query)
    return jsonify(poems = poems)

  if content_type == 'stories':
    stories = db_select_queries.get_random_stories_by_tag(tag_query)
    return jsonify(stories = stories)

  if content_type == 'books':
    books = db_select_queries.get_random_books_by_tag(tag_query)
    return jsonify(books = books)



# --- POST --- #


@app.route('/sign_up', methods=['POST'])
def sign_up():
  form_dict = {
    "displayname": str(request.form['displayname']).encode('utf-8'),
    "username": str(request.form['username']).encode('utf-8'),
    "email": str(request.form['email']).encode('utf-8'),
    "password": str(request.form['password']).encode('utf-8'),
  }

  password = str(form_dict['password']).encode('utf-8')
  password_confirm = str(request.form['password_confirm']).encode('utf-8')
  passwords_do_not_match = password != password_confirm

  if passwords_do_not_match:
    return jsonify(error = True, message = 'passwords do not match')

  check_username = db_select_queries.check_user_by_username(form_dict['username'])
  if check_username:
    return jsonify(error = True, message = 'username already in use')

  check_email = db_select_queries.check_user_by_email(form_dict['email'])
  if check_email:
    return jsonify(error = True, message = 'email already in use')

  new_user_id = db_insert_queries.create_new_user(form_dict)
  new_user = db_select_queries.get_user_by_username(form_dict['username'])

  user_session['session_id'] = uniqueValue()
  user_session['you_id'] = new_user_id
  user_session['you_username'] = form_dict['username']
  user_session['you'] = new_user

  return jsonify(
    message = 'Signed Up Successfully!', 
    success = True, 
    new_user_id = user_session['you_id'],
    new_username = user_session['you_username'],
  )

@app.route('/create_poem', methods=['POST'])
def create_poem():
  if 'title' not in request.form:
    return jsonify(error = True, message = 'title is required')

  if 'body' not in request.form:
    return jsonify(error = True, message = 'body is required')

  if not request.form['title']:
    return jsonify(error = True, message = 'title is required')

  if not request.form['body']:
    return jsonify(error = True, message = 'body is required')

  try:
    title = request.form['title'].decode()
    body = request.form['body'].decode()
  except Exception as e:
    print(e)
    raise e 
    return

  form_dict = {
    "title": title,
    "body": body,
  }

  if 'tags' in request.form:
    form_dict['tags'] = str(request.form['tags']).encode('utf-8')
    if form_dict['tags']:
      if len(form_dict['tags']) > 100:
        return jsonify(error = True, message = 'tags input max of 100 characters exceeded')
  else:
    form_dict['tags'] = ''

  if 'explicit' in request.form:
    if request.form['explicit'] == 'yes':
      form_dict['is_explicit'] = True
    else:
      form_dict['is_explicit'] = False
  else:
    form_dict['is_explicit'] = False

  if 'visibility' in request.form:
    if request.form['visibility'] == 'private':
      form_dict['is_private'] = True
    else:
      form_dict['is_private'] = False
  else:
    form_dict['is_private'] = False

  poem_icon_file = request.files['poem-icon']
  if poem_icon_file:
    is_image_valid = poem_icon_file and poem_icon_file.filename != '' and allowed_photo(poem_icon_file.filename)
    if not is_image_valid:
      return jsonify(error = True, message = 'file not valid')
    else:
      icon_res = uploadFile(poem_icon_file)
      print('icon_res', icon_res)
      form_dict['image_id'] = icon_res["upload_result"]["public_id"]
      form_dict['image_link'] = icon_res["upload_result"]["secure_url"]
  else:
    form_dict['image_id'] = ''
    form_dict['image_link'] = ''

  new_poem_id = db_insert_queries.create_new_poem(form_dict, user_session['you'])
  poem = db_select_queries.get_poem_full_by_id(new_poem_id)
  return jsonify(message = 'Poem Created Successfully!', poem = poem)

@app.route('/create_story', methods=['POST'])
def create_story():
  if 'title' not in request.form:
    return jsonify(error = True, message = 'title is required')

  if 'body' not in request.form:
    return jsonify(error = True, message = 'body is required')

  if not request.form['title']:
    return jsonify(error = True, message = 'title is required')

  if not request.form['body']:
    return jsonify(error = True, message = 'body is required')

  try:
    title = request.form['title'].decode()
    body = request.form['body'].decode()
  except Exception as e:
    print(e)
    raise e 
    return

  form_dict = {
    "title": title,
    "body": body,
  }

  if 'tags' in request.form:
    form_dict['tags'] = str(request.form['tags']).encode('utf-8')
    if form_dict['tags']:
      if len(form_dict['tags']) > 100:
        return jsonify(error = True, message = 'tags input max of 100 characters exceeded')
  else:
    form_dict['tags'] = ''

  if 'explicit' in request.form:
    if request.form['explicit'] == 'yes':
      form_dict['is_explicit'] = True
    else:
      form_dict['is_explicit'] = False
  else:
    form_dict['is_explicit'] = False

  if 'visibility' in request.form:
    if request.form['visibility'] == 'private':
      form_dict['is_private'] = True
    else:
      form_dict['is_private'] = False
  else:
    form_dict['is_private'] = False

  story_icon_file = request.files['story-icon']
  if story_icon_file:
    is_icon_valid = story_icon_file and story_icon_file.filename != '' and allowed_photo(story_icon_file.filename)
    if not is_icon_valid:
      return jsonify(error = True, message = 'file not valid')
    else:
      icon_res = uploadFile(story_icon_file)
      print('icon_res', icon_res)
      form_dict['image_id'] = icon_res["upload_result"]["public_id"]
      form_dict['image_link'] = icon_res["upload_result"]["secure_url"]
  else:
    form_dict['image_id'] = ''
    form_dict['image_link'] = ''

  new_story_id = db_insert_queries.create_new_story(form_dict, user_session['you'])
  story = db_select_queries.get_story_full_by_id(new_story_id)
  return jsonify(message = 'Story Created Successfully!', story = story)

@app.route('/create_book', methods=['POST'])
def create_book():
  if 'title' not in request.form:
    return jsonify(error = True, message = 'title is required')

  if 'summary' not in request.form:
    return jsonify(error = True, message = 'summary is required')

  if not request.form['title']:
    return jsonify(error = True, message = 'title is required')

  if not request.form['summary']:
    return jsonify(error = True, message = 'summary is required')

  try:
    title = request.form['title'].decode()
    summary = request.form['summary'].decode()
  except Exception as e:
    print(e)
    raise e 
    return

  form_dict = {
    "title": title,
    "summary": summary,
  }

  if 'tags' in request.form:
    form_dict['tags'] = str(request.form['tags']).encode('utf-8')
    if form_dict['tags']:
      if len(form_dict['tags']) > 100:
        return jsonify(error = True, message = 'tags input max of 100 characters exceeded')
  else:
    form_dict['tags'] = ''

  if 'explicit' in request.form:
    if request.form['explicit'] == 'yes':
      form_dict['is_explicit'] = True
    else:
      form_dict['is_explicit'] = False
  else:
    form_dict['is_explicit'] = False

  if 'visibility' in request.form:
    if request.form['visibility'] == 'private':
      form_dict['is_private'] = True
    else:
      form_dict['is_private'] = False
  else:
    form_dict['is_private'] = False

  try:
    upload_book_cover = process_image(request.files, 'book-icon-cover')
    form_dict['cover_image_id'] = upload_book_cover["image_id"] if upload_book_cover else ''
    form_dict['cover_image_link'] = upload_book_cover["image_link"] if upload_book_cover else ''
  except Exception as E:
    print('Error: ', E)
    return jsonify(error = True, message = 'could not process given cover image file')

  try:
    upload_book_back = process_image(request.files, 'book-icon-back')
    form_dict['back_image_id'] = upload_book_back["image_id"] if upload_book_back else ''
    form_dict['back_image_link'] = upload_book_back["image_link"] if upload_book_back else ''
  except Exception as E:
    print('Error: ', E)
    return jsonify(error = True, message = 'could not process given back image file')

  new_book_id = db_insert_queries.create_new_book(form_dict, user_session['you'])
  book = db_select_queries.get_book_full_by_id(new_book_id)
  return jsonify(message = 'Book Created Successfully!', book = book)




# --- PUT --- #



@app.route('/sign_in', methods=['PUT'])
def sign_in():
  email = request.form['email']
  password = request.form['password']
  check_user = db_select_queries.check_user_by_email(email)

  if not check_user:
    return jsonify(error = True, message = 'invalid credentials')

  pw_check = check_password(password, check_user['password'])
  if not pw_check:
    return jsonify(error = True, message = 'invalid credentials')

  user = db_select_queries.get_user_by_username(check_user['username'])

  user_session['session_id'] = uniqueValue()
  user_session['you_id'] = user["id"]
  user_session['you_username'] = user['username']
  user_session['you'] = user

  return jsonify(
    message = 'Signed In Successfully!', 
    success = True, 
    user_id = user_session['you_id'],
    username = user_session['you_username'],
  )

@app.route('/update_account', methods=['PUT'])
def update_account():
  if 'displayname' not in request.form:
    return jsonify(error = True, message = 'displayname is required')

  if 'username' not in request.form:
    return jsonify(error = True, message = 'username is required')

  if 'email' not in request.form:
    return jsonify(error = True, message = 'email is required')

  form_dict = {
    "displayname": str(request.form['displayname']).encode('utf-8'),
    "username": str(request.form['username']).encode('utf-8'),
    "email": str(request.form['email']).encode('utf-8'),
  }

  if 'weblink' in request.form:
    form_dict['weblink'] = str(request.form['weblink']).encode('utf-8')

  if 'bio' in request.form:
    form_dict['bio'] = str(request.form['bio']).encode('utf-8')

  if form_dict['bio']:
    if len(form_dict['bio']) > 100:
      return jsonify(error = True, message = 'bio input max of 100 characters exceeded')

  if 'tags' in request.form:
    form_dict['tags'] = str(request.form['tags']).encode('utf-8')

  if form_dict['tags']:
    if len(form_dict['tags']) > 100:
      return jsonify(error = True, message = 'tags input max of 100 characters exceeded')

  if 'visibility' in request.form:
    if request.form['visibility'] == 'private':
      form_dict['visibility'] = True
    else:
      form_dict['visibility'] = False
  else:
    form_dict['visibility'] = False

  if 'password' in request.form:
    if 'old_password' not in request.form:
      return jsonify(error = True, message = 'old_password input is required')
    if 'password_confirm' not in request.form:
      return jsonify(error = True, message = 'password_confirm input is required')
    old_password = str(request.form['old_password']).encode('utf-8')
    password = str(request.form['password']).encode('utf-8')
    password_confirm = str(request.form['password_confirm']).encode('utf-8')
    if not password:
      if old_password or password_confirm:
        return jsonify(error = True, message = 'all password inputs are required when changing password')
    if password:
      if not old_password:
        return jsonify(error = True, message = 'old_password input is empty/invalid')
      check_user = db_select_queries.check_user_by_email(user_session['you']['email'])
      pw_check = check_password(old_password, check_user['password'])
      if not pw_check:
        return jsonify(error = True, message = 'old password is invalid')
      passwords_do_not_match = password != password_confirm
      if passwords_do_not_match:
        return jsonify(error = True, message = 'new passwords do not match')
      form_dict['password'] = password

  email_changed = form_dict['email'] and form_dict['email'] != user_session['you']['email']
  if email_changed:
    check_email = db_select_queries.check_user_by_email(form_dict['email'])
    if check_email:
      return jsonify(error = True, message = 'email already in use')
  else:
    del form_dict['email']

  username_changed = form_dict['username'] and form_dict['username'] != user_session['you']['username']
  if username_changed:
    check_username = db_select_queries.check_user_by_username(form_dict['username'])
    if check_username:
      return jsonify(error = True, message = 'username already in use')
  else:
    del form_dict['username']

  profile_icon_file = request.files['profile-icon']
  if profile_icon_file:
    is_icon_valid = profile_icon_file and profile_icon_file.filename != '' and allowed_photo(profile_icon_file.filename)
    if not is_icon_valid:
      return jsonify(error = True, message = 'file not valid')
    else:
      icon_res = uploadFile(profile_icon_file)
      print('icon_res', icon_res)
      form_dict['icon_id_old'] = user_session['you']['icon_id']
      form_dict['icon_id'] = icon_res["upload_result"]["public_id"]
      form_dict['icon_link'] = icon_res["upload_result"]["secure_url"]

  profile_wallpaper_file = request.files['profile-wallpaper']
  if profile_wallpaper_file:
    is_wallpaper_valid = profile_wallpaper_file and profile_wallpaper_file.filename != '' and allowed_photo(profile_wallpaper_file.filename)
    if not is_wallpaper_valid:
      return jsonify(error = True, message = 'file not valid')
    else:
      wallpaper_res = uploadFile(profile_wallpaper_file)
      print('wallpaper_res', wallpaper_res)
      form_dict['wallpaper_id_old'] = user_session['you']['wallpaper_id']
      form_dict['wallpaper_id'] = wallpaper_res["upload_result"]["public_id"]
      form_dict['wallpaper_link'] = wallpaper_res["upload_result"]["secure_url"]

  db_update_queries.update_account(form_dict, user_session['you'])
  user_updated = db_select_queries.get_user_by_id(user_session['you_id'])
  user_session['you_username'] = user_updated['username']
  user_session['you'] = user_updated
  return jsonify(message = 'Updated Successfully!', user = user_updated)
  




# --- DELETE --- #
  



# --- API --- #




# --- ----- --- #
# --- Start --- #
# --- ----- --- #

if __name__ == '__main__':
  app.debug = True
  socketio.run(app)
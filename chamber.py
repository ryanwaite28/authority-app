import string, random, os, psycopg2, uuid, bcrypt, re

import sendgrid, cloudinary
from sendgrid.helpers.mail import *
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url

from dotenv import load_dotenv
load_dotenv()

DATABASE_URL = os.environ.get('DATABASE_URL')
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

CLOUDINARY_URL = os.getenv('CLOUDINARY_URL')
CLOUDINARY_API_KEY = os.getenv('CLOUDINARY_API_KEY')
CLOUDINARY_API_SECRET = os.getenv('CLOUDINARY_API_SECRET')
CLOUDINARY_CLOUD_NAME = os.getenv('CLOUDINARY_CLOUD_NAME')

cloudinary_env_proper = (
  CLOUDINARY_API_KEY and CLOUDINARY_API_SECRET and CLOUDINARY_CLOUD_NAME
)

if cloudinary_env_proper:
  cloudinary.config(
    cloud_name = CLOUDINARY_CLOUD_NAME, 
    api_key = CLOUDINARY_API_KEY, 
    api_secret = CLOUDINARY_API_SECRET
  )

sg = None
if SENDGRID_API_KEY:
  sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)

ALLOWED_PHOTOS = set(['png', 'jpg', 'jpeg', 'gif', 'PNG', 'JPG', 'JPEG', 'GIF'])
VALID_RATINGS = set([1, 2, 3, 4, 5])
VALID_CONTENT_TYPES = set(['poems', 'stories', 'books'])

default_icon = '/static/img/anon.png'
default_wallpaper = '/static/img/blank.png'



def allowed_photo(filename):
  return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_PHOTOS

def uniqueValue():
  value = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(50))
  return value.lower()

def check_value_type(value):
  is_int = isinstance(value, int)
  is_str = isinstance(value, str) 
  is_unicode = type(value) == unicode 

  print('is_int', is_int)
  print('is_str', is_str)
  print('is_unicode', is_unicode)

  if is_int:
    return int
  if is_str or is_unicode:
    return str

  return False

def get_connection():
  return psycopg2.connect(DATABASE_URL)

def run_db_action(callback_fn):
  try:
    DB = get_connection()
    cursor = DB.cursor()
    result = callback_fn(cursor)
    DB.commit()
    DB.close()
    print('committed and closed successfully. result - ', result)
    return result

  except Exception as e:
    print('error: ', e)
    if DB:
      DB.close()
    raise e

def get_new_uuid1():
  UUID = uuid.uuid1()
  return UUID

def make_password(password):
  hashed = bcrypt.hashpw(str(password).encode(), bcrypt.gensalt())
  return hashed

def check_password(password_entered, password_stored):
  check = bcrypt.checkpw(str(password_entered).encode(), password_stored.encode())
  return check

def isValidEmail(email):
  if re.match("[\w.-]+@[\w.-]+", email) != None:
    return True
  else:
    return False


def uploadFile(file, old_id = None):
  try:
    if not file:
      print('no file...')
      return False
    if not cloudinary_env_proper:
      print('cloudinary env not proper...')
      return False

    upload_result = upload(file)
    thumbnail_url1, options = cloudinary_url(upload_result['public_id'], format="jpg", crop="fill", width=200, height=200)

    data_dict = {
      "upload_result": upload_result,
      "thumbnail_url1": thumbnail_url1,
      "options": options
    }

    return data_dict

  except Exception(e):
    print("error - ", e)
    return False

def send_email(email, subject, mimetype, body):
  try:
    from_email = Email("app113835630@heroku.com")
    to_email = Email(email)
    subject = subject
    content = Content(mimetype, body)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body = mail.get())

    print("response", response)
    return {"error": None, "successful": True, "response": response}

  except Exception as err:
    print(err)
    return {"error": err, "successful": False}
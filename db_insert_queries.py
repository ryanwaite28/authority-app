import datetime
from chamber import run_db_action
from chamber import get_new_uuid1, make_password
from chamber import default_icon, default_wallpaper

def create_new_user(form_dict):
  def callback(cursor):
    displayname = str(form_dict['displayname']).encode()
    username = str(form_dict['username']).encode()
    email = str(form_dict['email']).encode()
    password = make_password(form_dict['password'])

    uuid = get_new_uuid1()
    date_created = str(datetime.datetime.today())

    query = '''
    INSERT INTO authority.users (displayname, username, email, pswrd, icon_link, wallpaper_link, uuid, date_created)
    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s') RETURNING id
    ''' % (displayname, username, email, password, default_icon, default_wallpaper, uuid, date_created)

    print('insert query - ', query)

    cursor.execute(query)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)
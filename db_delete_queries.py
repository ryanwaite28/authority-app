from chamber import run_db_action

def delete_follow(user_id, follow_id):
  def callback(cursor):
    delete_tuple = (user_id, follow_id, )

    query = '''
    DELETE FROM authority.followings WHERE user_id = %s AND follows_id = %s
    '''

    print('insert query - ', query)

    cursor.execute(query, delete_tuple)
    new_id = cursor.fetchone()[0]
    return new_id 

  return run_db_action(callback)
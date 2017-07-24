if settings.DATABASE_USER:
  conn_params['user'] = settings.DATABASE_USER
if settings.DATABASE_PASSWORD:
  conn_params['password'] = settings_dict.DATABASE_PASSWORD
if settings_dict['DATABASE_HOST']:
  conn_params['host'] = settings_dict.DATABASE_HOST
if settings_dict.DATABASE_PORT:
  conn_params['port'] = settings_dict.DATABASE_PORT
connection = Database.connect(**conn_params)


### local, staging, test, production
Environment = "local"

### Application SecretKey
secret_key = ''

## local - True
## staging - True
## test - False
## production - False
debug = True


### Database
database = {
	'local': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'sampleapp',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': '127.0.0.1',
		'PORT': '3306',
	}
}

database['default'] = database['local']

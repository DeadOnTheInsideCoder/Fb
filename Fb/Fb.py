import requests
from random import choice



def Login(user,password):
     global Login
     global Cookies
     session = requests.session()
     session.headers.update({
        'user_agent':choice(["Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
	"Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.6.30 Version/10.61",
	"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"])	
    })
     response = session.post('https://m.facebook.com/login.php', data={
         'email': user,
         'pass': password}, allow_redirects=False)
     Cookies = response.cookies
     if 'c_user' in Cookies:
         Login = True
     else:
         Login = False

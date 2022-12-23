from bottle import route, run ,template ,request , response ,static_file
from dotenv import load_dotenv
import requests
import os 
import jwt
from os.path import join , dirname

# app code goes here
load_dotenv()

@route('/sidebar',method='POST')
def send_iframe_html():
    token = request.forms.get("token")
    if not token:
        return 'Missing token. Sorry, no can do.'
    # try:
    #     key = os.environ.get('ZENDESK_APP_PUBLIC_KEY')
    #     audience = os.environ.get('ZENDESK_APP_AUD')
    #     payload = jwt.decode(token, key, algorithms=['RS256'], audience=audience)
    # except jwt.InvalidTokenError:
    #     return '401 Invalid token. Calling the cops.'
    else:
        qs = request.query_string
        response.set_cookie('my_app_params', qs)
        return template('start', qs=qs)

@route('/list')
def show_tasks():
    access_token = os.environ.get('ASANA_ACCESS_TOKEN')
    header = {'Authorization': 'Bearer {}'.format(access_token)}
    proj_id = os.environ.get('ASANA_PROJECT_ID')
    url = 'https://app.asana.com/api/1.0/projects/{}/tasks'.format(proj_id)
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        tasks = r.json()
        return template('list_tasks', list=tasks['data'], proj_id=proj_id)
    else:
        msg = 'Problem with the request: {} {}'.format(r.status_code, r.reason)
        qs = request.get_cookie('my_app_params')
        return template('start', qs=qs, error_msg=msg)

        # return msg 


@route('/js/<filename>')
def send_js(filename):
    return static_file(filename, root='static/js')

if os.environ.get('ENVIRONMENT') == 'production':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8080)
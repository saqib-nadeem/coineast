import os
from coineast_exchange import app

def runserver():
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
	runserver()



# Set the path
'''import os, sys
import Gunicorn
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from coineast_exchange import app

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

#web: gunicorn -b 0.0.0.0:$PORT manage:app
#manager.add_command("rungunicorn", Gunicorn(host='0.0.0.0', port=5000))

if __name__ == "__main__":
    manager.run()'''

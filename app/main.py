# pylint: skip-file
from app import app
from views import views

app.run(port=8080, host='0.0.0.0', threaded=True)

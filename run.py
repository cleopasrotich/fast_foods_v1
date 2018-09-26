import os

from app import create_app


config = os.getenv('APP_SETTINGS')
app = create_app('development')

from app.api.v1.views import *


if __name__ == "__main__":
    app.run(debug=True)

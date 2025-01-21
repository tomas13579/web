from app import create_app, db
from app.models import User
from config import Config

app = create_app()


if __name__ == '__main__':
    print(f"Using Python executable: {Config.PYTHON_EXECUTABLE}")
    app.run(debug=Config.DEBUG)

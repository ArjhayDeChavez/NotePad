from flask import Flask
from routes import note_routes
from database import Base, engine

app = Flask(__name__)

# Create tables
Base.metadata.create_all(engine)

# Register routes
app.register_blueprint(note_routes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
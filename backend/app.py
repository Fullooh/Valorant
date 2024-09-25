from flask import Flask
from routes import predictions

app = Flask(__name__)

# Register Blueprints (modular route handling)
app.register_blueprint(predictions.bp)

if __name__ == '__main__':
    app.run(debug=True)
    
from services.database_service import init_db

# Initialize the database
init_db()

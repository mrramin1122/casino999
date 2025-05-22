import os
import sys
from src.main import app
from src.models import create_initial_data

if __name__ == '__main__':
    # Create database tables and initial data
    with app.app_context():
        from src.main import db
        db.create_all()
        create_initial_data()
    
    # Run the application
    app.run(host='0.0.0.0', port=5000, debug=True)
gunicorni

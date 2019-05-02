from app import app
from app.models import Title, db, User

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Title': Title, 'User': User}

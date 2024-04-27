from cto_bank import create_app
from cto_bank.models import *

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return dict(db = db, app=app, User = User, Transaction = Transaction, Service = Service)

if __name__ == '__main__':
    make_shell_context()
    app.run(debug = False, port='9090')
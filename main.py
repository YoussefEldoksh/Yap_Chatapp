from Backend import create_app
from flask_socketio import SocketIO,send


app ,socketio= create_app()

if __name__ == '__main__': #this says that only if we run this file not import it run what's inside
    # create_database(app)
    socketio.run(app,debug=True,host='0.0.0.0', port=5000)

# this is the entry point to the website  
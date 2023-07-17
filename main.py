from flask import Flask
from flask_restx import Resource,Api 

app = Flask(__name__)

api = Api()
api.init_app(app)
import threading
import time

def task():
 
    """
    background Process handled by Threads
    :return: None
    """
 
    print("Started Task ...")
    print(threading.current_thread().name)
    time.sleep(20)
    print("completed .....")

class Helloworld(Resource):
    def get(self):
        threading.Thread(target=task).start()
        # task()
        return {"message":"hello world"}
    
api.add_resource(Helloworld,'/a')

if __name__ == '__main__':
    app.run(debug=True)
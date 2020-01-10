
from dashboard import app

if __name__ =='__main__':

    app.config['ENV'] = 'development'
    app.run(port="5002")

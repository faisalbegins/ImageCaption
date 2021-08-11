from flask import Flask
import model_initializer
import caption_generator as generator

app = Flask(__name__)

# initialize all the model during app startup
model_initializer.initialize(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

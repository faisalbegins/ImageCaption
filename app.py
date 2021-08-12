from flask import Flask
import model_initializer
import caption_generator as generator

app = Flask(__name__)

# initialize all the model during app startup
model_initializer.initialize(app)


@app.route('/')
def hello_world():
    caption = generator.generate(app, '/Users/Faisal/Downloads/Flicker8k_Dataset/997722733_0cb5439472.jpg')
    print(caption)
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

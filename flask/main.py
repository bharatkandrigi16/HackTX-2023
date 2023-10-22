from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
        return render_template('index2.html')

@app.route('/process_image', methods=['POST'])
def process_image():
    from image_compare import image_compare
    if 'image' in request.files:
        image_file = request.files['image']
        measurements = image_compare(image_file)
        return render_template('index2.html', data=measurements)

if __name__ == '__main__':
    app.run(debug=True)

import os
import io
from flask import Flask, render_template, send_file, abort, request
from src.image_utils import Companions

app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html', url=request.base_url)

@app.route('/place', methods=['GET'])
@app.route('/place/<mate>',  methods=['GET'])
def place(mate=None):
	width = request.args.get('w', type=int) or request.args.get('width', type=int)
	height = request.args.get('h', type=int) or request.args.get('height', type=int)
	image, mimetype = Companions(mate).get_byte_image(width, height)
	if image == b'':
    		return abort(404)
	return send_file(io.BytesIO(image), mimetype=mimetype)
	

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
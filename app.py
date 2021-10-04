# save this as app.py
from flask import Flask
from flask import send_file
import qrcode

# Link for website
input_data = "https://towardsdatascience.com/face-detection-in-10-lines-for-beginners-1787aa1d9127"

app = Flask(__name__)


@app.route("/<string:color>")
def generateqr(color):
    # Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(input_data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color=color or 'white')
    img.save('qrcode001.png')
    return send_file('qrcode001.png', mimetype='image/gif')


@app.route('/post/<int:post_id>/<int:post_id2>', methods=['POST'])
def show_post(post_id, post_id2):
    # show the post with the given id, the id is an integer
    return f'Post = {post_id + post_id2}'

# save this as app.py
from flask import Flask
from flask import send_file
import qrcode
app = Flask(__name__)


@app.route("/<string:data>")
def generateqr(data):
    # Creating an instance of qrcode
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save('qrcode001.png')
    return send_file('qrcode001.png', mimetype='image/gif')


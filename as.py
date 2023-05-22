import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data('https://www.youtube.com/watch?v=jfKfPfyJRdk')
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')

img.save('qrcode_img.png')
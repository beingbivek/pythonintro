import qrcode

code = "mailto:beingbivek@gmail.com?subject=My First Email Using Python&body=Hello, This is my first email using Python"
img = qrcode.make(code)
type(img)  # qrcode.image.pil.PilImage
img.save("firstemailQR.png")
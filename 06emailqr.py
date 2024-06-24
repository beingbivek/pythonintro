import qrcode

code = "mailto:beingbivek@gmail.com?subject=To apply for current vacnacies&body=Greetings, I would like to join your company"
img = qrcode.make(code)
type(img)  # qrcode.image.pil.PilImage
img.save("applyemail.png")
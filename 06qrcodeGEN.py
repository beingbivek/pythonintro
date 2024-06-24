import qrcode


# Qr code for wifi

# wifi_type = "WPA"
# wifi_ssid = "hotspot"
# wifi_password = "theundertaker"
# code = "WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
# img = qrcode.make(code)
# type(img)  # qrcode.image.pil.PilImage
# img.save("wifi.png")

# QR for Google Maps

code = "https://www.google.com/maps?q=27.7032354,85.3099676"
img = qrcode.make(code)
type(img)  # qrcode.image.pil.PilImage
img.save("location.png")

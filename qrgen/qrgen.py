# Using Virtual Env that will manage libaries installation for a project easily
# using git bash terminal type
# source myenv/Scripts/activate  <= For activation
# deactivate <= For deactivation
# to create libaries used in project type
    # "pip freeze > requirements.txt"
# to install libraries of another projects follow these steps
    # Create Virtul environment = virtualenv {name}
    # Activate Virtualenv
    # pip install -r requirements.txt


import qrcode


# Qr code for wifi

wifi_type = "WPA"
wifi_ssid = "hotspot"
wifi_password = "theundertaker"
code = "WIFI:T:{wifi_type};S:{wifi_ssid};P:{wifi_password};;"
img = qrcode.make(code)
type(img)  # qrcode.image.pil.PilImage
img.save("wifi.png")
import qrcode
from PIL import Image

qrc = qrcode.QRCode(version = 1,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size=10, border=10)
qrc.add_data("https://www.linkedin.com/in/ishan-wadhwani-16a5b921b/")
qrc.make(fit = True)
img = qrc.make_image(fill_color = "white", back_color = "black")
img.save("linkedln_profile.png")
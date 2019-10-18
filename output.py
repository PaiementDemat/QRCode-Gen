import qrcode
import vars

price = "5.50"
currency = "€"

str1 = vars.merchant + "pay?price=" + price + "&currency=" + currency
img = qrcode.make(str1)
# outputImage = open("myQR.png", "a+")
# outputImage.write(img)
img.save("outputs/QRcode.png")
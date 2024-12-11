import os
import img2pdf
with open("output.pdf", "wb") as file:
   file.write(img2pdf.convert([i for i in os.listdir('/Users/admin/Desktop/python-learning/automation') if i.endswith(".jpg")]))
import pyqrcode

Name = "parth Shukla "
Mobile_No = "9599587014"
Linked_ID ="www.linkedin.com/in/parth-shukla-09205239 "
github = "https://github.com/ParthShuklaa"
Website_link ="http://shuklaparth.com/"

MyQR = pyqrcode.create(Name+Mobile_No+"\n"+Linked_ID+"\n"+github+"\n"+Website_link)
MyQR.svg("QRCode.svg")
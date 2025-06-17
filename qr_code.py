import qrcode
from PIL import Image

# Creiamo un QR code fittizio che punta a un URL simbolico del sito della villa
fake_url = "https://villaserafini-evento.it/serata-beneficenza"
qr = qrcode.make(fake_url)

# Salviamo l'immagine del QR code
qr_path = "/mnt/data/qr_villa_serafini.png"
qr.save(qr_path)

qr_path

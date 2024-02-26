import qrcode

url = ""
nomeImmagine = ""

while url == "" or nomeImmagine == "":
    url = input("Inserisci l'url da cui ricavare il qrcode: \n")
    nomeImmagine = input("Inserisci il nome con cui vuoi salvare l'immagine\n")

try:
    img = qrcode.make(url)
    img.save(nomeImmagine + ".png")
    print("Immagine salvata con successo.")
except Exception as e:
    print("Si è verificato un errore durante il salvataggio dell'immagine:", e)

import importlib.util
import subprocess
import sys


def kutuphaneyi_yukle():
  if importlib.util.find_spec("qrcode") is None:
    print("'qrcode' kütüphanesi bulunamadı, yükleniyor...")
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", "qrcode[pil]"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("'qrcode' başarıyla yüklendi.")


# Kütüphaneyi kontrol et ve yüklet
kutuphaneyi_yukle()

import qrcode


def qr_olustur():
  print("\n--- QR Kod Oluşturucu ---")
  veri = input("QR kodun içine yazılacak metin veya linki gir: ").strip()

  if not veri:
    veri = "https://github.com"
    print(f"Boş bırakıldı, varsayılan kullanılıyor: {veri}")

  dosya_adi = input(
      "Kaydedilecek dosya adı ne olsun? (Uzantısız, örn: benim_qrim): "
  ).strip()
  if not dosya_adi:
    dosya_adi = "qr_kod_cikti"

  # QR Kod oluşturma
  qr = qrcode.QRCode(
      version=1,
      error_correction=qrcode.constants.ERROR_CORRECT_H,
      box_size=10,
      border=4,
  )
  qr.add_data(veri)
  qr.make(fit=True)

  img = qr.make_image(fill_color="black", back_color="white")
  tam_dosya_adi = f"{dosya_adi}.png"
  img.save(tam_dosya_adi)

  print(f"\n[+] QR Kod başarıyla oluşturuldu ve kaydedildi: {tam_dosya_adi}")


if __name__ == "__main__":
  qr_olustur()

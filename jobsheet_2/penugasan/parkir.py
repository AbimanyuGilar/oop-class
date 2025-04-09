from datetime import datetime
import math

parkir = []
max_slot = 20

def registrasi(motor):
  if(len(parkir) < max_slot):
    parkir.append(motor)
    motor.lama_parkir = datetime.now()
    print(f'Motor dengan plat {motor.plat} telah terparkir')
  else:
    print('Tidak bisa memarkir motor, parkiran sudah penuh')

def slot():
  return(max_slot - len(parkir))

def lihat_semua():
  print('Daftar Motor Terparkir:')
  for i, j in enumerate(parkir):
    lama_parkir = math.ceil((datetime.now() - j.lama_parkir).total_seconds() / 3600) 
    tagihan = 2000 * lama_parkir
    print(f"{i+1}. {j.plat}, jam ke-{lama_parkir}, tagihan: Rp{tagihan}")

def keluar_parkir(motor):
  lama_parkir = math.ceil((datetime.now() - motor.lama_parkir).total_seconds() / 3600) 
  tagihan = 2000 * lama_parkir
  motor.lama_parkir = 0
  print(f'Motor {motor.plat} telah keluar dari tempat parkir')
  print(f'Silahkan bayar tagihan sebesar: {tagihan}')
  global parkir
  parkir = [m for m in parkir if m != motor]
import parkir # Memanggil file parkir.py untuk menggunakan fungsi-fungsinya

class Motor:
  def __init__(self, plat, merk, tipe, pemilik): # Inisialisasi atribut
    self.plat = plat
    self.merk = merk
    self.tipe = tipe
    self.pemilik = pemilik
    self.lama_parkir = 0
  
  def parkir(self): # Method untuk memarkirkan motor
    parkir.registrasi(self)

  def keluar_parkir(self): # Method untuk mengeluarkan motor dari tempat parkir
    parkir.keluar_parkir(self)

  def desc(self): # Method untuk mendeskripsikan motor
    hasil = f'''
      Plat Nomor: {self.plat}
      Merk: {self.merk}
      Tipe: {self.tipe}
      Pemilik: {self.pemilik}
    '''
    print(hasil)

  def lihat_pemilik(self): # Method untuk melihat siapa pemilik motor
    return f'Pemilik dari motor ini adalah {self.pemilik}'

  
    
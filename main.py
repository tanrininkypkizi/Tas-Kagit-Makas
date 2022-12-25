from getpass import getpass as input

print("🪨📄✂️")
print("""Oyuna başlamak için
Taş için = T 
Kağıt için = K 
Makas için = M
seçeneklerinden birini yazınız.""")
print()
Oyuncu1 =  input("Player 1:")
Oyuncu2 = input("Player 2:")
print()
if Oyuncu1 == "T" or Oyuncu1 == "t":
  if Oyuncu2 == "T" or Oyuncu2 == "t":
    print("İkiniz de taş seçtiniz. Berabere. Tekrar deneyin.")
  elif Oyuncu2 == "K" or Oyuncu2 == "k":
    print("Kağıt taşı sarar. Oyuncu2 kazandı!")
  elif Oyuncu2 == "M" or Oyuncu2 == "m":
    print("Taş makası kırar. Oyuncu1 kazandı!")
  else:
    print("Şaka yapıyorsan komik değil...")
elif Oyuncu1 == "K" or Oyuncu1 == "k":
  if Oyuncu2 == "T" or Oyuncu2 == "t":
    print("Kağıt taşı sarar. Oyuncu1 kazandı!")
  elif Oyuncu2 == "K" or Oyuncu2 == "k":
    print("İkiniz de kağıt seçtiniz. Berabere. Tekrar deneyin!")
  elif Oyuncu2 == "M" or Oyuncu2 == "m":
    print("Makas kağıdı keser. Oyuncu2 kazandı!")
  else:
    print("Seçimlerini gözden geçirsen iyi olur. Her anlamda...")
elif Oyuncu1 == "M" or Oyuncu1 == "m":
  if Oyuncu2 == "T"or Oyuncu2 == "t":
    print("Taş makası kırar. Oyuncu2 kazandı!")
  elif Oyuncu2 == "K" or Oyuncu2 == "k":
    print("Makas kağıdı keser. Oyuncu1 kazandı!")
  elif Oyuncu2 == "M" or Oyuncu2 == "m":
    print("İkiniz de makas seçtiniz. Berabere. Tekrar deneyin!")
  else:
    print("T, K ve M harflerinden birini seçmen gerektiğinin nesini anlamadın?")
else:
  print("Lütfen geçerli bir harf seç -_-")
print()
print("Teşekkür ederim Mustafa:)")



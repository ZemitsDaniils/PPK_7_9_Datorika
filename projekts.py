klase = 0
klases = [1,2,3,4,5,6,7,8,9,10,11,12]

while klase not in klases:
    klase = int(input("Ievadi klasi: "))

stundu_summa = 0

atbilde = 0

for i in range (5):
    atbilde = int(input(f"Ievadi stundu skaitu {i+1}. diena: "))
    stundu_summa = stundu_summa + atbilde

stundu_skaits_gada = 0

if (klase == 1):
    stundu_skaits_gada = stundu_summa * 34
elif (klase == 9):
    stundu_skaits_gada = stundu_summa * 37
elif (klase == 12):
    stundu_skaits_gada = stundu_summa * 38
else:
    stundu_skaits_gada = stundu_summa * 35

minutes = stundu_skaits_gada*40

print(f"Tu skola šonedēļ nosēdēji: {stundu_summa} mācību stundas, kas ir {stundu_summa*40} minūtes")
print(f"Tu skola šogad nosēdēji: {stundu_skaits_gada} mācību stundas, kas ir {minutes} minūtes")
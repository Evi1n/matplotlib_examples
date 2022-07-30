import matplotlib.pyplot as plt  # plt takma ismi ile matplotlib i içe aktardık.
plt.style.available

input_values = [1,2,3,4,5]

squares = [1, 4, 9, 16, 25]
plt.style.use('dark_background')

fig, ax = plt.subplots()  # fig değişkeni,grafiği veya şeklin tamamının koleksiyonunu temsil eder. ax tek bir grafiği temsil eder
ax.plot(input_values, squares, "r", linewidth=3) # çizgi kalınlığını düzenledik
ax.set_title("Sayıların Karesi", fontsize = 24) # çizelge için başlık belirledik ve yazı boyutu verdik
ax.set_xlabel("Değer", fontsize = 14) # eksenler için başlık seçtik
ax.set_ylabel("Değerin karesi", fontsize = 14)

ax.tick_params(axis = 'both', labelsize= 14) # çentik işaretlerine stil verdik.


plt.show()
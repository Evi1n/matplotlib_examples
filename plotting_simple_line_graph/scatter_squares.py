import matplotlib.pyplot as plt

x_values = range(1,1000)
y_values=[x**2 for x in x_values]

plt.style.use("dark_background")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c = y_values, cmap=plt.cm.Reds, s=20) # tek bir noktayı çizdirmek için kullandığımız metot. ilgili noktanın x ve y değerlerini girmeliyiz, sargümanı nokta büyüklüğü.

ax.set_title("Sayıların karesi", fontsize=24)  #grafik başlığını ve eksen isimlerini verdik
ax.set_xlabel("Değer", fontsize=14)
ax.set_ylabel("Değerin karesi", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)
ax.axis([0, 1100, 0, 1100000])

plt.show() # bu kod yerine plt.savefig('squares_plot.png', bbox_inches='tight') kullansaydık grafiği kaydetmiş olurduk. 
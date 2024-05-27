import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Συντελεστές AR(1)
alpha1, beta1 = 0.2, -0.8
alpha2, beta2 = -0.8, 0.2

# Αριθμός δειγμάτων
n_samples = 20000

# Δημιουργία θορύβου
np.random.seed(0)
noise = np.random.normal(0, 10, n_samples)  # Θόρυβος με τυπική απόκλιση 10

# Δημιουργία της χρονοσειράς AR(1) για alpha1 και beta1
X_alpha1_beta1 = np.zeros(n_samples)
for t in range(1, n_samples):
    X_alpha1_beta1[t] = alpha1 * X_alpha1_beta1[t-1] + beta1 * noise[t]

# Δημιουργία της χρονοσειράς AR(1) για alpha2 και beta2
X_alpha2_beta2 = np.zeros(n_samples)
for t in range(1, n_samples):
    X_alpha2_beta2[t] = alpha2 * X_alpha2_beta2[t-1] + beta2 * noise[t]

# Υπολογισμός της αυτοσυσχέτισης
autocorr_result_alpha1_beta1 = sm.tsa.acf(X_alpha1_beta1, nlags=10, fft=True)  # 10 σημεία
autocorr_result_alpha2_beta2 = sm.tsa.acf(X_alpha2_beta2, nlags=10, fft=True)  # 10 σημεία

# Θεωρητική διακύμανση
variance_theoretical_alpha1_beta1 = np.var(noise) / (1 - alpha1**2)
variance_theoretical_alpha2_beta2 = np.var(noise) / (1 - alpha2**2)

# Υπολογισμός της εμπειρικής διακύμανσης
variance_empirical_alpha1_beta1 = np.var(X_alpha1_beta1)
variance_empirical_alpha2_beta2 = np.var(X_alpha2_beta2)

# Υπολογισμός του μέσου όρου
mean_alpha1_beta1 = np.mean(X_alpha1_beta1)
mean_alpha2_beta2 = np.mean(X_alpha2_beta2)


print("Θεωρητική διακύμανση (α1, β1):", variance_theoretical_alpha1_beta1)
print("Εμπειρική διακύμανση (α1, β1):", variance_empirical_alpha1_beta1)
print("Μέσος όρος (α1, β1):", mean_alpha1_beta1)
print("Θεωρητική διακύμανση (α2, β2):", variance_theoretical_alpha2_beta2)
print("Εμπειρική διακύμανση (α2, β2):", variance_empirical_alpha2_beta2)
print("Μέσος όρος (α2, β2):", mean_alpha2_beta2)

# Γράφημα της αυτοσυσχέτισης για alpha1 και beta1
plt.figure(figsize=(10, 5))
plt.stem(range(len(autocorr_result_alpha1_beta1)), autocorr_result_alpha1_beta1, basefmt=" ")
plt.title("Autocorrelation για α = 0.2, β = -0.8")
plt.xlabel("Σημεία")
plt.ylabel("Συντελεστές")
plt.savefig("autocorrelation_alpha1_beta1.png")
plt.show()

# Γράφημα της αυτοσυσχέτισης για alpha2 και beta2
plt.figure(figsize=(10, 5))
plt.stem(range(len(autocorr_result_alpha2_beta2)), autocorr_result_alpha2_beta2, basefmt=" ")
plt.title("Autocorrelation για α = -0.8, β = 0.2")
plt.xlabel("Σημεία")
plt.ylabel("Συντελεστές")
plt.savefig("autocorrelation_alpha2_beta2.png")
plt.show()

# Ιστογράμματα της κατανομής των χρονοσειρών
plt.figure(figsize=(10, 5))
plt.hist(X_alpha1_beta1, bins=50, alpha=0.5, label='α = 0.2, β = -0.8')
plt.hist(X_alpha2_beta2, bins=50, alpha=0.5, label='α = -0.8, β = 0.2')
plt.title("Ιστόγραμμα Κατανομής")
plt.xlabel("Τιμές")
plt.ylabel("Συχνότητα")
plt.legend()
plt.savefig("histogram_time_series.png")
plt.show()

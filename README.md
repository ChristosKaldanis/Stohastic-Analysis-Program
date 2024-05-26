# Stohastic-Analysis-Program
# Info

# Περιγραφή Project
Το Project Stohastic-Analysis-Program αφορά την στοχαστική ανάλυση δύο Markov χρονοσειρών με θετικό και αρνητικό συντελεστή αλλά και αντιστρόφως χρησιμοποιώντας τις βιβλιόθηκες Numpy, Matplotlib και Statsmodels.api. 

# Μεθοδολογία 
Αρχικά, αφού ορίσουμε τους συντελεστές μας ορίζουμε και τον αριθμό των δειγμάτων (τιμών) που θα χρησιμοποιήσουμε. Στη συνέχεια δημιουργούμε τον θόρυβο με τυπική απόκλιση 10. Δημιουργούμε τις χρονοσειρές μας για α1 = 0,2 και β1 = -0,8 και αντίστοιχα για α2 = -0,8 και β2 = 0,2. Υπολογίζουμε την αυτοσυσχέτιση (Αutocorrelation) για 10 διαφορετικά σημεία (nlags = 10) σε διαφορετικές χρονικές περιόδους, ώστε να δούμε πόσο επηρεάζεται το κάθε ένα από το προηγούμενό του. Ύστερα, υπολογίζουμε τη θεωρητική αλλά και την εμπειρική διακύμανση για να κρίνουμε εάν οι συντελεστές που έχουμε πάρει είναι προσιτοί για ανάλυση. Για να είναι προσιτοί πρέπει το αποτέλεσμα της θεωρητικής διακύμανσης να είναι όσο πιο κοντά γίνεται στο αποτέλεσμα της εμπειρικής διακύμανσης. Τέλος, απεικονίζεται η αυτοσυσχέτιση και για τις δύο περιπτώσεις, καθώς και η κατανομή των τιμών των δύο χρονοσειρών.

# Υλοποίηση
Η υλοποίηση του συγκεκριμένου Project πραγματοποιήθηκε από τον Καλδάνη Χρήστο, προπτυχιακό φοιτητή στο τμήμα Πληροφορικής του Ιονίου Πανεπιστημίου.


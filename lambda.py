#lambda function è utile per definire funzioni brevi
somma = lambda x, y : x + y #parametri della funzione separati dalle virgole e dopo i due punti il risultato che deve ritornare

x, y = 10, 4
lista = [10, 4]
print(somma(*lista)) #sacchettamento di lista sui parametri funziona solo se gli elementi della lista soo gli stesi della funzione

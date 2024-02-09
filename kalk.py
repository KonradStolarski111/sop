def dodawanie(x, y):
  return x + y
def odejmowanie(x, y):
  return x - y
def mnozenie(x, y):
  return x * y
def dzielenie(x, y):
  if y != 0:
      return x / y
  else:
      return "za dzielenie przez 0 grozi wiezienie"
def kalkulator():
  while True:
      print("wybierz dzialanie:")
      print("1. +")
      print("2. -")
      print("3. *")
      print("4. :")
      wybor = input("podaj numer 1-4: ")
      if wybor in ('1', '2', '3', '4'):
          try:
              liczba1 = float(input("podaj 1 liczbe: "))
              liczba2 = float(input("podaj 2 liczbe: "))
          except ValueError:
              print("blad")
              continue
          if wybor == '1':
              print("wynik: ", dodawanie(liczba1, liczba2))
          elif wybor == '2':
              print("wynik: ", odejmowanie(liczba1, liczba2))
          elif wybor == '3':
              print("wynik: ", mnozenie(liczba1, liczba2))
          elif wybor == '4':
              wynik = dzielenie(liczba1, liczba2)
              print("wynik: ", wynik)
          else:
              print("blad")
      else:
          print("blad")

kalkulator()

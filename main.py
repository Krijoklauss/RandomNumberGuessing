# Imports
import random


# Diese Funktion gibt 'True' zurück wenn der/die Spieler*in die Korrekte Zahl
# erraten hat! Wenn nicht wird eine Ausgabe getätigt welche
# dem/der Spieler*in einen Hinweis gibt!

def check_win(solution: int, n: int):
    # Überprüft ob der/die Spieler*in gewonnen hat
    if solution == n:
        return True
    
    # Überprüft ob die genannte Zahl größer ist als die Lösung
    elif n > solution:
        print("Ihr Zahl ist größer als die Lösung!\n")

    # Überprüft ob die genannte Zahl kleiner ist als die Lösung
    elif n < solution:
        print("Ihre Zahl ist kleiner als die Lösung!\n")

    # Gibt Standardmäßig False wieder wenn der/die Spieler*in noch nicht gewonnen hat
    return False


# Diese Funktion überprüft die Eingabe des/der Spielers*in, darauf ob
# eine ganze zahl eingegeben wurde
# Sie überprüft nur ob das Format des Eingabestrings valide ist
def check_input(userInput: str):
    try:
        # Ich überprüfe ob alle chars im String Zahlen sind und keine Kommastelle angegeben wurde
        # Sollte dies doch der Fall sein wird eine ValueError Ausnahme geworfen welche False returned!
        if userInput.isdigit():
            return True
        else:
            raise ValueError
    except ValueError:
            print("Bitte geben Sie nur ganze ZAHLEN zwischen 0 und 100 ein!")
            print("Versuchen Sie es erneut...\n")
            return False


# Main input loop welcher den Input des users bis zur Lösung einliest
def input_loop(solution: int):
    userInput = None

    # Der loop läuft solange, bis die Korrekte Lösung eingegeben wurde
    while userInput != solution:

        # Diese Zeile liest die Eingabe des Nutzers ein
        userInput = input("Bitte geben Sie eine ganze Zahl zwischen 0 und 100 ein: ")
        
        # Hier wird mithilfe der Funktion check_input überpüft ob der Input eine Valide Zahl ist
        # und nichts anderes in der Eingabe des Nutzers ist (z.B. Buchstaben, Wörter, Kommastellen usw.)
        if check_input(userInput):
            # Diese Zeile wandelt den String in einen Integer Wert um
            num = int(userInput)

            # Nun wird geprüft wie weit die Eingabe des Nutzers von der Lösung entfernt ist
            if check_win(solution, num):
                return


# Eine kleine funktion welche eine Zufällige Zahl zwischen 0 und 100 zurückgibt
def get_random(min: int, max: int):
    return random.randint(min, max)


# Dies ist die Main Funktion welche beim Start des Programms ausgeführt wird
def __main__():
    
    # Eine zufällige Zahl wird am Anfang des Programms generiert welche die Lösung des Spiels darstellt
    solution = get_random(0, 100)
    
    # Einleitungstext welcher in der Konsole ausgegeben wird
    print("Willkommen bei meinem ZufallsZahlen-Spiel")
    print("Viel Glück beim raten!\n")

    # Diese Zeile startet den MainInputLoop welcher das Spiel bis zur Eingabe der Lösung am laufen hält
    input_loop(solution)

    # Beglückwünschung zum erraten der Korrekten Zahl!
    print("Herrzlichen Glückwunsch!")
    print("Die Korrekte Antwort war: "+str(solution))
    

# Aufruf der Main Funktion
__main__()

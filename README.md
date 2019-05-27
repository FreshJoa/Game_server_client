Instrukcja do gry: "TicTacToe"


Przed rozpoczęciem korzystania z programu:
-należy sprawdzić czy wszyscy użytkownicy są podłączeni do jednej sieci;
-należy dokonać modyfikacji plików: network.py oraz server.py, gdzie należy wpisać ręcznie adres sieciowy komputera, który będzie serwerem (można go sprawdzić przy użyciu komendy ifconfig(Linux) lub config(Windows)).

1. Jeden z użytkowników uruchamia dwa terminale,a następnie przechodzi do folderu Game_server_client-Tictactoe_modern. Drugi użytkownik włącza tylko jeden terminal, w którym również przechodzi do folderu Game_server_client-Tictactoe_modern.
2. Pierwszy gracz wpisuje komendę ./server.py (do nawiązania połączenia z drugim graczem).
3. W następnym etapie obaj użytkownicy (pierwszy użytkownik robi to w drugim terminalu) wpisuje komendę ./client.py, po czym uruchamia się każdemu plansza o wymiarach 3x3 z polami do wypełnienia.
4. Grę rozpoczyna ten użytkownik, który pierwszy kliknie w wybrane przez siebie pole. Następnie ruch wykonuje przeciwnik. 
5. Gra toczy się do momentu, aż któryś z graczy zapełni trzy pola (w pionie, poziomie lub po przekątnej) swoim symbolem, po czym wyświetla się komunikat o tym czy rozgrywkę wygrał zawodnik "O" czy "X".
6. Maksymalna ilość ruchów, które może wykonać każdy z graczy wynosi 4 i jeśli do tego momentu rozgrywka nie zostanie rozstrzygnięta na planszach wyświetli się komunikat o remisie i końcu gry.

                                    MIŁEJ GRY!!!


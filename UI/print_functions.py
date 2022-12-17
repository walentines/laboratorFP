def print_menu():
    print("Bine ati venit!")
    print()
    print_menu_movie()
    print()
    print_menu_client()
    print()
    print_menu_rent()
    print()
    print_menu_exit()

def print_menu_movie():
    print("OPERATII FILME: ")
    print("Adauga un film in baza de date: -------------------------- af [id], [titlu], [descriere], [gen], [an]")
    print()
    print("Sterge un film din baza de date (dupa id) ---------------- sfi [id]")
    print("Sterge filme din baza de date (dupa titlu) --------------- sft [titlu]")
    print("Sterge filme din baza de date (dupa descriere)------------ sfd [descriere]")
    print("Sterge filme din baza de date (dupa gen)------------------ sfg [gen]")
    print("Sterge filme din baza de date (dupa an) ------------------ sfa [an]")
    print()
    print("Modifica titlul unui film din baza de date --------------- mft [id], [titlu]")
    print("Modifica descrierea unui film din baza de date ----------- mfd [id], [descriere]")
    print("Modifica genul unui film din baza de date ---------------- mfg [id], [gen]")
    print("Modifica anul unui film din baza de date ----------------- mfa [id], [an]")
    print()
    print("Cauta filme dupa id -------------------------------------- cfi [id]")
    print("Cauta filme dupa titlu ----------------------------------- cft [titlu]")
    print("Cauta filme dupa descriere ------------------------------- cfd [descriere]")
    print("Cauta filme dupa gen ------------------------------------- cfg [gen]")
    print("Cauta filme dupa an -------------------------------------- cfa [an]")
    print()
    print("Afiseaza toate filmele disponibile ----------------------- showf")

def print_menu_client():
    print("OPERATII CLIENTI: ")
    print("Adauga un client in baza de date: ------------------------ ac [id], [nume], [cnp], [varsta]")
    print()
    print("Sterge un client din baza de date (dupa id) -------------- sci [id]")
    print("Sterge clienti din baza de date (dupa nume) -------------- scn [nume]")
    print("Sterge un client din baza de date (dupa cnp) ------------- scc [cnp]")
    print("Sterge clienti din baza de date (dupa varsta) ------------ scv [varsta]")
    print()
    print("Modifica numele unui client din baza de date ------------- mcn [id], [nume]")
    print("Modifica cnp-ul unui client din baza de date ------------- mcc [id], [cnp]")
    print("Modifica varsta unui client din baza de date ------------- mcv [id], [varsta]")
    print()
    print("Cauta clienti dupa id ------------------------------------ cci [id]")
    print("Cauta clienti dupa nume ---------------------------------- ccn [nume]")
    print("Cauta clienti dupa cnp ----------------------------------- ccc [cnp]")
    print("Cauta clienti dupa varsta -------------------------------- ccv [varsta]")
    print()
    print("Afiseaza toti clientii ----------------------------------- showc")

def print_menu_rent():
    print("OPERATII INCHIRIERE")
    print("Inchiriaza un film pentru un client ---------------------- ifc [id_client], [id_film]")
    print()
    print("Sterge inchirierea cu id-ul introdus --------------------- sl [id_link]")
    print()
    print("Afiseaza cele mai inchiriate filme ----------------------- cmif")
    print("Afiseaza clientii ordonati dupa nume --------------------- acon")
    print("Afiseaza clientii ordonati dupa num filme inchiriate ----- acof")
    print("Afiseaza primii 30% clienti cu cele mai multe filme ------ ac3of")
    print()
    print("Afiseaaza filmele inchiriate ale unui client ------------- showmvc [id_client]")

def print_menu_exit():
    print("Iesire din aplicatie ------------------------------------- exit")

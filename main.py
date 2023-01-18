import sqlite3

#conn = sqlite3.connect('mano_db.db') # sitoj db neiesko masinu
conn = sqlite3.connect('masinos.db') # bandau su kita duombaze
# butinai duombaze turi buti ten kur ir pycharm projektai, kitu atveju nesusijungs!
c = conn.cursor()

ivesti = """
INSERT INTO automobiliai VALUES(NULL,?,?,?,?,?)
"""

ieskoti = """SELECT * FROM automobiliai
WHERE marke LIKE ?
AND modelis LIKE ?
AND spalva LIKE ?
AND pagaminta BETWEEN ? AND ?
AND kaina BETWEEN ? AND ?"""

while True:
    pasirinkti = int(input("1 - automobilio įvedimas\n2 - ieškoti\n3 - atvaizduoti\n0 - išeiti\n"))
    match pasirinkti:
        case 1:
            # print("Įveskite automobilio duomenis: ")
            marke = input("Markė: ")
            modelis = input("Modelis: ")
            spalva = input("Spalva: ")
            pagaminta = int(input("Metai: "))
            kaina = int(input("Kaina: "))
            with conn:
                c.execute(ivesti, (marke, modelis, spalva, pagaminta, kaina))
        case 2:
            marke = input("Markė: ") + "%"
            modelis = input("Modelis: ") + "%"
            spalva = input("Spalva: ") + "%"
            pagaminta_nuo = input("Metai nuo: ")
            pagaminta_nuo = pagaminta_nuo if pagaminta_nuo else 1900
            pagaminta_iki = input("Metai iki: ")
            pagaminta_iki = pagaminta_iki if pagaminta_iki else 2030
            kaina_nuo = input("Kaina nuo: ")
            kaina_nuo = kaina_nuo if kaina_nuo else 1
            kaina_iki = input("Kaina iki: ")
            kaina_iki = kaina_iki if kaina_iki else 100000
            with conn:
                c.execute(ieskoti, (marke, modelis, spalva, int(pagaminta_nuo), int(pagaminta_iki),
                                    int(kaina_nuo), int(kaina_iki)))
                rezultatas = c.fetchall()  # fetchone grazina None.

            for i in rezultatas:
                print(i)
            print(f'\nIš viso rasta automobilių: {len(rezultatas)}')
            # tikrinu kiek eiluciu rodys

        case 3:
            with conn:
                c.execute("SELECT * FROM automobiliai")
                print(c.fetchall())
        case 0:
            print("Viso gero")
            break

# with conn:
# c.execute("INSERT INTO automobiliai VALUES ('1001','Audi', 'Audele', 'geltona', '1996-07-02','25000')")

# pasitikrinau ar veikia ieskant violetines spalvos visu auto.
# with conn:
#     c.execute("SELECT * From automobiliai WHERE spalva LIKE 'V%'")
#     print(c.fetchall())

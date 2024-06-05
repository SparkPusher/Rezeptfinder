# %%
import json

class Rezeptbuch:
    def __init__(self):
        self.rezepte = self.lade_rezeptbuch()
    
    def lade_rezeptbuch(self):
        with open("./JSON/rezeptbuch.json", "r", encoding="utf-8") as f:
            try:
                daten = json.load(f)
                return daten["Rezepte"]
            except (KeyError, TypeError, json.JSONDecodeError) as e:
                print(f"Fehler beim Laden der JSON-Datei: {e}")
                return []
            
    def save_rezeptbuch(self):
        with open("./JSON/rezeptbuch.json", "w", encoding="utf-8") as f:
            try:
                json.dump({"Rezepte": self.rezepte}, f, ensure_ascii=False, indent=4)
            except (KeyError, TypeError, json.JSONDecodeError) as e:
                print(f"Fehler beim Speichern der JSON-Datei: {e}")

    def add_rezept(self, rezeptname, kochbuch, seite, zutaten): 
        neues_rezept = { 
            "Rezept": rezeptname, 
            "Kochbuch": kochbuch, 
            "Seite": seite, 
            "Zutaten": zutaten 
        } 
        self.rezepte.append(neues_rezept) 
        self.save_rezeptbuch()
        print(f"Rezept '{rezeptname}' wurde hinzugefügt.")

    def show_rezeptnamen(self):
        for rezept in self.rezepte:
            print(rezept["Rezept"])

    def find_rezept(self, rezeptname):
        for rezept in self.rezepte:
            if rezept["Rezept"] == rezeptname:
                self.zutatenliste = rezept["Zutaten"]
                state_finding = True
                print(self.zutatenliste)
                break
            else:
                state_finding = False
                pass
        if state_finding == False:
            print(f"Rezept {rezeptname} nicht gefunden")

    def find_rezept_by_zutaten(self, zutaten, ausschluss_rezept=None):
        ergebnisse = []

        for rezept in self.rezepte:
            if rezept["Rezept"] == ausschluss_rezept:
                continue

            treffer = sum(zutat in rezept["Zutaten"] for zutat in zutaten)
            if treffer > 0:
                ergebnisse.append((rezept["Rezept"], treffer))

        ergebnisse.sort(key=lambda x: x[1], reverse=True)

        if ergebnisse:
            print("Rezepte nach Zutatenübereinstimmung absteigend sortiert:")
            for rezept, trefferzahl in ergebnisse:
                print(f"{rezept}: {trefferzahl} Treffer")
        else:
            print("Kein Rezept entspricht den gegebenen Zutaten.")

    def find_rezepte_basierend_auf_rezept(self, rezept_name):
        zutaten = None
        for rezept in self.rezepte:
            if rezept["Rezept"] == rezept_name:
                zutaten = rezept["Zutaten"]
                break

        if zutaten:
            print(f"Zutaten für '{rezept_name}': {', '.join(zutaten)}")
            self.find_rezept_by_zutaten(zutaten, ausschluss_rezept=rezept_name)
        else:
            print(f"Rezept '{rezept_name}' nicht gefunden.")



# %%
#############################################
#############################################
#############################################
#############################################

rezeptbuch = Rezeptbuch()
#############################################

rezeptbuch.show_rezeptnamen()
print("\n\n\n")
#############################################

rezept = rezeptbuch.find_rezept("Pancakes")
print("\n\n\n")
rezept = rezeptbuch.find_rezept("Teriyakisauce")
print("\n\n\n")
#############################################

rezeptbuch.find_rezept_by_zutaten(['Mehl', 'Eier', 'Kartoffeln'])
print("\n\n\n")
#############################################

rezeptbuch.find_rezepte_basierend_auf_rezept("Kartoffelrösti mit Lachstatar")
print("\n\n\n")

rezeptbuch.add_rezept("Toastie", "Julians Köstlichkeiten", 0, ["Toast", "Cheddar", "Tillmanns Toasty", "Siracha", "Mayo"])

rezeptbuch.show_rezeptnamen()
print("\n\n\n")

test = rezeptbuch.find_rezept("Toastie")
print(test)
print("\n\n\n")




    
# %%

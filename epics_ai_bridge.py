import time
import numpy as np

class MockPV:
    def __init__(self, name, value=12.45):
        self.name = name
        self.value = value

    def get(self):
        return self.value + float(np.random.normal(0, 0.05))

    def put(self, new_val):
        self.value = new_val
        print(f"[{self.name}] Consigne mise à jour : {self.value:.3f} A")

# 1. Connexion aux PVs virtuelles
pv_mesure_courant = MockPV("SPIRAL2:BPM01:Current", 12.45)
pv_consigne_aimant = MockPV("SPIRAL2:QUAD01:CurrentSet", 45.0)

# 2. Modèle surrogate (correction rapide)
def surrogate_model(mesure_uA):
    cible = 12.50
    erreur = cible - mesure_uA
    return 45.0 + (erreur * 2.5)

# 3. Boucle temps réel
print("=== Démarrage du pont IA <-> EPICS ===")
for cycle in range(3):
    courant_actuel = pv_mesure_courant.get()
    nouvelle_consigne = surrogate_model(courant_actuel)
    print(f"Cycle {cycle+1} | Faisceau : {courant_actuel:.3f} uA -> Consigne : {nouvelle_consigne:.3f} A")
    pv_consigne_aimant.put(nouvelle_consigne)
    time.sleep(1)

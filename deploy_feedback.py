import time

# Bornes de sécurité matérielles (Interlocks GANIL)
I_MIN = 40.0
I_MAX = 50.0

def verif_securite(consigne):
    """Bloque la commande si le modèle prédit une valeur dangereuse."""
    if I_MIN <= consigne <= I_MAX:
        return True, consigne
    print(f"[ALERTE SÉCURITÉ] Consigne {consigne:.2f} A hors limites ! Rejetée.")
    return False, 45.0  # Valeur refuge par défaut

def on_mesure_change(nouvelle_mesure):
    """Callback déclenché uniquement quand le capteur bouge."""
    print(f"[EPICS Monitor] Faisceau mesuré : {nouvelle_mesure:.2f} µA")
    
    # 1. Prédiction du modèle
    cible = 12.50
    erreur = cible - nouvelle_mesure
    consigne_ia = 45.0 + (erreur * 2.5)
    
    # 2. Vérification de sécurité avant envoi
    valide, consigne_finale = verif_securite(consigne_ia)
    
    # 3. Actionneur (caput)
    if valide:
        print(f"[EPICS caput] Aimant ajusté à : {consigne_finale:.2f} A\n")
    else:
        print(f"[EPICS caput] Consigne d'urgence appliquée : {consigne_finale:.2f} A\n")

# SIMULATION DE FLUX D'ÉVÉNEMENTS
print("=== Démarrage du contrôleur asynchrone TwinRISE ===\n")

# Cas 1 : Dérive légère normale
on_mesure_change(12.44)

# Cas 2 : Mesure stable
on_mesure_change(12.50)

# Cas 3 : Incident faisceau (dérive brutale qui ferait surchauffer l'aimant)
on_mesure_change(8.00)

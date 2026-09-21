"""Surveillance de derive statistique (Data Drift) pour les variables EPICS."""

import numpy as np
from scipy import stats

def detect_feature_drift(reference_data: np.ndarray, production_data: np.ndarray, alpha: float = 0.01) -> dict:
    """Compare deux distributions de features via le test de Kolmogorov-Smirnov.
    
    Args:
        reference_data: Distribution issue du Feature Store (donnees d'entrainement).
        production_data: Distribution observee en temps reel (Online).
        alpha: Seuil de significativite (defaut: 0.01 pour limiter les faux positifs).
        
    Returns:
        Dictionnaire avec statistique KS, p-valeur et statut d'alerte.
    """
    ks_stat, p_value = stats.ks_2samp(reference_data, production_data)
    drift_detected = p_value < alpha
    
    return {
        "statistic_ks": round(float(ks_stat), 4),
        "p_value": round(float(p_value), 6),
        "alpha": alpha,
        "drift_detected": bool(drift_detected),
        "status": "DRIFT_ALERT: Re-entrainement necessaire" if drift_detected else "STABLE: Distribution conforme"
    }

if __name__ == "__main__":
    np.random.seed(42)
    
    # 1. Distribution de reference (Feature Store / entrainement)
    ref_beam_current = np.random.normal(loc=42.0, scale=1.5, size=1000)
    
    # 2. Flux nominal reel (meme distribution physique, bruit capteur normal)
    nominal_live_data = np.random.normal(loc=42.0, scale=1.5, size=200)
    res_nominal = detect_feature_drift(ref_beam_current, nominal_live_data)
    print("--- Surveillance de flux nominal ---")
    print(f"Statistique KS : {res_nominal['statistic_ks']}, p-valeur : {res_nominal['p_value']}")
    print(f"Etat           : {res_nominal['status']}\n")
    
    # 3. Degradation physique reelle (usure source d'ions : glissement vers 44.5 mA)
    drifted_live_data = np.random.normal(loc=44.5, scale=1.8, size=200)
    res_drift = detect_feature_drift(ref_beam_current, drifted_live_data)
    print("--- Surveillance avec degradation physique (glissement faisceau) ---")
    print(f"Statistique KS : {res_drift['statistic_ks']}, p-valeur : {res_drift['p_value']}")
    print(f"Etat           : {res_drift['status']}")

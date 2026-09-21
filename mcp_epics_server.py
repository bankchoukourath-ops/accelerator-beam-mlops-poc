"""Serveur MCP exposant des outils securises pour le controle EPICS."""
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("EPICS-Beam-Control-Gateway")

I_MIN = 30.0
I_MAX = 60.0
SAFE_DEFAULT_SETPOINT = 45.0

simulated_state = {
    "beam_current": 42.5,
    "corrector_current": 45.0,
    "beam_status": "STABLE"
}

@mcp.tool()
def read_beam_diagnostics() -> dict:
    """Lit les variables de procede (PV) du faisceau en temps reel."""
    return simulated_state

@mcp.tool()
def apply_magnet_correction(target_current: float) -> dict:
    """Valide et applique une consigne de courant sur l'aimant correcteur.
    Verifie les bornes physiques avant ecriture (Software Safety Gate).
    """
    if not (I_MIN <= target_current <= I_MAX):
        simulated_state["corrector_current"] = SAFE_DEFAULT_SETPOINT
        simulated_state["beam_status"] = "DRIFT_PREVENTED"
        return {
            "status": "REJECTED",
            "reason": f"Setpoint {target_current} A hors limites [{I_MIN}, {I_MAX}]",
            "applied_fallback": SAFE_DEFAULT_SETPOINT,
            "unit": "A"
        }

    simulated_state["corrector_current"] = target_current
    simulated_state["beam_status"] = "CORRECTED"
    return {
        "status": "ACCEPTED",
        "applied_current": target_current,
        "unit": "A"
    }

if __name__ == "__main__":
    mcp.run(transport="stdio")

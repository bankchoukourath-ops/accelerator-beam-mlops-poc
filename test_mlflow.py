import mlflow

# 1. Adresse du serveur MLflow (en local ou sur le réseau du labo)
mlflow.set_tracking_uri("http://localhost:5000")

# 2. Nommer l'expérience pour le projet
mlflow.set_experiment("SPIRAL2_Beam_Surrogate")

with mlflow.start_run(run_name="hpc_run_01"):
    # Paramètres
    mlflow.log_param("model_type", "MLP_Surrogate")
    mlflow.log_param("batch_size", 64)
    mlflow.log_param("learning_rate", 0.0005)

    # Métriques simulées
    mlflow.log_metric("final_mae_uA", 0.018)
    mlflow.log_metric("inference_latency_ms", 1.45)

    # Artefact : rapport de déploiement
    with open("hpc_execution_summary.txt", "w") as f:
        f.write("Run execute sur noeud GPU HPC via Apptainer.\n")
        f.write("Validation du profil faisceau SPIRAL2 : OK.\n")
    
    mlflow.log_artifact("hpc_execution_summary.txt")

print("Run HPC termine et synchronise avec MLflow avec succes !")

#!/bin/bash
#SBATCH --job-name=ganil_ai_eval     # Nom du job affiché dans la queue
#SBATCH --output=slurm_%j.out        # Fichier de logs de sortie (%j = ID unique du job)
#SBATCH --error=slurm_%j.err         # Fichier d'erreurs
#SBATCH --partition=gpu_prod         # File / partition ciblée sur le cluster
#SBATCH --nodes=1                    # Nombre de machines physiques
#SBATCH --ntasks=1                   # Nombre de tâches
#SBATCH --cpus-per-task=4            # Nombre de cœurs CPU alloués
#SBATCH --gpus=1                     # Allocation d'un GPU
#SBATCH --mem=16G                    # Mémoire RAM réservée
#SBATCH --time=02:00:00              # Temps maximum autorisé (walltime HH:MM:SS)

# Chargement de modules d'environnement (standard en HPC)
# module load apptainer/1.3.4
# module load cuda/12.2

echo "Démarrage du job $SLURM_JOB_ID sur $(hostname) à $(date)"

# Exécution du modèle IA via le conteneur Apptainer avec support GPU (--nv)
apptainer exec --nv python_hpc.sif python3 -c "print('Pipeline IA exécuté sur le nœud de calcul avec succès')"

echo "Fin du job à $(date)"

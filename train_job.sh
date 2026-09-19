#!/bin/bash
#SBATCH --job-name=twinrise_mlflow
#SBATCH --output=slurm_%j.log
#SBATCH --error=slurm_%j.err
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --time=00:05:00

echo "=== Debut du Job SLURM $SLURM_JOB_ID ==="
echo "Execution sur le noeud : $(hostname)"

# Option A (dans un conteneur Apptainer si disponible sur le cluster) :
# apptainer exec --nv mon_image_ia.sif python3 test_mlflow.py

# Option B (execution directe dans l'environnement virtuel) :
source ~/lab-ganil/venv/bin/activate
python3 test_mlflow.py

echo "=== Fin du Job SLURM ==="

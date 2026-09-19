#!/bin/bash
#SBATCH --job-name=ganil_pipeline
#SBATCH --output=resultat_%j.log
#SBATCH --error=erreur_%j.log
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=00:10:00
#SBATCH --mem=4G

echo "=== Lancement du job Slurm sur le noeud : $(hostname) ==="
echo "Date de debut : $(date)"

# Execution du conteneur Apptainer
apptainer run pipeline.sif

echo "Date de fin : $(date)"

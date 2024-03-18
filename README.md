

# Chest_Disease_Image_Classification
- DL project: Image classification with CNN architexture

# Tools used:
- Ingest data from Google drive: `gdown` package
- Experiment tracking (hyper parameter tuning) with open source MLOPs tools: `MLFlow, Dagshub` 
- Model registration: MLFlow (MLOPs tool)
- Docker
- User app: 
- CI/CD deployment: Jenkins
- Data version control: DVC (MLOPs tool) -> for pipeline tracking

# Workflows
1. Update config.yaml # to define constants
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml


# Git commands
git add .

git commit -m "Updated"

git push origin main

# How to run?
- conda create -n chest python=3.8 -y
- conda activate chest
- pip install -r requirements.txt


### Mlflow dagshub connection uri (get this from dagshub.com repository experiment )
MLFLOW_TRACKING_URI=https://dagshub.com/malleswarigelli/Chest_Disease_Image_Classification_.mlflow \
MLFLOW_TRACKING_USERNAME=malleswarigelli \
MLFLOW_TRACKING_PASSWORD==2285aa424e395caab6840e555b7d9680a386cde7

# RUN from bash terminal

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/malleswarigelli/Chest_Disease_Image_Classification_.mlflow
export MLFLOW_TRACKING_USERNAME=malleswarigelli
export MLFLOW_TRACKING_PASSWORD=2285aa424e395caab6840e555b7d9680a386cde7

```
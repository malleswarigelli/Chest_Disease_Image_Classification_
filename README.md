
# Chest_Disease_Image_Classification
<<<<<<< HEAD
Build and deploy end to end DL: Image classification model to AWS EC2 using Docker, CI/CD Jenkins
![screenshot](flowcharts\Webapp.png)

In this project, we aimed to revolutionize healthcare by accurately classifying chest diseases from CT scan images. This would enhance early diagnosis and treatment. We utilized a DL approach: `Image Classification with CNN architexture` to achieve this.
=======
- DL project: Image classification with CNN architexture; used custom Vgg16 for model training

# Tools used:
- Ingest data from Google drive: `gdown` package
- Experiment tracking (hyper parameter tuning) with open source MLOPs tools: `MLFlow, Dagshub` 
- Model registration: MLFlow (MLOPs tool)
- Containerization: Docker, AWS ECR
- User app: Flask
- CI/CD deployment: Jenkins
- Data version control: DVC (MLOPs tool) -> for pipeline tracking
- Model deployment: AWS Ec2 
>>>>>>> e917bfedf35982cc7668bdd6f97daea20150e2cf

- Convolutional Neural Network (CNN) model was trained on a dataset of chest CT scan images, labeled as one of the following diseases: Normal, adenocarcinoma. 
- Project structure is made with a data science project template. This template ensured modularity, reusability, and maintainability of the code. It included modules for logging, exception handling, and utilities.
- Utilized DagsHub with MLflow for experiment tracking and model management, allowed us to track the experiments, compare results and manage models effectively.
- Also integrated DVC (Data Version Control) for managing the data pipeline to ensure reproducibility and collaboration among the team members.

## The project workflows were as follows:

- Data Ingestion: We ingested the CT scan images from Google drive using `gdown` package. Images were preprocessed to remove any noise and normalize the pixel values.
- Prepare Base Model: We prepared a base CNN model using a pre-trained model, VGG16, then fine-tuned this model on our dataset.
- Model Trainer: We trained the CNN model on the prepared dataset. Then, used a training-validation split to ensure the model's generalization capabilities.
- Model Evaluation: We evaluated the model's performance on a test dataset. We calculated metrics like accuracy, precision, recall, and F1-score.
- MLflow Integration: We integrated MLflow with the model trainer and evaluator components. This allowed us to track the experiments and manage the models effectively.
- DVC Pipeline: We integrated DVC with the data ingestion, model trainer, and evaluator components. This ensured reproducibility and collaboration among the team members.
- Deployed the pipeline to AWS EC2 using containers Docker, AWS ECR, CI/CD tool Jenkins
- Built user application with Flask

By the end of this project, we achieved a high level of accuracy in classifying chest diseases from CT scan images. This would significantly improve the early diagnosis and treatment of patients with chest diseases.


# Files to update workflows
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
dvc init # initializes dvc (o/p .dvc, .dvcignore files generated)
dvc repro # runs dvc.yaml file -> creates artificats -> dvc.lock
dev dag

```


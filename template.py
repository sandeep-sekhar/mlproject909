import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name='mlproject4'

list_of_files=[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_transformation.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/model_trainer.py",
    f"src/{project_name}/components/model_monitering.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/training_pipeline.py",
    f"src/{project_name}/pipeline/prediction_pipeline.py",
    f"src/{project_name}/utils.py",
    "app.py",
    "Dockerfile"
    "requirements.txt",
    "setup.py"
]



for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory:{filedir} for the file {filename}")

        if (not os.path.exists(filename)) or (os.path.getsize(filename)==0):
            with open (filepath,"w") as f:
                pass
            logging.info(f"creating empty file:{filename}")
                

        else:
            logging.info(f"{filename} is already exists")
import os 
from pathlib import Path
import logging

logging.basicconfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'Hate'

list_of_files = [
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/
]
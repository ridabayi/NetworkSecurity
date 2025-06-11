from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ == "__main__":
    try: 
        print("NetworkSecurity")

        # Créer d'abord le pipeline principal
        trainingpipelineconfig = TrainingPipelineConfig()

        # Puis créer l'objet DataIngestionConfig avec ce pipeline
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)

        # Lancer le pipeline
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiating data ingestion")

        dataingestionartificat = data_ingestion.initiate_data_ingestion()
        print("Artifacts")
        print(dataingestionartificat)

    except Exception as e:
        raise NetworkSecurityException(e, sys)

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

import mlflow

EXPERIMENT_NAME = "linear-regression-models"

mlflow.set_tracking_uri("http://mlflow:5000")
mlflow.set_experiment(EXPERIMENT_NAME)

# Enable autologging
mlflow.sklearn.autolog()

@data_exporter
def export_data(data, *args, **kwargs):
    with mlflow.start_run():
        mlflow.sklearn.log_model(data[1], artifact_path="models_mlflow")



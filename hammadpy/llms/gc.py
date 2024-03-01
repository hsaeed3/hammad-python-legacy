
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value
from hammadpy.core.interactions import TextStyles, Status
from typing import Dict, Union, Optional, List

from hammadpy.core.interactions import TextStyles, Status

class VertexAI:
    def __init__(self, project_id: str, credentials: str, location: str):
        self.text = TextStyles()
        self.status = Status()
        self.project_id = project_id
        self.location = location
        self.credentials = credentials
        self.text.say("Initializing Vertex AI...", color="blue", style="bold")
        aiplatform.init(project=self.project_id, location=self.location, credentials=self.credentials)
        self.text.say("Initialization completed.", color="green", style="bold")

    def create_dataset(self, display_name: str, gcs_source: List[str], dataset_type: str):
        """
        Creates a Vertex AI dataset.
        
        Args:
        - display_name (str): The name of the dataset.
        - gcs_source (List[str]): List of GCS paths to your data.
        - dataset_type (str): Type of dataset ('tabular', 'text', 'image', or 'video').
        """
        self.status.enter()
        if dataset_type == 'tabular':
            dataset = aiplatform.TabularDataset.create(display_name=display_name, gcs_source=gcs_source)
        elif dataset_type == 'text':
            dataset = aiplatform.TextDataset.create(display_name=display_name, gcs_source=gcs_source)
        elif dataset_type == 'image':
            dataset = aiplatform.ImageDataset.create(display_name=display_name, gcs_source=gcs_source)
        elif dataset_type == 'video':
            dataset = aiplatform.VideoDataset.create(display_name=display_name, gcs_source=gcs_source)
        else:
            self.status.exit()
            self.text.say("Invalid dataset type provided.", color="red", style="bold")
            return None
        self.status.exit()
        self.text.say(f"Dataset {display_name} created successfully.", color="green", style="bold")
        return dataset

    def train_model(self, display_name: str, dataset_id: str, training_type: str, model_type: str, target_column: Optional[str] = None):
        """
        Trains a Vertex AI model.
        
        Args:
        - display_name (str): The display name of the training job.
        - dataset_id (str): ID of the dataset to be used for training.
        - training_type (str): Type of training ('custom', 'AutoML').
        - model_type (str): Type of model ('tabular', 'image', 'text', 'video').
        - target_column (Optional[str]): The target column (for tabular datasets only).
        """
        self.status.enter()
        dataset = aiplatform.Dataset(dataset_id)
        if training_type == 'AutoML':
            if model_type == 'tabular':
                job = aiplatform.AutoMLTabularTrainingJob(display_name=display_name)
                model = job.run(dataset=dataset, target_column=target_column)
            # Add other AutoML job types here
        elif training_type == 'custom':
            # Custom training logic here
            pass
        else:
            self.status.exit()
            self.text.say("Invalid training type provided.", color="red", style="bold")
            return None
        self.status.exit()
        self.text.say(f"Model {display_name} trained successfully.", color="green", style="bold")
        return model

    def deploy_model(self, model_id: str, machine_type: str = 'n1-standard-4', min_replica_count: int = 1, max_replica_count: int = 5):
        """
        Deploys a Vertex AI model to an endpoint.
        
        Args:
        - model_id (str): The ID of the model to deploy.
        - machine_type (str): Type of machine to deploy the model to.
        - min_replica_count (int): Minimum number of replicas.
        - max_replica_count (int): Maximum number of replicas.
        """
        self.status.enter()
        model = aiplatform.Model(model_id)
        endpoint = model.deploy(machine_type=machine_type, min_replica_count=min_replica_count, max_replica_count=max_replica_count)
        self.status.exit()
        self.text.say(f"Model {model_id} deployed successfully.", color="green", style="bold")
        return endpoint

    def predict(self, endpoint_id: str, instance: Dict):
        """
        Makes a prediction query for a single instance on a deployed model endpoint using the initialized project and location.

        Args:
        - endpoint_id (str): The ID of the deployed model endpoint.
        - instance (Dict): The single input instance for prediction.
        """
        self.status.enter()
        self.text.say("Preparing to make a single prediction...", color="blue", style="bold")

        client_options = {"api_endpoint": f"{self.location}-aiplatform.googleapis.com"}
        client = aiplatform.gapic.PredictionServiceClient(client_options=client_options)

        # Prepare the instance for prediction
        instance_formatted = json_format.ParseDict(instance, Value())
        parameters_dict = {}
        parameters = json_format.ParseDict(parameters_dict, Value())

        endpoint_full_path = client.endpoint_path(project=self.project_id, location=self.location, endpoint=endpoint_id)

        self.text.say("Sending single prediction request...", color="blue", style="bold")
        # Make the prediction request
        response = client.predict(endpoint=endpoint_full_path, instances=[instance_formatted], parameters=parameters)
        
        self.text.say("Single prediction result:", color="green", style="bold")
        if response.predictions:
            prediction = dict(response.predictions[0])
            self.text.say(f"Prediction: {prediction}", color="lightwhite", style="bold")
        else:
            self.text.say("No prediction received from the model.", color="red", style="bold")

        self.status.exit()
        return response.predictions
    
if __name__ == "__main__":
    # Initialize Vertex AI
    project_id = "975757473665"
    location = "us-central1"
    credentials = "AIzaSyD44SYXA_4vB4Lrhh16nmYWYcAMQvkYeBw"
    vertex_ai = VertexAI(project_id=project_id, location=location, credentials=credentials)
    
    # Prepare input instance for prediction
    instance = {
        "feature1": 0.5,
        "feature2": 0.8,
        "feature3": 0.2
    }
    
    # Make a prediction
    endpoint_id = "3797724157454581760"
    vertex_ai.predict(endpoint_id, instance)

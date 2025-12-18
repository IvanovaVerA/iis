import mlflow
import pickle as pkl

# Работаем с MLflow локально
TRACKING_SERVER_HOST = "127.0.0.1"
TRACKING_SERVER_PORT = 5000

registry_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"
tracking_uri = f"http://{TRACKING_SERVER_HOST}:{TRACKING_SERVER_PORT}"

mlflow.set_tracking_uri(tracking_uri)   
mlflow.set_registry_uri(registry_uri)   


RUN_NAME = '8148290552ec4370b30ce5b3a589bc2f'
path = f"runs:/{RUN_NAME}/models"
loaded_model = mlflow.sklearn.load_model(path)
print(loaded_model)

with open('model.pkl', 'wb+') as f:
    pkl.dump(loaded_model, f)
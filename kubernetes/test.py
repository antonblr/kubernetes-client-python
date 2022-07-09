from kubernetes import client, config
from kubernetes.client import ApiClient

config.load_kube_config()

batch_v1 = client.BatchV1Api()
api_response = batch_v1.read_namespaced_job_status(name="descheduler-cronjob-27444656", namespace="kube-system")
print(api_response.status)
api = ApiClient()
api_response_status_dict = api.sanitize_for_serialization(api_response.status)
print(api_response_status_dict)

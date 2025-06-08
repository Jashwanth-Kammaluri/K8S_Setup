from locust import HttpUser, task, between

class MyLoadTest(HttpUser):
    wait_time = between(1, 2)  # wait time between requests per user

    @task
    def hit_echo_service(self):
        with self.client.get("/", catch_response=True) as response:
            if response.status_code == 200 and "Hello from K8s!" in response.text:
                response.success()
            else:
                response.failure(f"Unexpected response: {response.text}")

from locust import HttpUser, task

class LoadTest(HttpUser):
    @task
    def load(self):
        self.client.get("/")
#python3 -m venv test-st/
#./test-st/Scripts/activate
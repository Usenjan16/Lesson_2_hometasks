
class Config:
    def __init__(self, conf_data: dict):
        self.base_url = conf_data.get('base_url', '')
        self.service_path = f"{self.base_url}{conf_data.get('service_path', '')}"
        self.auth_path = f"{self.base_url}{conf_data.get('auth_path', '')}"
        self.username = conf_data.get("credentials", {}).get("username", '')
        self.password = conf_data.get("credentials", {}).get("password", '')
        self.credentials = {
            "username": self.username,
            "password": self.password
        }

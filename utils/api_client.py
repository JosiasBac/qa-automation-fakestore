from dotenv import load_dotenv
import os 


load_dotenv()
url = os.getenv("BASE_URL")
print(url)

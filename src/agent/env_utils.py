import os
from dotenv import load_dotenv

load_dotenv(override=True)

DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
KIMI_API_KEY = os.getenv('KIMI_API_KEY')
CHATGPT_API_KEY = os.getenv('JENIYA_API_KEY')
QWEN_API_KEY = os.getenv('JENIYA_API_KEY')

DEEPSEEK_BASE_URL = os.getenv('DEEPSEEK_BASE_URL')
KIMI_BASE_URL = os.getenv('KIMI_BASE_URL')
CHATGPT_BASE_URL = os.getenv('JENIYA_BASE_URL')
QWEN_BASE_URL = os.getenv('JENIYA_BASE_URL')

LOCAL_BASE_URL = os.getenv('LOCAL_BASE_URL')

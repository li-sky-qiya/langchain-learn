from langchain.chat_models import init_chat_model
from langchain_core.rate_limiters import InMemoryRateLimiter
from langchain_deepseek import ChatDeepSeek
from langchain_openai import ChatOpenAI

from src.agent.env_utils import DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, CHATGPT_API_KEY, CHATGPT_BASE_URL, QWEN_API_KEY, \
    QWEN_BASE_URL

# 使用OpenAI调用
llm_openai = ChatOpenAI(
    model_name="gpt-4.1-mini-2025-04-14",
    temperature=1.0,
    api_key=CHATGPT_API_KEY,
    base_url=CHATGPT_BASE_URL,
)

# 使用DeepSeek模型 （集成深度思考）
llm_deepseek = ChatDeepSeek(
    model_name="deepseek-reasoner",
    temperature=1.3,

    api_key=DEEPSEEK_API_KEY,
    api_base=DEEPSEEK_BASE_URL,
)

# 千问
llm_qwen = ChatDeepSeek(
    model_name="qwen3.5-397b-a17b",
    temperature=1.0,
    api_key=QWEN_API_KEY,
    api_base=QWEN_BASE_URL,
)

# 速率限制
rate_limiter = InMemoryRateLimiter(
    requests_per_second=0.1,
    check_every_n_seconds=0.1,
    max_bucket_size=10
)

rate_llm = init_chat_model(
    model="gpt-4.1-mini-2025-04-14",
    model_provider="openai",
    rate_limiter=rate_limiter,
    api_key=CHATGPT_API_KEY,
    base_url=CHATGPT_BASE_URL,
    temperature=1.0
)


# src/agent/__init__.py
import sys
from pathlib import Path

# 添加 src 到 Python 路径
src_path = Path(__file__).parent.parent
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))

from .my_llm import llm_openai, llm_deepseek, llm_qwen
from .my_agent1 import agent

__all__ = ['llm_openai', 'llm_deepseek', 'llm_qwen', 'agent']

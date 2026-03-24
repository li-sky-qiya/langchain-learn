from langchain_core.output_parsers import SimpleJsonOutputParser
from langchain_core.prompts import ChatPromptTemplate

from agent.my_llm import llm_qwen

prompt = ChatPromptTemplate.from_template(
    "尽你所能回答用户的问题，语言为中文。"  # 基本指令
    '你必须始终输出一个包含"title", "year", "director", "rating"键的JSON对象。'
    "{question}"  # 用户的问题占位符
)

# 链式调用：模板 -> 模型 -> 解析器（从左往右，左侧的输出作为右侧的输入）
chain = prompt | llm_qwen | SimpleJsonOutputParser()
resp = chain.invoke({"question": "请提供一下电影《霸王别姬》的详细信息"})
print(resp)

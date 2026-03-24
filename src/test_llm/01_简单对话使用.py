from agent.my_llm import rate_llm

# resp = llm_deepseek.invoke("请用三句话介绍一下，机器学习的基本概念")
# print(type(resp))
# print(resp)

# resp = llm_openai.invoke("请简单介绍一下你的模型版本，及发布日期")
# print(type(resp))
# print(resp)

# full = ""
# for chuck in llm_openai.stream("请简单介绍一下你的模型版本，及发布日期"):
#     print(chuck)
#     full = chuck if full == "" else full + chuck
#     print(full.text)

resp = rate_llm.invoke("请简单介绍一下你的模型版本，及发布日期")
print(resp)
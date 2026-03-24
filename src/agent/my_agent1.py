from langchain.agents import create_agent

from src.agent.my_llm import llm_openai


def send_email(to: str, subject: str, body: str):
    """
    发送邮件
    :param to:
    :param subject:
    :param body:
    :return:
    """
    email = {"to": to, "subject": subject, "body": body}
    # 发送邮件逻辑...

    return f"邮件已发送至：{to}"

agent = create_agent(
    model=llm_openai,
    tools=[send_email],
    system_prompt="你是一个邮件助手。请始终使用 send_email 工具。"
)
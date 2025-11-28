import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

import logging
from utils.logger import setup_logging

# 初始化日志配置
setup_logging(level=logging.INFO, log_file='logs/app.log')

logger = logging.getLogger("agent")

load_dotenv()
NEXTCHAT_API_KEY = os.getenv("NEXTCHAT_API_KEY")
NEXTCHAT_BASE_URL = os.getenv("NEXTCHAT_API_BASE")


def create_agent() -> ChatOpenAI | None:
    if not (NEXTCHAT_API_KEY and NEXTCHAT_BASE_URL):
        logger.error("Please set NEXTCHAT_API_KEY and NEXTCHAT_API_BASE in .env file")
        return None

    return ChatOpenAI(
        model = "kimi-k2-turbo-preview",
        api_key = NEXTCHAT_API_KEY,
        base_url= NEXTCHAT_BASE_URL,
        temperature=0.1,
        max_tokens=1000,
        timeout=30
    )




if __name__ == '__main__':

    logger.info("Start the first agent for Young")

    agent_mode = create_agent()
    if not agent_mode:
        logger.error("Failed to create agent")
        exit(1)

    # 创建 PromptTemplate 实例
    template = PromptTemplate(
        input_variables=["product", "feature"],
        template="为{product}写一句广告语，重点突出{feature}特点。"
    )


    # 格式化 prompt
    prompt_text = template.format(product="Young", feature="智能")
    logger.info(f"生成的 prompt: {prompt_text}")

    # 调用模型
    response = agent_mode.invoke(prompt_text)
    print(response.content)

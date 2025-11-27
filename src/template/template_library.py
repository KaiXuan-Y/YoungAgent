
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field


class TemplateLibrary(BaseModel):

    # 构建提示翻译模板
    TRANSLATOR = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are a professional translator, you can translate any language into Chinese."
        ),
        ("human", "{text}")
    ])



    CODE_GENERATOR = ChatPromptTemplate.from_messages([
        ("system",
         "你是一个经验丰富的{language}开发者。\n"
         "代码要求：\n"
         "1. 遵循{language}最佳实践\n"
         "2. 添加必要的注释\n"
         "3. 代码简洁、可读性强"),
        ("user",
         "请用{language}编写代码实现以下功能：\n\n{description}\n\n"
         "附加要求：{requirements}")
    ])




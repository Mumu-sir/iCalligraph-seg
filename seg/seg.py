from langchain_community.chat_models import ChatSparkLLM
from langchain_core.messages import HumanMessage

# 初始化ChatSparkLLM
chat = ChatSparkLLM(
    spark_app_id="",
    spark_api_key="",
    spark_api_secret="",
    spark_api_url="wss://spark-api.xf-yun.com/v4.0/chat",
    spark_llm_domain="4.0Ultra",
    model_kwargs={},  # 保持此行为空字典
)

# 用户输入文言文
text = input("请输入需要划分的文言文段落：")

# 构建请求消息
message_content = f'假设你是一个研究文言文的专家，现有一段没有段落划分也没有句读的文言文，请你给出正确的段落及标点划分，如："床前明月光疑是地上霜举头望明月低头思故乡"则回答"床前明月光，疑是地上霜。举头望明月，低头思故乡。"，请你直接给出划分后的答案，不要掺杂其他任何的语句，回答格式为：划分为：""，请严格按照回答格式回答。你需要划分的段落为："{text}"'

# 创建HumanMessage
message = HumanMessage(content=message_content)

# 调用并打印返回结果
response = chat.invoke([message])
print(response.content)

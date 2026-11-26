# pip install openai
# 用 OpenAI SDK 通过 TeamoRouter 调用 GPT、Gemini、DeepSeek 等模型（OpenAI 兼容接口）
import os

from openai import OpenAI

client = OpenAI(base_url="https://api.teamorouter.com/v1", api_key=os.environ["TEAMOROUTER_API_KEY"])

resp = client.chat.completions.create(
    model=os.environ.get("MODEL", "gpt-6.2-astra"),  # 也可以换成 gemini-4-argon、deepseek-v4-pro 等
    messages=[{"role": "user", "content": "用一句话介绍你自己"}],
)
print(resp.choices[0].message.content)

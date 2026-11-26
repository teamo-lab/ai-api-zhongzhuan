# pip install anthropic
# 用 Anthropic SDK 通过 TeamoRouter 调用 Claude（Anthropic 原生接口，Base URL 不带 /v1）
import os

from anthropic import Anthropic

client = Anthropic(base_url="https://api.teamorouter.com", api_key=os.environ["TEAMOROUTER_API_KEY"])

message = client.messages.create(
    model=os.environ.get("MODEL", "claude-opus-5-5"),
    max_tokens=1024,
    messages=[{"role": "user", "content": "用一句话介绍你自己"}],
)
print(message.content[0].text)

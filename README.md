# Claude / GPT / Gemini API 中转接入示例

TeamoRouter 官方维护的中文接入示例：用一个 API Key，通过 OpenAI 兼容接口和 Anthropic 原生接口调用 Claude、GPT、Gemini、DeepSeek、Kimi、Qwen、GLM 等模型。下面的配置可以直接复制到 Claude Code、Codex、Gemini CLI 和 Python SDK 里用。

- 官网：<https://teamorouter.com/zh>
- 模型与官方价：<https://teamorouter.com/zh/models>
- Claude API 中转：<https://teamorouter.com/zh/claude-api-zhongzhuan>
- 接入文档：<https://teamorouter.com/zh/docs/api-integration>

## 各厂商 API 中转

| 仓库 | 说明 |
|---|---|
| [teamo-lab/claude-api-zhongzhuan](https://github.com/teamo-lab/claude-api-zhongzhuan) | Claude API 中转站｜Claude、Claude Code 接入，不用 Anthropic 账号 |
| [teamo-lab/gpt-api-zhongzhuan](https://github.com/teamo-lab/gpt-api-zhongzhuan) | GPT API 中转站｜OpenAI / ChatGPT API 接入、Codex 配置，不用 OpenAI 账号 |
| [teamo-lab/gemini-api-zhongzhuan](https://github.com/teamo-lab/gemini-api-zhongzhuan) | Gemini API 中转站｜Gemini、Gemini CLI、Nano Banana 接入，不用 Google 账号 |
| [teamo-lab/deepseek-api-zhongzhuan](https://github.com/teamo-lab/deepseek-api-zhongzhuan) | DeepSeek API 中转站｜DeepSeek V4 接入、Claude Code 配置，一个 Key 调全部模型 |
| [teamo-lab/kimi-api-zhongzhuan](https://github.com/teamo-lab/kimi-api-zhongzhuan) | Kimi API 中转站｜Kimi K3 接入、Claude Code / Codex 配置 |
| [teamo-lab/qwen-api-zhongzhuan](https://github.com/teamo-lab/qwen-api-zhongzhuan) | Qwen API 中转站｜通义千问 Qwen API 接入、Cherry Studio 配置 |
| [teamo-lab/glm-api-zhongzhuan](https://github.com/teamo-lab/glm-api-zhongzhuan) | GLM API 中转站｜智谱 GLM-5 接入、Claude Code / Codex 配置 |
| [teamo-lab/grok-api-zhongzhuan](https://github.com/teamo-lab/grok-api-zhongzhuan) | Grok API 中转站｜xAI Grok API 接入、OpenAI 兼容，不用 xAI 账号 |
| [teamo-lab/minimax-api-zhongzhuan](https://github.com/teamo-lab/minimax-api-zhongzhuan) | MiniMax API 中转站｜MiniMax M3 接入、OpenAI 兼容 |
| [teamo-lab/codex-zhongzhuan](https://github.com/teamo-lab/codex-zhongzhuan) | Codex 中转站｜Codex CLI 配置 config.toml、GPT API 中转，不用 OpenAI 账号 |
| [teamo-lab/claude-code-zhongzhuan](https://github.com/teamo-lab/claude-code-zhongzhuan) | Claude Code 中转站｜Claude Code 环境变量配置、Claude API 中转，不用 Anthropic 账号 |

## 接入地址

| 接口 | Base URL | 适用 |
|---|---|---|
| OpenAI 兼容 | `https://api.teamorouter.com/v1` | Codex、Cherry Studio、Cursor、Cline、OpenCode、OpenAI SDK |
| Anthropic 原生 | `https://api.teamorouter.com`（不带 /v1） | Claude Code、Anthropic SDK |
| Gemini 原生 | `https://api.teamorouter.com` | Gemini CLI |

API Key 在 [控制台](https://teamorouter.com/dashboard?tab=api-keys) 创建，格式是 `sk-teamo-…`。新账号余额为 0，先充值再调用，$5 起，支持支付宝、微信和银行卡。

## Claude API 中转：Claude Code

```bash
export ANTHROPIC_BASE_URL=https://api.teamorouter.com
export ANTHROPIC_AUTH_TOKEN=<你的 TeamoRouter API Key>
export ANTHROPIC_API_KEY=""
claude --model claude-opus-5-5
```

完整步骤：[Claude Code 接入文档](https://teamorouter.com/zh/docs/install-claude-code)

## GPT API 中转：Codex

```toml
# ~/.codex/config.toml
model_provider = "teamorouter"
model = "gpt-6.2-astra"

[model_providers.teamorouter]
name = "TeamoRouter"
base_url = "https://api.teamorouter.com/v1"
env_key = "OPENAI_API_KEY"
wire_api = "responses"
```

完整步骤：[Codex 接入文档](https://teamorouter.com/zh/docs/install-codex)

## Gemini API 中转：Gemini CLI

```bash
mkdir -p ~/.gemini && cat > ~/.gemini/.env <<'ENV'
GOOGLE_GEMINI_BASE_URL=https://api.teamorouter.com
GEMINI_API_KEY=<你的 TeamoRouter API Key>
GEMINI_API_KEY_AUTH_MECHANISM=bearer
ENV
gemini --model gemini-4-argon
```

完整步骤：[Gemini CLI 接入文档](https://teamorouter.com/zh/docs/install-gemini-cli)

## Python SDK

- [examples/openai_chat.py](examples/openai_chat.py)：OpenAI SDK 调用 GPT / Gemini / DeepSeek
- [examples/anthropic_messages.py](examples/anthropic_messages.py)：Anthropic SDK 调用 Claude

模型 ID 以 [模型广场](https://teamorouter.com/zh/models) 为准，每个模型页都有官方价、上下文和接入示例。

## 企业对公与发票

企业账号共用一个钱包，按成员分配预算。支持对公转账充值；增值税专用发票和普通发票都可以在控制台充值记录里申请，按实际消耗金额开具，开票产生的 6% 税点由客户承担。字节跳动、腾讯及北京大学、清华大学、香港大学、哈尔滨工业大学等高校的团队在用 TeamoRouter。企业采购：<https://teamorouter.com/enterprise>

## 常见问题

**用 Claude / GPT / Gemini 中转需要厂商账号或海外信用卡吗？**
不需要。请求用 TeamoRouter 的 API Key 发到 TeamoRouter，不用注册厂商账号。

**和官方 API 有什么区别？**
接口协议和官方一致，代码只改 Base URL 和 Key；一个 Key 调用多家厂商的模型，人民币付款，可开国内增值税发票。

---

本仓库由 TeamoRouter 团队维护，示例代码以 MIT 协议开源。

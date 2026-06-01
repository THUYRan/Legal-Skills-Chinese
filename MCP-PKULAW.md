# 北大法宝 MCP · 服务与链接总表

本文件汇总接入 **[北大法宝 MCP](https://mcp.pkulaw.com)** 所需的全部官方链接、配置方式，以及其公开宣传的各项 MCP 服务。本库的检索/核验类技能（`case-retrieval`、`legal-article-retrieval`、`legal-norm-validity-check`）均通过这套接口获取真实法律数据。

> **信息可信度声明**
> 本表分两类信息：
> - ✅ **官方原文**：直接来自北大法宝官网/控制台页面，可靠。
> - ⚠️ **第三方综述**：服务的功能类别来自公开的第三方文章（如法律从业者综述），北大法宝官方亦有相应宣传，但**各服务在 MCP 协议中暴露的确切工具名（tool name）、参数 schema、`SERVICE_ID`，务必以你登录控制台后实际看到的为准**，或连接后用 `tools/list` 核实。本库不臆造工具的确切函数名。

---

## 一、核心入口链接（✅ 官方）

| 用途 | 链接 |
|---|---|
| MCP 平台首页 | https://mcp.pkulaw.com |
| **MCP 应用中心**(在此挑选服务、获取各服务 `SERVICE_ID`) | https://mcp.pkulaw.com/apis |
| **文档中心**(接入指南、工具说明) | https://mcp.pkulaw.com/docs |
| MCP 接入指南(直达) | https://mcp.pkulaw.com/docs?doc=mcp-integration |
| **控制台**(注册后管理应用与 Token) | https://mcp.pkulaw.com/console |
| 应用 / Token 管理 | https://mcp.pkulaw.com/console/apps |
| 服务定价 | https://mcp.pkulaw.com/pricing |
| CLI 工具(npm 包) | https://www.npmjs.com/package/@pkulaw/mcp-cli |
| 官方示例技能(Gitee `pkulaw-skills`) | https://gitee.com/pkulaw/pkulaw-skills |
| 北大法宝官网(数据详情) | https://www.pkulaw.com |
| ModelScope 上的官方 MCP Server | https://modelscope.cn/mcp/servers/Pkulaw/pkulaw-mcp-law-search |
| 官方客服 | 400-810-8266 |

---

## 二、统一配置方式（✅ 官方原文）

所有北大法宝 MCP 服务共用**同一套网关与鉴权**：一个 Token，MCP 与 CLI 通用。差别只在 `SERVICE_ID`（每个服务一个）。

### MCP 协议接入（对话式，经大模型）

```json
{
  "mcpServers": {
    "pkulaw-law-semantic": {
      "url": "https://apim-gw.pkulaw.com/{SERVICE_ID}/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  }
}
```

- `{SERVICE_ID}`：在[应用中心](https://mcp.pkulaw.com/apis)选定某服务后获得，**每个服务不同**。要同时用多个服务，就在 `mcpServers` 里配多个条目（各用各的 `SERVICE_ID`，可共用同一个 Token）。
- `YOUR_TOKEN`：在[控制台](https://mcp.pkulaw.com/console/apps)创建应用后获得。
- 适用客户端：Claude Code / Claude Desktop、Cursor、Dify 等任何兼容 MCP 的客户端，字段相同。
- 特点：自然语言触发，有 Token 消耗（加载 schema + LLM 推理上下文）。

### CLI 接入（脚本式，不经大模型）

```bash
npm install -g @pkulaw/mcp-cli
pkulaw-mcp init --authorization "Bearer YOUR_TOKEN"
pkulaw-mcp law-semantic search_article "劳动合同解除"
```

- 特点：固定命令直接执行、返回结构化 JSON、**零 LLM 消耗**，适合批量查询、脚本与内部系统对接。
- 上面 `law-semantic search_article` 为官网示例命令（✅ 官方原文）。其余命令组/子命令请见 `pkulaw-mcp --help` 或 [CLI 文档](https://www.npmjs.com/package/@pkulaw/mcp-cli)。

---

## 三、数据规模（✅ 官方原文）

| 数据库 | 规模 | 说明 |
|---|---|---|
| 法律法规库 | 500 万+ | 全面准确,实时更新 |
| 司法案例库 | 1.6 亿+ | 内容健全,覆盖全面 |
| 行政执法库 | 4250 万+ | 执法实务 |
| 检察文书库 | 820 万+ | 检察实务 |
| 法学期刊库 | 45 万+ | 学术前沿 |
| 专题参考库 | 30+ | 专业分类 |
| 官方称 MCP 服务总数 | **10+** | —— |

---

## 四、MCP 服务一览（⚠️ 功能类别为第三方综述，确切工具名以控制台/`tools/list` 为准）

下表是北大法宝公开宣传的 MCP 服务类别。**「对应本库技能」一列是本库的接入建议**，即每个技能在执行检索/核验步骤时，期望调用哪一类法宝服务。

| # | 服务类别 | 大致功能 | 喂给本库哪个技能 |
|---|---|---|---|
| 1 | 法律法规**语义检索** | 自然语言检索法规/法条 | `legal-article-retrieval` |
| 2 | 司法案例**语义检索** | 自然语言检索类案/判决 | `case-retrieval` |
| 3 | 法律法规**关键词检索** | 标题/正文关键词精确匹配法规(注:据第三方综述,目前较基础,约返回前 10 条) | `legal-article-retrieval` |
| 4 | 法条**关键词检索** | 关键词定位具体条文 | `legal-article-retrieval` |
| 5 | 司法案例**关键词检索** | 关键词检索案例 | `case-retrieval` |
| 6 | **法条/案号识别与溯源** | 从文本中识别法条/案号并溯源到原文与出处 | `legal-norm-validity-check`、`legal-article-retrieval` |
| 7 | **修正法条生成幻觉** | 校验/纠正模型生成的法条,识别条号错位、版本过期、虚构条文 | `legal-norm-validity-check` |
| … | 其余服务(官方称"10+") | 见[应用中心](https://mcp.pkulaw.com/apis) | 按需 |

> 第 3、第 6、第 7 项的功能描述源自公开第三方综述（[程序员如何准确高效查询法律法规？· 知乎](https://zhuanlan.zhihu.com/p/1996361054247219729)），仅供选型参考；能力的实际范围、限制与确切工具名，请以官方应用中心与文档中心为准。

---

## 五、本库三个技能的接入说明

| 技能 | 接入说明 | 主要调用的法宝服务 |
|---|---|---|
| 案例检索 `case-retrieval` | [skills/case-retrieval/README.md](./skills/case-retrieval/README.md) | 司法案例语义/关键词检索 |
| 法条检索 `legal-article-retrieval` | [skills/legal-article-retrieval/README.md](./skills/legal-article-retrieval/README.md) | 法律法规语义/关键词检索、法条识别溯源 |
| 法条效力核验 `legal-norm-validity-check` | [skills/legal-norm-validity-check/README.md](./skills/legal-norm-validity-check/README.md) | 法条识别与溯源、修正法条生成幻觉 |

---

## 六、安全与责任

- **Token 不入库**：Token 与 `SERVICE_ID` 只配置在你本地的 MCP 客户端，**绝不写进任何 SKILL.md 或提交到本仓库**。
- **不接也能跑**：未接入任何数据库时，技能仍可运行，但所有案例/法条须标注 `[待检索]` / `[待查]`，**绝不编造**。
- **可替换**：本库技能只依赖「检索/溯源」这一抽象接口，任何等价的 MCP 服务或自建检索 API 都可替换北大法宝，无需改动 `SKILL.md`。
- **最终责任**：无论数据来源，所有输出均为供执业法律专业人员审阅的草稿，最终判断与责任由执业人员承担。

---

> 接入范式参考 [fayayy888/legal-document-assistant](https://github.com/fayayy888/legal-document-assistant) 的 `anli-jiansuo` 技能。

# 接入法规数据库 · 北大法宝 MCP

`legal-article-retrieval`(法条检索)技能本身**不绑定任何特定数据库**,它定义的是检索与生成检索报告的方法论。要让它检索到**真实、现行有效、可溯源**的法律法规,需为运行环境接入一个能检索法规的 MCP 服务。

> ⚠️ 不接入数据库时,无法在线验证的法条一律标注 `[待查]`,**不得凭模型记忆编造条文编号或内容**。

目前已验证可用的是 **[北大法宝 MCP](https://mcp.pkulaw.com)**(500 万+ 法律法规库)。

## 配置

标准远程 MCP Server,以 Claude Code / Claude Desktop 为例:

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

- Token 与 `SERVICE_ID` 在 [mcp.pkulaw.com 控制台](https://mcp.pkulaw.com/console/apps) 获取,**不要提交到仓库**。
- `SERVICE_ID` 选用**法律法规语义/关键词检索**或**法条识别与溯源**服务。

## 接口契约

技能只依赖"检索"这一个抽象动作:输出检索词 → MCP 返回结构化法规(标题、文号、效力级别、生效日期、条文正文、来源链接)→ 技能据此生成检索报告。任何提供等价能力的法规库都可替换北大法宝,无需改动 `SKILL.md`。

> 完整的获取 Token、CLI、用法示例与注意事项,见 [`../case-retrieval/README.md`](../case-retrieval/README.md),配置方式完全一致,仅 `SERVICE_ID` 不同。
> 全部法宝服务与链接清单见 [`../../MCP-PKULAW.md`](../../MCP-PKULAW.md)。

---

> 致谢:接入范式参考 [fayayy888/legal-document-assistant](https://github.com/fayayy888/legal-document-assistant)。

# 接入案例数据库 · 北大法宝 MCP

`case-retrieval`(案例检索)技能本身**不绑定任何特定数据库**。它定义的是"如何提取检索要素、设计检索策略、评估相似度、生成检索报告"的方法论。要让它检索到**真实、现行、可溯源**的司法案例,你需要为运行环境接入一个能检索案例的 MCP(Model Context Protocol)服务。

> ⚠️ 不接入任何数据库时,本技能仍可运行——但所有案例都应标注为 `[待检索]`,**绝不可凭模型记忆编造案号、当事人或裁判要旨**。这与本库"宁可留白不编造"的底线一致。

目前已验证可用的方案是 **[北大法宝 MCP](https://mcp.pkulaw.com)**(1.6 亿+ 司法案例库)。下面是接入方式。

---

## 一、获取 Token

1. 访问 [mcp.pkulaw.com](https://mcp.pkulaw.com) 注册账号。
2. 进入[控制台](https://mcp.pkulaw.com/console/apps) → 创建应用 → 获取 API Token。
3. 在 [MCP 应用中心](https://mcp.pkulaw.com/apis) 找到**司法案例检索**相关服务,记下它的 `SERVICE_ID`。

> Token 与 SERVICE_ID 属于你的私密凭证,**不要写进任何 SKILL.md 或提交到仓库**。它们只配置在你本地的 MCP 客户端里。

## 二、在 MCP 客户端中配置 Server

北大法宝是标准的远程 MCP Server(URL + Bearer 鉴权)。以 Claude Code / Claude Desktop 的 `mcpServers` 配置为例:

```json
{
  "mcpServers": {
    "pkulaw-case-search": {
      "url": "https://apim-gw.pkulaw.com/{SERVICE_ID}/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN"
      }
    }
  }
}
```

把 `{SERVICE_ID}` 换成案例检索服务的实际 ID,`YOUR_TOKEN` 换成第一步拿到的 Token。其他兼容 MCP 的客户端(Cursor、Dify 等)配置字段相同,详见[官方接入文档](https://mcp.pkulaw.com/docs?doc=mcp-integration)。

> 不想经过大模型、想直接批量取数据时,北大法宝也提供 CLI:`npm i -g @pkulaw/mcp-cli`,与 MCP 共用同一个 Token。详见 [@pkulaw/mcp-cli](https://www.npmjs.com/package/@pkulaw/mcp-cli)。

## 三、技能如何调用接口(接口契约)

配置完成后,`case-retrieval` 在执行到「**四、检索方法与路径**」这一步时,会把自己设计好的检索式交给已连接的 MCP 案例检索工具,而不是凭空生成案例。技能对接口的期望非常简单——**只要环境中存在一个"输入检索词、返回真实案例列表"的工具即可**:

| 技能侧 | 接口侧(北大法宝 MCP 提供) |
|---|---|
| 输出:语义检索词 / 关键词组合(见 SKILL.md §3) | 司法案例**语义检索** / **关键词检索**工具 |
| 期望返回:案号、法院、年份、案由、裁判要旨、全文链接 | MCP 工具返回的结构化案例 JSON |
| 技能消费方式:按 §5 相似度维度评估、§6 筛选排序、§7 生成报告 | —— |

也就是说,**技能只依赖"检索"这一个抽象动作**。任何能提供等价能力的案例库(其他厂商 MCP、内部案例库、自建检索 API)都可以替换北大法宝,无需改动 `SKILL.md`。这正是"给个接口"而非"绑定供应商"的含义。

## 四、用法示例

接好之后,在 Claude Code 等环境里正常对话即可:

```
提供案件材料,说"帮我检索类似案例" → 触发 case-retrieval 技能
→ 技能提取检索要素、设计检索式
→ 技能调用 pkulaw-case-search MCP 获取真实案例
→ 技能按相似度评估、筛选排序,输出结构化《案例检索报告》
```

## 五、注意事项

- **效力与时效**:法宝返回的案例需按 SKILL.md §5.1 标注效力层级(指导性案例 / 一般案例)与时效性,避免引用已被推翻的裁判观点。
- **配套技能同理**:本库的 `legal-article-retrieval`(法条检索)、`legal-norm-validity-check`(法条效力核验)可同样接入北大法宝,配置方式一致,只是换成对应的 `SERVICE_ID`。各自的接入说明见 [`../legal-article-retrieval/README.md`](../legal-article-retrieval/README.md) 与 [`../legal-norm-validity-check/README.md`](../legal-norm-validity-check/README.md)。
- **全部服务与链接清单**:见仓库根目录 [`MCP-PKULAW.md`](../../MCP-PKULAW.md)。
- **最终责任**:无论数据来自哪个库,检索结果都只是供执业法律专业人员审阅的草稿,最终判断与责任由执业人员承担。

---

> 致谢:本接入范式参考了 [fayayy888/legal-document-assistant](https://github.com/fayayy888/legal-document-assistant) 的 `anli-jiansuo` 技能。

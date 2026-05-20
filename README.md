# Legal-Skills-Chinese · 中文法律技能库

> 面向中国大陆法域的法律推理技能集（Agent Skills）。共 38 个技能，覆盖法律检索、事实与要素处理、法律解释、法律推理、论证组织、风险评估与文书事务管理的完整链条。

---

## ⚠️ 免责声明

本技能库是辅助法律工作者进行分析的工具，**不提供法律意见、不构成法律结论、不能替代律师**。每一项技能的输出都应被视为**供执业法律专业人员审阅的草稿**，而非可直接对外使用或据以作出决定的成果。

- 技能中包含的检查清单、分析框架、风险提示，以及对法条或裁判规则的归纳，都只是辅助审阅者本人进行判断的工具，不代表本项目对法律的立场。
- 本库默认面向**中国大陆成文法体系**。在成文法体系下，案例不具有普遍约束力（最高人民法院指导性案例除外）；类比推理在刑法定罪量刑、税法课税要件等领域受严格限制甚至禁止。涉及其他法域（港澳台、普通法系等）时，使用者必须自行调整相应技能的法律前提。
- AI 生成的推理与结论可能存在偏差、遗漏或过时。**最终的法律判断必须由具备执业资格的法律专业人员作出，并由其承担相应责任。**

---

## 设计理念

这套技能库不是一堆零散的提示词，而是一个**分层的法律推理体系**：

- **原子能力（36 个）**——每个技能只做一件事：检索一条法条、提取一组要素、完成一次演绎、评估一段论证的强度。它们是可独立调用、可相互组合的最小单元。
- **复合能力（2 个）**——`judgment-document-generation`（裁判文书生成）和 `legal-judgment-prediction`（法律判决预测）是**编排层**，它们按固定主线调度多个原子能力（事实提取 → 概念理解 → 争议识别 → 法条检索 → 案例检索 → 演绎推理 → 格式适用 → 术语规范），完成端到端的复杂任务。

每个技能（`SKILL.md`）都自带：触发条件、能力边界、操作步骤、输入/输出格式，以及一段法律声明。复合能力会显式说明它调用了哪些原子能力以及调用顺序。

---

## 技能分类

38 个技能按功能分为 7 类：

| # | 类别 | 数量 | 技能 |
|---|---|:---:|---|
| 一 | **信息检索** | 5 | `case-retrieval` · `legal-article-retrieval` · `other-legal-retrieval` · `legal-norm-validity-check` · `legal-concept-comprehension` |
| 二 | **事实与要素处理** | 4 | `legal-element-extraction` · `structured-element-extraction` · `dispute-issue-identification` · `evidence-evaluation` |
| 三 | **法律解释** | 4 | `legal-interpretation-argument` · `systematic-interpretation` · `teleological-interpretation` · `normative-meaning-argumentation` |
| 四 | **法律推理** | 7 | `deductive-reasoning` · `inductive-reasoning` · `analogical-reasoning` · `legal-abductive-reasoning` · `counterfactual-reasoning` · `formal-legal-consequence` · `conflict-resolution` |
| 五 | **论证组织与评估** | 4 | `argument-chain-construction` · `argument-strength-evaluation` · `evidence-argument-chain` · `strategic-risk-prioritization` |
| 六 | **风险评估与价值判断** | 6 | `dispute-and-performance-risk` · `internal-compliance-risk-identification` · `legal-risk-assessment` · `judicial-value-judgment` · `administrative-value-judgment` · `legal-judgment-prediction`✦ |
| 七 | **文书与事务管理** | 8 | `legal-document-formatting` · `judgment-document-generation`✦ · `legal-document-summarization` · `multi-document-summarization` · `legal-terminology` · `case-lifecycle-planning` · `trial-scheduling-and-deadline-monitoring` · `billing-and-litigation-budget` |

> ✦ 标记为**复合能力**。`legal-judgment-prediction` 和 `judgment-document-generation` 在功能上分别归入「风险评估/预测」与「文书」类，但实现上是调度其他原子能力的编排层。

---

## 技能清单

| 技能目录 (slug) | 中文名 | 一句话说明 |
|---|---|---|
| `legal-element-extraction` | 法律核心要素提取 | 把日常/情绪化叙事转化为可进入法律推理的事实结构 |
| `structured-element-extraction` | 结构化要素清单 | 分析前的「质量闸门」，确保要素提取完整无遗漏 |
| `legal-concept-comprehension` | 法律概念理解 | 解释、辨析、拆解法律概念，判断事实是否构成某概念 |
| `legal-terminology` | 法律术语规范表达 | 将生活语言转化为准确、无歧义的法律术语 |
| `case-retrieval` | 案例检索 | 查找类似案例与相关判决，输出结构化检索报告 |
| `legal-article-retrieval` | 法条检索 | 生成标准化法律检索报告，含法源位阶与效力甄别 |
| `other-legal-retrieval` | 其他检索 | 检索立法背景、监管案例、地方指导意见等辅助信息 |
| `legal-norm-validity-check` | 法律规范效力检查 | 验证所引法条是否现行有效、层级正确、无冲突 |
| `dispute-issue-identification` | 争议焦点识别 | 从事实中提炼争议焦点，区分事实争议与法律争议 |
| `evidence-evaluation` | 证据效力评估 | 评估证据「三性」与证明力，识别非法证据 |
| `legal-interpretation-argument` | 运用法律解释论证 | 综合文义/体系/目的解释，对关键法条作解释论证 |
| `systematic-interpretation` | 体系解释 | 依据规范在法律体系中的位置作最符合体系的解释 |
| `teleological-interpretation` | 目的解释 | 发现并论证条文目的，在文本可承受范围内择最正当含义 |
| `normative-meaning-argumentation` | 规范意义论证 | 论证规范为何能评价特定事实及评价限度，建立涵摄链条 |
| `deductive-reasoning` | 演绎推理 | 基于形式逻辑构建可检验的三段论（P-F-C）论证链 |
| `inductive-reasoning` | 归纳推理 | 从具体案例提炼一般性裁判规则，附置信度与适用边界 |
| `analogical-reasoning` | 类比推理 | 「相似案件相似处理」，论证类比正当性（注意类推禁区） |
| `legal-abductive-reasoning` | 法律溯因推理 | 证据不完整时生成并检验最合理的解释性假设 |
| `counterfactual-reasoning` | 反事实推理 | But-for 检验，判断目标变量对法律结果的贡献 |
| `formal-legal-consequence` | 形式化推导法律后果 | 从要件满足推导赔偿数额、刑期、处罚等量化后果 |
| `conflict-resolution` | 冲突解决与优先级判定 | 处理法条竞合、证据矛盾、争点排序、法源冲突 |
| `argument-chain-construction` | 构建论证链条 | 将分散推理要素组织为完整自洽的论证结构 |
| `argument-strength-evaluation` | 评估论证强度 | 对推理结论作置信度评级，标注薄弱环节 |
| `evidence-argument-chain` | 组织证据论证链 | 建立「主张→要件→证据→证明力」的完整映射 |
| `strategic-risk-prioritization` | 战略层面风险优先级排序 | 按概率×影响对多个风险/结论排序，支撑资源配置 |
| `dispute-and-performance-risk` | 识别争议与履约风险 | 审查合同/交易，前瞻识别纠纷与违约风险 |
| `internal-compliance-risk-identification` | 内部合规风险识别 | 审查制度完整性、流程控制有效性、个人信息保护合规 |
| `legal-risk-assessment` | 识别外部监管风险 | 从许可资质、法规遵循、历史处罚等维度评估监管风险 |
| `judicial-value-judgment` | 司法价值判断 | 辅助法官在疑难案件中作可审查、可论证的价值衡量 |
| `administrative-value-judgment` | 行政价值判断 | 辅助行政人员按行政法原则作裁量与利益衡量 |
| `legal-document-formatting` | 法律文书格式适用 | 将案卷转化为格式合规的民事/刑事裁判文书 |
| `legal-document-summarization` | 法律摘要 | 对判决/裁定/调解/仲裁/行政处罚文书作结构化摘要 |
| `multi-document-summarization` | 多源文档归纳 | 跨多份文档作关联分析，识别共性与差异 |
| `case-lifecycle-planning` | 案件全周期规划 | 生成案件诉讼路线图与关键时间一览表 |
| `trial-scheduling-and-deadline-monitoring` | 庭审排期与程序时限监控 | 跟踪开庭、举证、上诉、送达等法定期限 |
| `billing-and-litigation-budget` | 工时计费与诉讼预算控制 | 管理工时与费用，编制并监控诉讼预算 |
| `judgment-document-generation`✦ | 裁判文书生成 | **复合**：调度 8 个原子能力生成完整刑事判决书 |
| `legal-judgment-prediction`✦ | 法律判决预测 | **复合**：调度 8 个原子能力预测罪名、法条、刑期 |

---

## 覆盖的评测任务

这套技能库的设计参照了中文法律 NLP 的主流评测基准。下表将常见 benchmark 任务映射到对应的技能，说明本库能覆盖哪些标准任务。

### LexEval

| 认知维度 | 代表任务 | 对应技能 |
|---|---|---|
| 记忆 Memorization | 法律概念、法条、法律演变 | `legal-concept-comprehension` · `legal-article-retrieval` · `legal-norm-validity-check` |
| 理解 Understanding | 法律关系/要素/争议焦点识别、文书摘要 | `legal-element-extraction` · `structured-element-extraction` · `dispute-issue-identification` · `legal-document-summarization` |
| 推理 Logic Inference | 法条适用/罪名/刑期预测、多跳推理、类案识别 | `deductive-reasoning` · `formal-legal-consequence` · `legal-judgment-prediction`✦ · `case-retrieval` |
| 判别 Discrimination | 文书校对、咨询回答质量评估 | `argument-strength-evaluation` · `evidence-evaluation` |
| 生成 Generation | 文书生成、论辩挖掘、阅读理解 | `legal-document-formatting` · `judgment-document-generation`✦ · `argument-chain-construction` |
| 伦理 Ethic | 法律伦理判断、偏见检测、隐私/歧视识别 | `judicial-value-judgment` · `administrative-value-judgment` |

### LawBench

| 认知层次 | 代表任务 | 对应技能 |
|---|---|---|
| 知识记忆 | 法条背诵、知识问答 | `legal-article-retrieval` · `legal-concept-comprehension` |
| 知识理解 | 文件校对、纠纷焦点识别、命名实体识别、事件检测、舆情摘要、论点挖掘 | `dispute-issue-identification` · `legal-element-extraction` · `legal-document-summarization` · `evidence-argument-chain` |
| 知识应用 | 法条/罪名/刑期预测、案例分析、犯罪金额计算、法律咨询 | `legal-judgment-prediction`✦ · `formal-legal-consequence` · `deductive-reasoning` |

### CAIL（2018–2025）

| 代表任务 | 对应技能 |
|---|---|
| 罪名预测 / 法条推荐 / 刑期预测 | `legal-judgment-prediction`✦ · `formal-legal-consequence` · `deductive-reasoning` |
| 要素识别 / 法律要素和争议焦点识别 | `legal-element-extraction` · `structured-element-extraction` · `dispute-issue-identification` |
| 类案检索 / 相似案例匹配 / 可解释类案匹配 | `case-retrieval` · `analogical-reasoning` |
| 司法摘要 / 涉法舆情摘要 | `legal-document-summarization` · `multi-document-summarization` |
| 论辩挖掘 / 论辩理解 | `argument-chain-construction` · `evidence-argument-chain` |
| 裁判文书事实生成 / 说理生成 | `judgment-document-generation`✦ · `legal-document-formatting` |
| 多人多罪判决预测 / 量刑情节识别与刑期预测 | `legal-judgment-prediction`✦ · `conflict-resolution` |
| 法律数值计算（涉案金额/赔偿/利息） | `formal-legal-consequence` · `billing-and-litigation-budget` |
| 文书校对 / 事实认定 | `argument-strength-evaluation` · `legal-element-extraction` |

### 其他基准

| 基准 | 主要任务 | 对应技能 |
|---|---|---|
| **JEC-QA**） | 司法考试知识/案例问答 | `legal-concept-comprehension` · `deductive-reasoning` |
| **LeCaRD / v2** | 法律案例检索（排序） | `case-retrieval` · `analogical-reasoning` |
| **MSLR** | 基于 IRAC 的多步法律推理 | `deductive-reasoning` · `argument-chain-construction` |
| **LAiW** | 基于三段论的 NLU/推理/生成 | `deductive-reasoning` · `formal-legal-consequence` |
| **JuDGE** | 从事实生成完整判决书 | `judgment-document-generation`✦ |
| **CLAW** | 条/款/项三级法条检索与分析 | `legal-article-retrieval` · `legal-norm-validity-check` |
| **LeKUBE** | 法律知识更新追踪 | `legal-norm-validity-check` |
| **LEVEN** | 法律事件检测、触发词识别 | `legal-element-extraction` |
| **AR-Bench** | 判决错误检测/分类/纠正 | `argument-strength-evaluation` · `evidence-evaluation` |
| **LegalAgentBench / J1-EVAL** | Agent 多步推理、工具调用、过程合规 | `legal-judgment-prediction`✦ · `conflict-resolution` · `strategic-risk-prioritization` |

> 覆盖说明：上表反映的是**方法论层面**的对应关系，即本库提供了完成该类任务所需的分析框架与步骤，并不代表已在相应数据集上做过定量评测或达到某一分数。

---

## 目录结构

```
Legal-Skills-Chinese/
├── README.md
├── <技能名>/
│   └── SKILL.md          # 每个技能一个目录，一个 SKILL.md
├── <技能名>/
│   └── SKILL.md
└── ...                   # 共 38 个技能目录
```

每个 `SKILL.md` 的开头是 YAML frontmatter：

```yaml
---
name: skill-slug          # 与目录名一致，小写连字符
description: |            # 触发条件、适用场景、能力边界
  ...
---
```

---

## 使用方式

这些技能遵循 Anthropic Agent Skills 的 `SKILL.md` 约定，可在支持该格式的环境中使用（如 Claude Cowork、Claude Code，或任何兼容 Anthropic skill 格式的工具）。

**基本流程：**

1. 将需要的技能目录放入你的 skills 目录。
2. 用自然语言描述法律任务；模型会根据 `description` 中的触发条件匹配并调用相应技能。
3. 复杂任务（如生成完整判决书、预测判决）可直接触发复合能力，由其自动调度所需的原子能力。
4. **每一份输出都应经执业法律专业人员审阅后方可使用。**

---

## 命名与规范

- 技能目录名与 `name` 字段统一为小写连字符 slug（`^[a-z0-9][a-z0-9-]+$`）。
- 中文显示名见上方[技能清单](#技能清单)。
- 每个 `SKILL.md` 均含 `name` + `description` frontmatter，并在正文给出触发条件、步骤、输入/输出格式与法律声明。

---

## 许可与责任

本项目仅供法律研究与实务辅助之用。使用者须确保其使用方式符合所在法域对法律服务、执业资格与人工智能应用的相关规定。**任何对外的法律工作成果，其专业责任由使用该成果的执业人员承担，而非本项目或本项目的贡献者。**

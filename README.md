# Legal-Skills-Chinese · 中文法律技能库

> 面向中国大陆法域的法律推理技能集（Agent Skills）。共 38 个技能，覆盖法律检索、事实与要素处理、法律解释、法律推理、论证组织、风险评估与文书事务管理的完整链条。
>
> 这些技能均由执业法律专业人员（legal professionals）逐一手写并验证，力求精确贴合中国法律的推理逻辑与实务规范，而非由模型自动生成的泛化提示词。

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

## 技能清单与能力地图

下表把 38 个技能放回它们所属的**法律工作能力维度**中，并补充每个维度背后的**理论依据（法理学/逻辑学）**与**可参考的工具、文献**。维度按法律工作的「输入 → 处理 → 输出」三层组织。

> 说明：本表只收录**已实现为 `SKILL.md` 的技能**。原始能力框架中尚有若干设想中的维度与子能力（如知识库/法条库构建、客户沟通与澄清式发问、危机预案与多场景模拟等）尚未落地，故未列入；待补齐后再行收录。

### 一、输入层 · 读懂事实与找到规范

| 能力维度 | 对应技能 (slug) | 理论依据 | 可参考工具 / 文献 |
|---|---|---|---|
| **法律解析**（理解事实、识别要素与法律关系） | `legal-element-extraction` · `structured-element-extraction` · `legal-concept-comprehension` · `dispute-issue-identification` | 认识论为事实认定提供哲学基础；言语行为理论（说话即做事——承诺、命令、宣告）帮助识别当事人话语背后的真实目的，而非只看表面 | Lex Machina（大数据驱动的法律信息分析，lexmachina.com）；论文 arxiv.org/abs/2410.21306 |
| **法律检索**（找到现行有效、层级正确的规范与案例） | `legal-article-retrieval` · `case-retrieval` · `other-legal-retrieval` · `legal-norm-validity-check` | 法律渊源理论研究法律的表现形式与效力等级（宪法/法律/行政法规孰高孰低）；规范层级理论将法律视为动态层级体系，下位法不得抵触上位法，是解决法条冲突的基础 | Westlaw Edge（westlaw.com） |

### 二、处理层 · 调查、评估、推理与判断

| 能力维度 | 对应技能 (slug) | 理论依据 | 可参考工具 / 文献 |
|---|---|---|---|
| **法律调查**（核查证据真实性、可采性与证明力） | `evidence-evaluation` | 证据可采性理论研究何种证据能被法庭接受，涵盖相关性、真实性、合法性等标准 | JusticeText（视频证据，justicetext.com）；Luminance（luminance.com）；Litera Kira（litera.com/products/kira）；实务文 revealdata.com（法律团队如何应对 AI 生成文件与深度伪造证据） |
| **法律风险评估**（识别、量化并分级法律风险） | `dispute-and-performance-risk` · `internal-compliance-risk-identification` · `legal-risk-assessment` | 规范体系论、构成要件理论、程序法理论、风险评估理论、预防原则、决策理论，以及演绎/归纳/类比逻辑推理 | LegalOn（合同审核，legalontech.com）；Darrow（法律风险预测，darrow.ai） |
| **法律推理**（演绎、归纳、类比、溯因、反事实及冲突处理） | `deductive-reasoning` · `inductive-reasoning` · `analogical-reasoning` · `legal-abductive-reasoning` · `counterfactual-reasoning` · `formal-legal-consequence` · `conflict-resolution` | 基于案例的推理（case-based，比对当前案件与先例异同）与基于规则的推理（rule-based，三段论映射）；输入-输出逻辑形式化规范的条件结构；可废止道义逻辑结合道义逻辑（义务/许可/禁止）与可废止逻辑（允许例外推翻一般规则）处理规则与例外；可能世界语义学用于评估假设情形下的法律后果 | Prolog 法律推理系统；论文 arxiv.org/html/2506.08899v1、link.springer.com/chapter/10.1007/978-3-031-35254-6_23 |
| **价值判断**（在不确定与价值冲突中作可审查的裁量） | `judicial-value-judgment` · `administrative-value-judgment` | 法哲学（自然法、实证主义、现实主义对法律本质与正当性的不同主张）；价值衡量原则（在冲突权利/原则间权衡，越重要的利益越需严格保护）；比例原则（适当性、必要性、均衡性三阶）；公共利益理论 | 参见 Google Scholar 相关研究索引 |
| **法律归纳**（对大量材料作结构化摘要与跨源综合） | `legal-document-summarization` · `multi-document-summarization` | 法律信息降维与压缩理论（在保持信息完整的前提下降低复杂度）；法律论证结构理论（主张、根据、保证、支援、限定、反驳等要素）为提取关键论点提供框架 | LexisNexis Headnotes / Lexis+（自动判决摘要、争点提取）；Westlaw KeyCite / Headnotes；论文 mdpi.com/2073-8994/17/5/633 |
| **法律流程管理**（案件全周期、排期时限与预算控制） | `case-lifecycle-planning` · `trial-scheduling-and-deadline-monitoring` · `billing-and-litigation-budget` | 运筹学与调度理论（优化排期、资源分配、任务依赖）；程序法对程序时限、证据准备、庭审组织的专业要求 | Clio（clio.com）、Streamline AI、MyCase、Litify、Wrike 等案件管理产品；CoCounsel Legal（thomsonreuters.com）；KPI 参考 streamline.ai、swiftwaterco.com |

### 三、输出层 · 论证、解释与文书

| 能力维度 | 对应技能 (slug) | 理论依据 | 可参考工具 / 文献 |
|---|---|---|---|
| **法律论证**（构建论证链、攻防对方论点、评估强度） | `argument-chain-construction` · `evidence-argument-chain` · `argument-strength-evaluation` · `legal-interpretation-argument` | Dung 抽象论辩框架（以有向图表示论证间的攻击关系，定义可接受性语义，为量化论证强度提供形式化基础）；论证图式（每种模式附带批判性问题）；Toulmin 论证模型（六要素，强调语境依赖与可废止性） | Clearbrief（clearbrief.com）；论文 arxiv.org/html/2412.11617v1 |
| **法律解释**（文义、体系、目的解释及通俗化表达） | `systematic-interpretation` · `teleological-interpretation` · `normative-meaning-argumentation` | 法律解释学（理解是解释者与文本的视域融合，强调历史性、语言性、实践性）；法教义学以现行有效法律为对象，通过概念分析与体系建构发展法律；文义/体系/目的解释构成有优先级的方法层级 | 参考研究 Jurex-4E |
| **法律策略**（战略层面的风险优先级与资源取舍） | `strategic-risk-prioritization` | 多属性效用决策理论（将偏好表示为多属性效用函数，处理冲突目标间权衡）；战略运筹学；决策理论（期望效用、前景理论） | Lex Machina（lexmachina.com）；CoCounsel 策略分析；实务文 opus2.com/ai-for-legal-case-strategy |
| **法律文书写作**（格式适用与术语规范） | `legal-document-formatting` · `legal-terminology` | 言语行为理论确保文书的言外行为效力准确（合同条款产生约束力、诉状启动诉讼）；AGM 信念修正理论形式化知识库的扩张/收缩/修正三种操作；规范变更逻辑研究规范的创设、修改、废止与溯及力 | Spellbook、Briefpoint、Clio Draft、Legalyze.ai、Luminance；论文《Normative Change: An AGM Approach》 |

### 复合能力（编排层）

| 技能 (slug) | 中文名 | 说明 |
|---|---|---|
| `legal-judgment-prediction`✦ | 法律判决预测 | 调度 8 个原子能力（要素提取 → 概念理解 → 争议识别 → 法条检索 → 案例检索 → 演绎推理 → 格式适用 → 术语规范），预测罪名、适用法条、刑期与量刑情节；理论上对应 LJP 与多跳推理（multi-hop reasoning） |
| `judgment-document-generation`✦ | 裁判文书生成 | 调度同一组原子能力，生成完整刑事判决书 |

> ✦ 标记为**复合能力**：它们本身不引入新的原子能力，而是按固定主线调度上表中的原子技能完成端到端任务。
>
> 综合性参考产品（覆盖多维能力）：Harvey AI（harvey.ai）、Lexis+ AI、CoCounsel（cocounsel.com）、Clio（clio.com）。

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

## 许可与责任

本项目仅供法律研究与实务辅助之用。使用者须确保其使用方式符合所在法域对法律服务、执业资格与人工智能应用的相关规定。**任何对外的法律工作成果，其专业责任由使用该成果的执业人员承担，而非本项目或本项目的贡献者。**

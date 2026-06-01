<div align="center">

<img src="./assets/banner.svg" alt="Legal-Skills-Chinese · Chinese Legal Reasoning Skills Library" width="100%">

</div>

<br>

<div align="center">

[![Awesome](https://awesome.re/badge-flat.svg)](https://awesome.re)
[![Skills](https://img.shields.io/badge/Skills-38-3a5a8c.svg?style=flat-square)](#-skill-index)
[![Atomic + Compound](https://img.shields.io/badge/Atomic%20×36-+%20Compound%20×2-5b606b.svg?style=flat-square)](#-design-philosophy)
[![Jurisdiction](https://img.shields.io/badge/Jurisdiction-PRC%20Statutory%20Law-b5462f.svg?style=flat-square)](#-disclaimer)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-3f7d6e.svg?style=flat-square)](#-submit-a-new-skill)
[![License](https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-9aa0ab.svg?style=flat-square)](#-license)

**38 hand-crafted legal reasoning skills (Agent Skills) authored and validated by practicing lawyers, covering the full chain from retrieval → reasoning → argumentation → drafting.**

*A curated library of 38 hand-crafted, lawyer-verified legal reasoning skills for PRC statutory law.*

[Skill Index](#-skill-index) ·
[Design Philosophy](#-design-philosophy) ·
[Installation](#-installation) ·
[Benchmark Coverage](#-benchmark-coverage) ·
[Usage](#-usage) ·
[Submit a New Skill](#-submit-a-new-skill)

</div>

<img src="./assets/rule.svg" alt="" width="100%">

> [!WARNING]
> ### ⚠️ Disclaimer
>
> This skills library is an auxiliary tool for legal professionals. It does **not** provide legal advice, does **not** constitute legal conclusions, and **cannot** replace a lawyer. Each skill's output should be regarded as a draft for review by a qualified legal professional, not as a final product to be used externally or relied upon for decisions.
>
> - Checklists, analytical frameworks, risk prompts, and summaries of statutes or jurisprudential rules in the skills are aids for reviewers and do not represent the project's stance on the law.
> - This repository is intended for the **PRC statutory law** context. In civil law systems, cases do not have universal binding effect (except for guiding cases by the Supreme People's Court); analogical reasoning is strictly limited or prohibited in areas like criminal law elements and tax law. When applying skills to other jurisdictions (Hong Kong, Macau, Taiwan, common law systems, etc.), users must adjust the legal assumptions accordingly.
> - AI-generated reasoning and conclusions may contain biases, omissions, or be outdated. **Final legal determinations must be made by qualified legal professionals who bear the corresponding responsibility.**

<img src="./assets/rule.svg" alt="" width="100%">

## 🧭 Design Philosophy

This skills library is not a collection of disconnected prompts but a **layered legal reasoning system**.

<table>
<tr>
<td width="50%" valign="top">

#### 🧩 Atomic Abilities × 36

Each skill does one thing: retrieve a statute, extract a set of elements, perform a deduction, or evaluate an argument's strength.

They are the smallest callable, composable units.

</td>
<td width="50%" valign="top">

#### 🎼 Compound Abilities × 2 ✦

`judgment-document-generation` and `legal-judgment-prediction` are orchestration layers.

They do not introduce new abilities but schedule multiple atomic abilities in fixed flows to complete end-to-end complex tasks.

</td>
</tr>
</table>

The orchestration flow for compound abilities:

```
Fact element extraction → Concept comprehension → Issue identification → Statute retrieval → Case retrieval → Deductive reasoning → Rule application → Terminology normalization
```

Each `SKILL.md` includes: **trigger conditions · capability boundaries · operational steps · input/output format · legal disclaimer**. Compound abilities explicitly state which atomic abilities they call and in what order.

> 💡 **Why emphasize "hand‑written"?** These skills are individually authored and validated by practicing legal professionals to match Chinese legal reasoning and practice standards, rather than being generic, model-generated prompts.

<img src="./assets/rule.svg" alt="" width="100%">

## 📦 Installation

### One‑click install (recommended)

```bash
npx skills add THUYRan/Legal-Skills-Chinese --all
```

Installs all 38 skills at once. You can also run the following to pick skills from an interactive checklist:

```bash
npx skills add THUYRan/Legal-Skills-Chinese
```

Or install specific skills by name:

```bash
npx skills add THUYRan/Legal-Skills-Chinese --skill deductive-reasoning --skill case-retrieval
```

### Manual install

```bash
git clone https://github.com/THUYRan/Legal-Skills-Chinese.git
cp -r skills/<skill-dir> /path/to/your/.claude/skills/
```

See [Usage](#-usage) below for how to invoke the skills after installation.

<img src="./assets/rule.svg" alt="" width="100%">

## 📚 Skill Index

38 skills are grouped into **7 categories**, corresponding to the three layers of legal work: Input → Process → Output.

| Category | <span style="white-space:nowrap">Count</span> | Skills |
|:---|:---:|:---|
| <span style="white-space:nowrap">**01 · Retrieval**</span> | 5 | `case-retrieval` · `legal-article-retrieval` · `other-legal-retrieval` · `legal-norm-validity-check` · `legal-concept-comprehension` |
| <span style="white-space:nowrap">**02 · Facts & Element Processing**</span> | 4 | `legal-element-extraction` · `structured-element-extraction` · `dispute-issue-identification` · `evidence-evaluation` |
| <span style="white-space:nowrap">**03 · Legal Interpretation**</span> | 4 | `legal-interpretation-argument` · `systematic-interpretation` · `teleological-interpretation` · `normative-meaning-argumentation` |
| <span style="white-space:nowrap">**04 · Legal Reasoning**</span> | 7 | `deductive-reasoning` · `inductive-reasoning` · `analogical-reasoning` · `legal-abductive-reasoning` · `counterfactual-reasoning` · `formal-legal-consequence` · `conflict-resolution` |
| <span style="white-space:nowrap">**05 · Argument Organization & Evaluation**</span> | 4 | `argument-chain-construction` · `argument-strength-evaluation` · `evidence-argument-chain` · `strategic-risk-prioritization` |
| <span style="white-space:nowrap">**06 · Risk Assessment & Value Judgment**</span> | 6 | `dispute-and-performance-risk` · `internal-compliance-risk-identification` · `legal-risk-assessment` · `judicial-value-judgment` · `administrative-value-judgment` · `legal-judgment-prediction` ✦ |
| <span style="white-space:nowrap">**07 · Documents & Case Management**</span> | 8 | `legal-document-formatting` · `judgment-document-generation` ✦ · `legal-document-summarization` · `multi-document-summarization` · `legal-terminology` · `case-lifecycle-planning` · `trial-scheduling-and-deadline-monitoring` · `billing-and-litigation-budget` |

> ✦ Marked as **compound**: `legal-judgment-prediction` and `judgment-document-generation` are categorized under risk/prediction and documents respectively, but they are orchestration layers that call atomic abilities.

<br>

<img src="./assets/layer-1-input.svg" alt="INPUT · Input Layer" width="100%">

<img src="./assets/cat-1-retrieval.svg" alt="Retrieval" height="38">

> **Theoretical basis**: legal sources theory (forms and hierarchy of law) · normative hierarchy theory (lower law must not conflict with higher law) · speech act theory (identify underlying purpose of discourse) — **References** [Westlaw Edge](https://westlaw.com) · [Lex Machina](https://lexmachina.com)

[<img src="./assets/tag-case-retrieval.svg" alt="case-retrieval" height="30">](./skills/case-retrieval)

Find cases, relevant rulings, and adjudicative rules related to the legal issue to support arguments, predict outcomes, and compare judicial positions.

[<img src="./assets/tag-legal-article-retrieval.svg" alt="legal-article-retrieval" height="30">](./skills/legal-article-retrieval)

Generate standardized statute retrieval reports, verify the validity of legal bases, confirm claims/defenses' statutory support, and analyze judicial practice tendencies.

[<img src="./assets/tag-other-legal-retrieval.svg" alt="other-legal-retrieval" height="30">](./skills/other-legal-retrieval)

Retrieve auxiliary information beyond statutes/judicial interpretations/typical cases: legislative background, regulatory cases, local guidance, industry standards, academic views, and foreign comparisons.

[<img src="./assets/tag-legal-norm-validity-check.svg" alt="legal-norm-validity-check" height="30">](./skills/legal-norm-validity-check)

Validate the legal effect of retrieved statutes: current validity, hierarchical correctness, and absence of conflicts with higher or peer norms to ensure reliable reasoning.

[<img src="./assets/tag-legal-concept-comprehension.svg" alt="legal-concept-comprehension" height="30">](./skills/legal-concept-comprehension)

Explain, distinguish, and decompose legal concepts, analyze constitutive elements and legal effects—this is the foundational unit of legal analysis.

<br>

<img src="./assets/cat-2-facts.svg" alt="Facts & Element Processing" height="38">

> **Theoretical basis**: epistemology (philosophy of fact-finding) · elements-of-offense theory · evidence admissibility (relevance, authenticity, legality)

[<img src="./assets/tag-legal-element-extraction.svg" alt="legal-element-extraction" height="30">](./skills/legal-element-extraction)

Extract legally relevant facts from unstructured text (case descriptions, chat logs, reports) and translate lay descriptions into legal language.

[<img src="./assets/tag-structured-element-extraction.svg" alt="structured-element-extraction" height="30">](./skills/structured-element-extraction)

Decompose legal issues/facts/statutes into structured element checklists as a quality gate before downstream reasoning to ensure completeness and traceability.

[<img src="./assets/tag-dispute-issue-identification.svg" alt="dispute-issue-identification" height="30">](./skills/dispute-issue-identification)

After element extraction, identify the points of dispute, exclude undisputed matters, and convert case relationships into legal-issue questions.

[<img src="./assets/tag-evidence-evaluation.svg" alt="evidence-evaluation" height="30">](./skills/evidence-evaluation)

Assess evidence for relevance, authenticity, and legality (the "three qualities") and evaluate probative value, admissibility, standards of proof, reinforcement suggestions, and exclusion of illegal evidence.

<img src="./assets/rule.svg" alt="" width="100%">

<img src="./assets/layer-2-process.svg" alt="PROCESS · Process Layer" width="100%">

<img src="./assets/cat-3-interpret.svg" alt="Legal Interpretation" height="38">

> **Theoretical basis**: hermeneutics of law · doctrinal legal studies · prioritized methods of textual/systematic/purposive interpretation

[<img src="./assets/tag-legal-interpretation-argument.svg" alt="legal-interpretation-argument" height="30">](./skills/legal-interpretation-argument)

Use textual, systematic, and purposive interpretation to rigorously argue ambiguous or contested statutory provisions.

[<img src="./assets/tag-systematic-interpretation.svg" alt="systematic-interpretation" height="30">](./skills/systematic-interpretation)

Systematic interpretation: interpret provisions in light of their position and related norms within the legal system to achieve coherent system‑level meaning.

[<img src="./assets/tag-teleological-interpretation.svg" alt="teleological-interpretation" height="30">](./skills/teleological-interpretation)

Purposive interpretation: when textual meaning is indeterminate, discover and justify the statutory purpose and choose the most legitimate meaning within the text's tolerable range.

[<img src="./assets/tag-normative-meaning-argumentation.svg" alt="normative-meaning-argumentation" height="30">](./skills/Normative-Meaning-Argumentation)

Analyze a norm's purposes and value orientation, determining how facts enter normative evaluation and the limits of normative subsumption.

<br>

<img src="./assets/cat-4-reasoning.svg" alt="Legal Reasoning" height="38">

> **Theoretical basis**: rule-based (syllogism mapping) and case-based reasoning · input-output logic · defeasible deontic logic (duty/permission/prohibition + exceptions) · possible-world semantics

[<img src="./assets/tag-deductive-reasoning.svg" alt="deductive-reasoning" height="30">](./skills/deductive-reasoning)

Strict deductive reasoning based on formal logic, turning unstructured norms and facts into testable syllogistic chains (P-F-C).

[<img src="./assets/tag-inductive-reasoning.svg" alt="inductive-reasoning" height="30">](./skills/inductive-reasoning)

Generalize rules, decisional patterns, or principles from one or multiple concrete cases or factual patterns.

[<img src="./assets/tag-analogical-reasoning.svg" alt="analogical-reasoning" height="30">](./skills/analogical-reasoning)

Where statutory gaps exist, identify the basis of similarity (tertium comparationis), justify analogical reasoning, and draw conclusions.

[<img src="./assets/tag-legal-abductive-reasoning.svg" alt="legal-abductive-reasoning" height="30">](./skills/Legal-Abductive-Reasoning)

Generate and evaluate the most reasonable explanatory hypotheses when evidence is incomplete or facts are unclear; combine with Mill's methods for structured causal inference.

[<img src="./assets/tag-counterfactual-reasoning.svg" alt="counterfactual-reasoning" height="30">](./skills/counterfactual-reasoning)

Assess how the legal result would differ if a fact/action had not occurred, used for causal attribution, apportioning liability, and damage scope.

[<img src="./assets/tag-formal-legal-consequence.svg" alt="formal-legal-consequence" height="30">](./skills/formal-legal-consequence)

Terminal point of the reasoning chain: derive specific legal consequences (liability, compensation, sentence, sanction, contract effect) from established facts and matched norms.

[<img src="./assets/tag-conflict-resolution.svg" alt="conflict-resolution" height="30">](./skills/conflict-resolution)

Handle statute collisions, evidentiary contradictions, issue prioritization, and source conflicts— the central hub touched by most complex legal analyses.

<br>

<img src="./assets/cat-6-risk.svg" alt="Risk Assessment & Value Judgment" height="38">

> **Theoretical basis**: risk assessment theory · precautionary principle · decision theory · philosophy of law (natural law/positivism/realism) · proportionality (suitability, necessity, balance) · public interest theory

[<img src="./assets/tag-dispute-and-performance-risk.svg" alt="dispute-and-performance-risk" height="30">](./skills/dispute-and-performance-risk)

Assess whether a contract/transaction will produce disputes or breach risk, output structured risk checklists and mitigation suggestions.

[<img src="./assets/tag-internal-compliance-risk-identification.svg" alt="internal-compliance-risk-identification" height="30">](./skills/internal-compliance-risk-identification)

Systematically review corporate compliance frameworks, covering institutional completeness, process control effectiveness, and personal data protection.

[<img src="./assets/tag-legal-risk-assessment.svg" alt="legal-risk-assessment" height="30">](./skills/legal-risk-assessment)

Assess regulatory penalty risks from licensing, regulatory compliance, and historical penalties dimensions.

[<img src="./assets/tag-judicial-value-judgment.svg" alt="judicial-value-judgment" height="30">](./skills/judicial-value-judgment)

Assist judges in making reviewable, arguable value judgments in rights conflicts, legal uncertainty, and proportionality review.

[<img src="./assets/tag-administrative-value-judgment.svg" alt="administrative-value-judgment" height="30">](./skills/administrative-value-judgment)

Assist administrative officers to make value judgments and interest balancing under administrative law principles, forming directional discretionary conclusions.

[<img src="./assets/tag-legal-judgment-prediction.svg" alt="legal-judgment-prediction" height="30">](./skills/legal-judgment-prediction)

**Compound ability ✦**: orchestrates 8 atomic abilities to predict charges, applicable statutes, sentence ranges, and sentencing factors, outputting a structured report with confidence scores.

<img src="./assets/rule.svg" alt="" width="100%">

<img src="./assets/layer-3-output.svg" alt="OUTPUT · Output Layer" width="100%">

<img src="./assets/cat-5-argument.svg" alt="Argument Organization & Evaluation" height="38">

> **Theoretical basis**: Dung's abstract argumentation frameworks (quantify argument strength via directed attack relations) · argumentation schemata (with critical questions) · Toulmin model (six elements, defeasibility) · multi-attribute utility decision theory

[<img src="./assets/tag-argument-chain-construction.svg" alt="argument-chain-construction" height="30">](./skills/argument-chain-construction)

Organize reasoning results into coherent, persuasive argument structures for opinions, counsel submissions, or defenses.

[<img src="./assets/tag-argument-strength-evaluation.svg" alt="argument-strength-evaluation" height="30">](./skills/argument-strength-evaluation)

Self-evaluate completed reasoning, provide strength/confidence ratings, and identify weak links in the chain.

[<img src="./assets/tag-evidence-argument-chain.svg" alt="evidence-argument-chain" height="30">](./skills/evidence-argument-chain)

Map claim→elements→evidence→probative-value to ensure each claim has adequate evidence and every piece of evidence has a clear purpose.

[<img src="./assets/tag-strategic-risk-prioritization.svg" alt="strategic-risk-prioritization" height="30">](./skills/strategic-risk-prioritization)

Prioritize multiple risk points by likelihood and impact to help decision-makers make strategic trade-offs under limited resources.

<br>

<img src="./assets/cat-7-docs.svg" alt="Documents & Case Management" height="38">

> **Theoretical basis**: speech act theory (ensure performative effects of documents) · AGM belief revision theory · normative change logic · operations research & scheduling theory · legal information reduction and compression theory

[<img src="./assets/tag-legal-document-formatting.svg" alt="legal-document-formatting" height="30">](./skills/legal-document-formatting)

Draft complete civil/criminal judgments based on court drafting standards, invoking atomic skills as needed.

[<img src="./assets/tag-judgment-document-generation.svg" alt="judgment-document-generation" height="30">](./skills/judgment-document-generation)

**Compound ability ✦**: orchestrates the same set of atomic abilities to generate a format‑compliant, rigorously reasoned complete criminal judgment.

[<img src="./assets/tag-legal-document-summarization.svg" alt="legal-document-summarization" height="30">](./skills/legal-document-summarization)

Produce structured summaries of judgments, rulings, mediations, arbitrations, and administrative penalties—faithful to the original, objective, highlighting the core while avoiding verbatim reproduction.

[<img src="./assets/tag-multi-document-summarization.svg" alt="multi-document-summarization" height="30">](./skills/multi-document-summarization)

Synthesize across multiple documents to extract consensus views, identify conflicts, and produce unified overviews and new integrative insights.

[<img src="./assets/tag-legal-terminology.svg" alt="legal-terminology" height="30">](./skills/legal-terminology)

Ensure legal terminology is accurate, unambiguous, and consistent with legal style; a fundamental atomic ability across document production.

[<img src="./assets/tag-case-lifecycle-planning.svg" alt="case-lifecycle-planning" height="30">](./skills/case-lifecycle-planning)

Plan case preparation timelines and generate litigation roadmaps with key dates.

[<img src="./assets/tag-trial-scheduling-and-deadline-monitoring.svg" alt="trial-scheduling-and-deadline-monitoring" height="30">](./skills/trial-scheduling-and-deadline-monitoring)

Track and remind of hearings/execution schedules, evidence submission, appeals, service, preservation renewals, and other statutory deadlines.

[<img src="./assets/tag-billing-and-litigation-budget.svg" alt="billing-and-litigation-budget" height="30">](./skills/billing-and-litigation-budget)

Track attorney hours and expenses, prepare and monitor budgets, perform litigation cost analyses, and produce timesheets/expense reports.

<img src="./assets/rule.svg" alt="" width="100%">

## 🎯 Benchmark Coverage

This library's design references mainstream Chinese legal NLP benchmarks. The table below reflects methodological correspondences—i.e., the library provides analytical frameworks and steps required for such tasks—but does not imply quantitative evaluation or specific scores on those datasets.

<details>
<summary><b>📊 LexEval</b> · Six cognitive dimensions</summary>

<br>

| Cognitive Dimension | Representative Tasks | Corresponding Skills |
|:---|:---|:---|
| Memorization | Legal concepts, statutes, legal evolution | `legal-concept-comprehension` · `legal-article-retrieval` · `legal-norm-validity-check` |
| Understanding | Identify legal relations/elements/issues, document summarization | `legal-element-extraction` · `structured-element-extraction` · `dispute-issue-identification` · `legal-document-summarization` |
| Logic Inference | Statute application/charge/sentence prediction, multi-hop reasoning, case identification | `deductive-reasoning` · `formal-legal-consequence` · `legal-judgment-prediction` ✦ · `case-retrieval` |
| Discrimination | Document proofreading, consultation answer quality assessment | `argument-strength-evaluation` · `evidence-evaluation` |
| Generation | Document generation, argument mining, reading comprehension | `legal-document-formatting` · `judgment-document-generation` ✦ · `argument-chain-construction` |
| Ethics | Legal ethics judgment, bias detection, privacy/discrimination identification | `judicial-value-judgment` · `administrative-value-judgment` |

</details>

<details>
<summary><b>📊 LawBench</b> · Three cognitive levels</summary>

<br>

| Cognitive Level | Representative Tasks | Corresponding Skills |
|:---|:---|:---|
| Knowledge Memorization | Statute recall, knowledge QA | `legal-article-retrieval` · `legal-concept-comprehension` |
| Knowledge Understanding | Document proofreading, dispute focus identification, NER, event detection, sentiment summarization, argument mining | `dispute-issue-identification` · `legal-element-extraction` · `legal-document-summarization` · `evidence-argument-chain` |
| Knowledge Application | Statute/charge/sentence prediction, case analysis, legal consultation | `legal-judgment-prediction` ✦ · `formal-legal-consequence` · `deductive-reasoning` |

</details>

<details>
<summary><b>📊 CAIL (2018–2025)</b> · Chinese Legal AI benchmarks</summary>

<br>

| Representative Tasks | Corresponding Skills |
|:---|:---|
| Charge prediction / statute recommendation / sentence prediction | `legal-judgment-prediction` ✦ · `formal-legal-consequence` · `deductive-reasoning` |
| Element recognition / legal element & issue identification | `legal-element-extraction` · `structured-element-extraction` · `dispute-issue-identification` |
| Case retrieval / similar-case matching / explainable case matching | `case-retrieval` · `analogical-reasoning` |
| Judicial summarization / legal public opinion summary | `legal-document-summarization` · `multi-document-summarization` |
| Argument mining / argument understanding | `argument-chain-construction` · `evidence-argument-chain` |
| Judgment fact generation / reasoning generation | `judgment-document-generation` ✦ · `legal-document-formatting` |
| Multi-defendant/multiple-charge prediction / sentencing factor recognition | `legal-judgment-prediction` ✦ · `conflict-resolution` |
| Legal numeric calculation (amounts/compensation/interest) | `formal-legal-consequence` · `billing-and-litigation-budget` |
| Document proofreading / fact finding | `argument-strength-evaluation` · `legal-element-extraction` |

</details>

<details>
<summary><b>📊 Other Benchmarks</b> · JEC-QA / LeCaRD / MSLR / LAiW / JuDGE / CLAW / LeKUBE / LEVEN / AR-Bench / LegalAgentBench</summary>

<br>

| Benchmark | Main Tasks | Corresponding Skills |
|:---|:---|:---|
| **JEC-QA** | Judicial exam knowledge / case QA | `legal-concept-comprehension` · `deductive-reasoning` |
| **LeCaRD / v2** | Legal case retrieval (ranking) | `case-retrieval` · `analogical-reasoning` |
| **MSLR** | IRAC-based multi-step legal reasoning | `deductive-reasoning` · `argument-chain-construction` |
| **LAiW** | Syllogism-based NLU/reasoning/generation | `deductive-reasoning` · `formal-legal-consequence` |
| **JuDGE** | Generate full judgments from facts | `judgment-document-generation` ✦ |
| **CLAW** | Statute retrieval and analysis at article/paragraph/item levels | `legal-article-retrieval` · `legal-norm-validity-check` |
| **LeKUBE** | Legal knowledge update tracking | `legal-norm-validity-check` |
| **LEVEN** | Legal event detection, trigger-word identification | `legal-element-extraction` |
| **AR-Bench** | Judgment error detection/classification/correction | `argument-strength-evaluation` · `evidence-evaluation` |
| **LegalAgentBench / J1-EVAL** | Multi-step agent reasoning, tool calls, process compliance | `legal-judgment-prediction` ✦ · `conflict-resolution` · `strategic-risk-prioritization` |

</details>

<img src="./assets/rule.svg" alt="" width="100%">

## 🚀 Usage

These skills follow the Anthropic Agent Skills `SKILL.md` convention and can be used in any compatible environment—such as **Claude Code**, **Claude Cowork**, or other compatible platforms.

```text
1. Place the required skill directories (any subdirectory under `skills/`) into your skills folder
2. Describe the legal task in natural language — the model will match and invoke appropriate skills based on the `description` trigger conditions
3. Invoke compound abilities for complex tasks (full judgment generation, outcome prediction) and they will automatically schedule required atomic abilities
4. ⚠️ Every output must be reviewed by a qualified legal professional before use
```

### 🔌 External Data via MCP

The library's retrieval skills (`case-retrieval` · `legal-article-retrieval` · `legal-norm-validity-check`) **only define retrieval methodology and do not bind to any database**. To enable retrieval of real, current, and auditable cases and statutes (rather than relying on model memory), the runtime environment must connect to a legal data service compatible with the Model Context Protocol ([MCP](https://modelcontextprotocol.io)).

The skills expect a minimal interface—an environment tool that accepts an input query and returns structured results—so any case/statute database can be integrated. Verified available option: **PKULAW MCP** (Peking University Law Database) with 160M+ cases and 5M+ statutes. Configure by adding a standard server to your MCP client:

```json
{
  "mcpServers": {
    "pkulaw": {
      "url": "https://apim-gw.pkulaw.com/{SERVICE_ID}/mcp",
      "headers": { "Authorization": "Bearer YOUR_TOKEN" }
    }
  }
}
```

> Tokens and `SERVICE_ID` are retrieved from the PKULAW MCP console. **Configure them in your local client only; do not put tokens in `SKILL.md` or commit them to the repository**.
> Full services, links, and integration steps are in [MCP-PKULAW.md](./MCP-PKULAW.md); each skill's integration contract is in its directory README.md.
> ⚠️ If no database is connected, skills can still run but all cases/statutes must be annotated `[to be retrieved]`/`[to be checked]`; do not fabricate.

**Directory structure:**

```text
Legal-Skills-Chinese/
├── README.md
├── CONTRIBUTING.md
├── MCP-PKULAW.md             # ← PKULAW MCP services and links
├── assets/                   # README visual assets (banner, category labels, skill tags SVG)
├── skills/                   # all 38 skills
│   ├── case-retrieval/
│   │   ├── SKILL.md          # retrieval methodology (database-agnostic)
│   │   └── README.md         # ← PKULAW MCP integration notes (case DB)
│   ├── legal-article-retrieval/
│   │   ├── SKILL.md
│   │   └── README.md         # ← integration notes (statute DB)
│   ├── legal-norm-validity-check/
│   │   ├── SKILL.md
│   │   └── README.md         # ← integration notes (statute provenance / hallucination correction)
│   ├── <other-skill>/
│   │   └── SKILL.md          # one SKILL.md per skill directory
│   └── ...
└── .github/ISSUE_TEMPLATE/
    └── submit-skill.yml
```

Each `SKILL.md` begins with YAML frontmatter:

```yaml
---
name: skill-slug          # matches directory name, lowercase hyphen
description: |            # trigger conditions, applicable scenarios, capability boundaries
  ...
---
```

> 📝 **On coverage:** This repository only includes skills that have been implemented as `SKILL.md`. Some conceptual dimensions (knowledge base/statute library construction, clarifying questions for client communication, crisis simulation) are yet to be implemented and will be added later.

<img src="./assets/rule.svg" alt="" width="100%">

## 🤝 Submit a New Skill

We welcome community contributions. **No deep Git expertise required**—you can submit a skill and maintainers will review it for inclusion.

<div align="center">

### 👉 [**Submit a new Skill here!**](../../issues/new?template=submit-skill.yml)

</div>

**Review process:**

1. **Safety first** — check for malicious code, risky content, or inappropriate dependencies.
2. **Legal quality** — reviewed by practicing legal professionals: clear triggers, accurate capability boundaries, alignment with PRC statutory reasoning and practice norms.
3. **Practical value** — assess whether the skill provides usable assistance.

**Minimum to submit a skill:**

- Create a new directory under `skills/` named by the skill slug (lowercase hyphen).
- Add a `SKILL.md` with `name` and `description` in YAML frontmatter.
- In `description`, state: **trigger conditions · applicable scenarios · capability boundaries**.
- For compound abilities, explicitly list the atomic abilities called and the call sequence.

> See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for full guidelines.

<img src="./assets/rule.svg" alt="" width="100%">

## 📄 License

This repository and its documentation are licensed under [Creative Commons CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/): you may fork, copy, and redistribute with attribution; **do not distribute modified versions or use them for commercial purposes**.

This project is for legal research and practice assistance. Users must ensure their usage complies with local regulations on legal services, practitioner qualifications, and AI applications. **Professional responsibility for any external legal work product rests with the practitioner using the outputs, not the project or its contributors.**

## 🙏 Acknowledgments

Thanks to the Anthropic team for open-sourcing the Agent Skills standard and examples that enabled this library. Thanks to every practicing legal professional who authored, validated, and contributed skills—your work is the source of this library's expertise. And thanks to everyone who starred, forked, or bookmarked this project.

## 👥 Team

Hu Yiran, Cheng Rongxin, Li Haitao, Lv Wenbo, Chen Qingjing, Liu Huanghai, Xu Jing, Jiang Fuheng, Wu Xuanhang, Wang Xinyu, Wang Chong, Que Zibing

Contact email: huyr17@outlook.com

<div align="center">
<br>

**⚖️ If this library helps you, please give it a Star — it helps more legal professionals and researchers discover it.**

</div>



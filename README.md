# PM Master（PM宗师）

> PM Master（PM宗师）- 用一线产品与商业思想，训练更稳定的产品判断

PM Master 是一组面向产品经理、创业者、业务负责人和 AI Agent 使用者的产品思维技能包。项目将多位代表性产品与商业实践者的思维模型沉淀为可触发的 Agent Skills，让 AI 在需求分析、产品评审、商业判断、长期决策和表达风格上具备更明确的方法论边界。

当前版本包含 4 个 perspective skill：梁宁、俞军、张小龙、段永平。每个 skill 都围绕本地材料、公开信息核验、核心心智模型、决策启发式和表达 DNA 组织，适合在产品定义、需求讨论、方案评审、战略推演和个人决策中作为「思维顾问」使用。

---

## 快速安装

### 方法一：Git 克隆

```bash
git clone https://github.com/RETHINKAIZ/PM-Master.git
cd PM-Master
```

把需要的 skill 目录复制到你的 agent skills 目录：

```bash
# Codex 示例
cp -r *-perspective "$HOME/.codex/skills/"

# Claude Code 示例
cp -r *-perspective "$HOME/.claude/skills/"
```

复制完成后，重启你的 agent 或刷新 skills 索引即可使用。

### 方法二：手动安装

下载仓库后，将以下目录复制到对应 runtime 的 skills 目录：

```text
duanyongping-perspective/
liangning-perspective/
yujun-perspective/
zhangxiaolong-perspective/
```

常见目录示例：

| Runtime | 示例目录 |
|---|---|
| Codex | `~/.codex/skills/` |
| Claude Code | `~/.claude/skills/` |
| Cursor / 其他兼容 runtime | 以对应 runtime 文档为准 |

---

## 技能列表

| # | 技能名称 | 中文名 | 核心功能 |
|---|---|---|---|
| 1 | `liangning-perspective` | 梁宁产品与增长视角 | 真需求、商业闭环、增长破局、共识工程、点线面体 |
| 2 | `yujun-perspective` | 俞军产品方法论视角 | 用户模型、用户价值、交易模型、产品权衡、理性决策 |
| 3 | `zhangxiaolong-perspective` | 张小龙微信产品观视角 | 人与场景、产品克制、社交系统、体验气质、平台机制 |
| 4 | `duanyongping-perspective` | 段永平本分长期主义视角 | 生意模式、企业文化、现金流、能力圈、长期决策 |

---

## 使用方式

安装后，在支持 skills 的 agent 中直接提到技能名称、人物视角或对应关键词即可触发。

### 中文触发示例

- "用梁宁的视角帮我判断这个需求是不是真需求"
- "按俞军产品方法论分析这个功能的用户价值和交易模型"
- "从张小龙的产品观来看，这个社交功能该不该做"
- "用段永平的方式帮我看这个公司和长期现金流"

### 英文触发示例

- "Use `liangning-perspective` to analyze this growth problem"
- "Use `yujun-perspective` to evaluate the user value of this feature"
- "Use `zhangxiaolong-perspective` to review this social product idea"
- "Use `duanyongping-perspective` to think through this business decision"

---

## 典型使用场景

### 产品需求判断

- 判断用户反馈背后的真实需求
- 区分功能价值、情绪价值和资产价值
- 分析新体验、旧体验和替换成本
- 识别功能是否破坏产品结构和用户心智

### 产品方案评审

- 用不同产品思想交叉审视方案
- 检查用户模型、交易模型和商业闭环
- 识别短期指标与长期价值之间的冲突
- 找到下一步实验、验证或调研动作

### 商业与战略推演

- 判断机会所处的点、线、面、体
- 拆解商业模式、现金流、护城河和企业文化
- 分析平台机制、生态演化和多边利益
- 帮助团队从口号回到具体场景、约束和取舍

### 表达与思考训练

- 模拟不同产品思想家的表达节奏和分析路径
- 为 PRD、方案、复盘和评审会提供思考框架
- 帮助产品经理建立更稳定的判断语言

---

## 目录结构

```text
PM-Master/
├── README.md
├── duanyongping-perspective/
│   ├── SKILL.md
│   ├── references/
│   └── scripts/
├── liangning-perspective/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── test-prompts.json
├── yujun-perspective/
│   ├── SKILL.md
│   ├── references/
│   ├── scripts/
│   └── test-prompts.json
└── zhangxiaolong-perspective/
    ├── SKILL.md
    ├── references/
    ├── scripts/
    └── test-prompts.json
```

---

## 发布前检查

如果准备将项目公开上传到 GitHub，建议先检查以下内容：

- 确认 `references/sources/` 中的本地书籍、PDF、EPUB、原始材料是否具备公开分发授权。
- 如材料仅用于个人研究，建议在公开仓库中移除原始全文或改为保留引用说明、摘要和可公开链接。
- 检查是否存在个人隐私、账号信息、未公开访谈或不可公开数据。
- 为仓库补充明确的 `LICENSE` 文件，说明 skill 内容、脚本和参考材料的使用边界。
- 如后续增加安装脚本或分发包，再同步更新本 README 的安装说明。

---

## 版本信息

- 版本: 0.1.0
- 创建日期: 2026-06-15
- 更新日期: 2026-06-15
- 作者: RETHINKAIZ
- 许可证: 待补充

---

## 联系方式

- 微信: RETHINK-AIZ
- GitHub: [@RETHINKAIZ](https://github.com/RETHINKAIZ)
- 社交媒体: RETHINKAIZ / RETHINKAIZ HABITS

如有问题或建议，欢迎通过以上方式联系。

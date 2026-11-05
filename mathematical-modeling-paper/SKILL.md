---
name: mathematical-modeling-paper
description: Write, revise and audit Chinese mathematical-modeling competition papers with traceable derivations, natural academic prose, native Word equations, reproducible figures and tables, template-based layout and verified supporting files. Use for modeling papers and their code/result consistency, not unrelated academic writing.
metadata:
  version: "2.0.1"
---

# 数学建模论文：从题目到可复现交付

## 先守住四条边界

1. 先解决题目交付的问题，再选模型、组织证据与润色；每项修改都应说明解决了哪一个实际缺口，不为改写而改写。
2. 当前官方赛题、附件和比赛规则优先；用户指定模板控制排版，用户当次指定的修改范围与保留项必须尊重。模板示例数据、宣传性表述、过期赛事说明均不是事实依据。
3. 数学正确性、数值收敛、物理真实性、版面清晰度分别检查。获奖、测试通过、格式整齐都不能替代其他层面的证据；不预测奖项或保证获奖。
4. 修改已有人工作品前记录允许范围、锁定摘要/图尺寸等保留项，另存可回退版本。仅检查时先报告，不擅自改论文或发布材料。

## 工作方式

按当前任务选用相应步骤；一句话润色不需要重跑整套建模。全文任务应覆盖：

- **理解交付。** 把各问题需要的量、条件、时间/空间位置、表格模板、精度、结果文件名列成清单；区分题给量、推导量和显式假设。缺失条件保持符号化，不自行补值凑出唯一答案。
- **建立模型。** 交代对象、变量、坐标、单位和适用条件；由守恒/几何/统计关系推到方程，再选择求解方法。先解释方程从何而来，必要处引用可核验来源。
- **组织正文。** 每问围绕模型、求解、题目要求的结果、解释和检验展开。结果先回答题目指定表格/文件，再给辅助图和检验；避免大段检验抢在答案前面。
- **保持证据一致。** 公式、代码、未舍入结果、图表、摘要与附录共用一套来源。修改数值或编号时同步所有引用；不能凭四位小数的Excel反推未舍入阈值。
- **检验并交付。** 检查早期与末期、边界与内部，说明单位、误差定义和结论范围；渲染PDF检查公式/图表，再从最终ZIP解压复核目录、路径及运行命令。

## 写作与公式的最小要求

- 用做题人的具体表达说明为什么做、怎样算、结果说明什么。避免“根据某节模型与算法设计”这类空泛引导，写实际模型与算法。
- 建模章开头用简短过渡说明本问新增条件、承接什么和下面求什么。父标题下的过渡只在确实需要串起子节时添加，优先移动原有总述，避免逐级重复。
- 图表前说明数据与绘制/提取目的，后用正常正文解释关键数值或趋势。可用“根据……绘制……，如图X所示”“由上表可以看出……”，不要机械复制套话。
- 公式用原生公式对象。属于同一模型的并列方程用一个左大括号组合、各行贴近括号左对齐、共用编号；独立推导不强行合并。编号靠右，不能用空格堆齐。
- 区分微元`d r`与网格步长`Δr`，完整定义下标、时间层、迭代层、控制体界面和边界源项。正文变量也要用正确上下标，不把代码语法原样塞进正文。
- 公式被裁切先检查固定行距、固定行高、公式容器和跨页；不能靠缩小字体或给全篇加空行解决。

## 按任务读取参考

开始正文任务先读[通用写作规则](references/common-writing-rules.md)、[过程与过渡](references/process-writing.md)、[证据追溯](references/evidence-traceability.md)。其余按需要读取，不一次加载全部：

| 当前任务 | 参考文件 |
|---|---|
| Word公式、成组大括号、字母、编号、裁切 | [公式排版](references/equations-word.md) |
| 自然话术、图表前后引导、结果段、压缩语言 | [中文表达范例](references/chinese-writing-playbook.md) |
| 用户指定模板、字体字号、间距、三线表、30页 | [本次模板配置](references/template-profile.md) |
| 图的选型、几何图、星号标点、图例与流程箭头 | [图表流程](references/figure-table-workflow.md) |
| 实际改稿经验、错误反例和不应照搬的部分 | [省一项目复盘](references/competition-retrospective.md) |
| 摘要、关键词和每问结果文件 | [摘要与标题](references/abstract-and-title.md) |
| 小节名称、每问层级 | [标题组织](references/title-structure.md) |
| 模型、代码或数据矛盾 | [模型与代码调试](references/model-code-debugging.md) |
| 机理/几何/仿真、优化、数据题 | [机理](references/physical-mechanism.md)、[优化](references/optimization.md)、[数据](references/data-analysis.md) |
| 最优性、敏感性、反事实、结论范围 | [表述边界](references/claim-boundaries.md) |
| 结构参考优秀论文 | [结构学习](references/award-pattern-imitation.md)、[案例](references/award-case-patterns.md) |
| 全文与终稿 | [全文检查](references/review-checklist.md)、[提交交付](references/final-delivery.md) |

## 可复用检查工具

所有脚本为检查工具，不自动证明模型正确，不自动执行压缩包中的代码：

```text
python scripts/audit_text.py paper.txt --format text
python scripts/audit_final_surface.py paper.txt --format text
python scripts/audit_support_package.py supporting.zip --compile-python --required result1.xlsx --required result2.xlsx
```

表面审查命中后回到原文和原始结果核实。PDF文本提取中的空格、字体拆分、上下标和公式顺序可能失真；没有图像或DOCX证据时，不把提取异常直接断言为原文错误。

## 提交结论要有范围

报告本轮检查的文件、版本/哈希、通过项、缺陷、未验证项及是否做过完整复算。单元测试通过不能写成“四问全程重算通过”；缩略图浏览不能写成“所有公式逐个核验无误”。

AI使用声明、参考文献格式、页数计入范围和文件命名按本届官方要求核验；不把历史模板的AI示例或过往赛制永久当成现行规定。公开分享skill时不默认公开队伍论文、原题附件、个人路径或第三方模板原件。

# 数学建模论文工作流 Skill

把题意、模型、代码、结果、图表、论文和支撑材料连起来的一套可复用工作规则。适用于中文数学建模竞赛论文的写作、精修、排版与提交检查。

本次2.0版根据一次获广东省一等奖的圆柱药材烘干项目及完整改稿经历整理。奖项为作者自述，不代表比赛官方推荐，不保证使用本skill可以获奖。仓库不包含参赛论文、题目附件或第三方模板原件。

## 这次整理了什么

| 你遇到的问题 | Skill如何处理 |
|---|---|
| 公式一条条堆在一起、没有大括号 | 同一数学对象组合成组，左括号内左对齐，一组一个编号 |
| 分式下半部分消失、矩阵太挤 | 分清公式段落行距、内部行距和固定表格行高，局部处理后渲染 |
| 数学字母看似加粗、`c_p`等符号不规范 | 原生公式、上下标、数学字体、单位和全篇符号一致 |
| 作图花太多时间、总在挪图例 | 先确定证据目的、数据和插入尺寸，做一张风格样例，再批量绘制 |
| 星号没对应表格、关键时间没标 | 按规定采样点标记，同色星号、端点时间和阈值说明 |
| 流程图连线断、方向歪、字遮挡 | 短标签、连接走廊、共享分叉、是/否预留空间，按最终尺寸检查 |
| 章首直接进入公式，没有过渡 | 简述本问要算什么、新增条件是什么、下面用什么模型求解 |
| 话术生硬、只写“根据6.1—6.2” | 给具体模型与算法、图表前后句、结果解释与压缩范例 |
| 题目表格被改成另一套 | 指定模板优先，自建表才默认三线表 |
| 正文超页、用户调过的图又被重置 | 优先删重复，锁定摘要和人工图尺寸，不靠缩小字号凑页数 |
| 测试通过但正式JSON全0 | 每个输出写入隔离到临时目录，检查正式文件前后哈希 |
| 改文件夹后主程序/图形/测试失效 | 路径、导入、运行说明、追溯记录与纸面代码一起同步 |
| ZIP有内容却显示异常 | 检查实际成员名、CRC与编码，用平台解压器确认可见 |

## 安装

点击仓库的 **Code → Download ZIP**，解压后找到里面的`mathematical-modeling-paper`文件夹，将其复制到：

```text
Codex:        ~/.codex/skills/mathematical-modeling-paper
Claude Code: ~/.claude/skills/mathematical-modeling-paper
```

若目标已经安装旧版，先备份旧文件夹。这里的`~`表示当前用户目录。重新开启会话后使用：

```text
使用 $mathematical-modeling-paper，检查这篇论文的建模逻辑、公式分组、
图表前后解释及代码结果一致性。只报告问题，先不要改动文件。
```

支持Skill的其他工具可按各自加载规则安装；不保证所有工具对`$`调用语法和`agents/openai.yaml`都有相同支持。参考文档也可直接阅读。

## 常用请求

**精修一问：**

```text
只精修问题二，保留我改过的摘要、图尺寸和数值。
先指出影响理解的缺口，再做最小有用修改。
补好需要的过渡句、公式说明、表格引出和结果解释。
```

**规范公式：**

```text
将同一模型的并列方程用左大括号组合，内部左对齐，一组一个编号。
使用原生Word公式，检查分式和矩阵是否截断；不要改其他章节。
```

**减少作图返工：**

```text
先说明每张图要证明什么、用哪份正式结果及准备插入多大尺寸。
选一张做样例，检查中文、标点、关键时间、图例和箭头后再画其余图。
```

**最终交付：**

```text
核对最终PDF和实际ZIP，检查规定结果文件、目录、代码附录、运行方法和关键数值。
分别说明静态检查、单元测试、短时算例和完整复算做了哪些；不能把测试通过说成全程复算。
```

## 文件导航

- [Skill入口](mathematical-modeling-paper/SKILL.md)
- [公式与Word排版](mathematical-modeling-paper/references/equations-word.md)
- [中文话术与过渡范例](mathematical-modeling-paper/references/chinese-writing-playbook.md)
- [指定模板参数及冲突处理](mathematical-modeling-paper/references/template-profile.md)
- [作图、表格与流程图技巧](mathematical-modeling-paper/references/figure-table-workflow.md)
- [省一项目复盘](mathematical-modeling-paper/references/competition-retrospective.md)
- [终稿、参考文献、附录与ZIP](mathematical-modeling-paper/references/final-delivery.md)

附带的13页模板配置是历史项目配置，不是普遍比赛规定。使用前提供自己的模板、赛题和当届规则，特别是AI使用说明与提交命名要求。

## 检查工具与测试

只需Python 3.10或更高版本，无第三方依赖。脚本只做有限静态检查，不导入或执行压缩包中的程序：

```bash
python mathematical-modeling-paper/scripts/audit_text.py paper.txt --format text
python mathematical-modeling-paper/scripts/audit_final_surface.py paper.txt --format text
python mathematical-modeling-paper/scripts/audit_support_package.py supporting.zip --compile-python --required result1.xlsx --required result2.xlsx
python -m unittest discover -s mathematical-modeling-paper/scripts -p test_audits.py -v
python tools/validate_release.py
```

文本导出会丢失公式层次、字体与真实间距，提示项必须回到原文核实。ZIP工具不检查Excel数值正确性；还需从最终包解压，按说明运行、读取工作簿并对照论文。测试不代表模型已获独立科学验证。

## 许可与素材

本仓库自有文本与代码采用MIT许可证。对原题、第三方模板、论文、字体和其他参考素材的权利不作转授。需要分享自己的参赛论文时另行确认团队与赛事的公开条件。

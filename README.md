# RWS Skills 维护说明

本目录是自定义 RWS Skill 的唯一可编辑源码。工作区层面的使用边界、作者审阅门与来源路由由根目录的 `AGENTS.md` 规定；本文件只规定技能本身的维护方式。

## 本地化结构

- 每个自定义 RWS Skill 的 `SKILL.md` 以英文维护，作为能力定义的 canonical 版本。它负责该 Skill 的范围、边界、来源与出处规则、权限限制、安全约束与作者审阅要求。
- 每个自定义 RWS Skill 提供 `references/workflow.en.md`（英文协作）与 `references/workflow.zh-CN.md`（简体中文协作）；Humanizer 例外，见下。
- `workflow.en.md` 是本地化工作流的 canonical 版本。`workflow.zh-CN.md` 是可维护的本地化：可以调整措辞、术语、对话风格、示例与输出标签，但不得改变 canonical Skill 的范围、证据标准、所有权规则、安全约束或审阅门。
- 脚本与语言中立的技术参考只保留一份。
- 直接呈现给写作者的模板提供本地化变体，例如 `template.en.md` 与 `template.zh-CN.md`，并按目标产物语言选择。

## 变更检查

- 修改 `SKILL.md` 的范围、证据标准、所有权规则或审阅门时，同步检查两个本地化工作流是否仍然一致。
- 不在本目录保存工作区项目材料、草稿或临时输出。

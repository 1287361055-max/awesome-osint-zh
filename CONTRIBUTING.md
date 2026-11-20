# 贡献指南

欢迎为 **Awesome OSINT 简体中文版** 贡献内容！本仓库是 [jivoi/awesome-osint](https://github.com/jivoi/awesome-osint) 的汉化与本地化衍生版本，以 [CC BY-SA 4.0](LICENSE.txt) 协议发布。

> ⚠️ 请注意：上游原仓库明确**不接受由 LLM / AI Agent 提交的 Pull Request**。本汉化版为独立仓库，欢迎人工审校与内容贡献，但请勿将本仓库的改动提交到上游仓库，也不要用自动化账号批量提交 PR。

## 提交内容前请确认

- 阅读 [Awesome 宣言](https://github.com/sindresorhus/awesome/blob/master/awesome.md)，确保新增条目符合清单的定位。
- 先搜索已有条目，避免重复收录。
- 新条目请**按字母顺序**插入；排序时忽略开头的 "The"（或其他语言中对应的冠词）。
- 每个建议单独提交一个 Pull Request，不要一次混入多个无关改动。
- 条目名称保持工具／项目的官方原名（通常不翻译），标题遵循[英文标题大小写规范](http://grammar.yourdictionary.com/capitalization/rules-for-capitalization-in-titles.html)。
- 统一使用以下格式：

  `* [工具名称](链接) - 一句话中文说明。`

- 欢迎提出新分类或改进现有分类方式，但请在 PR 中说明理由。
- 检查拼写、语法与中文标点，删除行尾多余空格。
- PR 与 commit 标题请写清楚改动内容，并在描述中附上相关链接。
- 若条目与你自己或所在组织有关（自我推广），请在提交时主动说明。
- 提交前先问自己一句：「这条内容对做 OSINT 的人到底有什么帮助？」

## 汉化与术语约定

- 所有章节标题、目录、说明文字与条目描述使用**简体中文**；工具名、产品名、命令、URL、用户名保持原文。
- 术语尽量与 [README.md](README.md) 已有译法保持一致（例如 OSINT＝开源情报、CTI＝网络威胁情报、threat hunting＝威胁狩猎、dark web＝暗网）。
- 描述以简洁为准，一句话说清工具用途；不添加主观推荐或夸大宣传。
- 保留原条目中的全部链接，不得删除或替换链接目标。

## 同步上游与重建站点数据

本仓库内容基准为上游 `master` 分支。若上游更新，建议流程：

1. 将上游新增／变更的条目翻译后补入 [README.md](README.md)，目录与章节锚点保持对应；
2. 运行脚本重新生成可视化首页的数据：

   ```bash
   python scripts/build_data.py
   ```

   该脚本会读取 `README.md` 中的章节与 `* [名称](链接) - 描述` 条目，覆盖生成 `data.js`；
3. 打开 [index.html](index.html) 检查分类、条目数量与搜索是否正常，再一并提交。

> 直接编辑 `data.js` 会在下次运行脚本时被覆盖，请始终修改 `README.md`。

## 合规提醒

本清单仅用于合法授权的安全研究、教学与学习。请遵守适用法律法规与目标服务条款，尊重个人隐私与数据保护要求。

感谢你的建议与校对！ 🧙‍♂️

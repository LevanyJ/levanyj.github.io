# Keji Yin · Python First-Stage Portfolio

一个可直接部署在 **GitHub Pages** 上的静态个人作品集网站。主要内容：

- **首页** `index.html`：个人介绍、六个精选课程项目、学习阶段总览。
- **项目详情** `project.html?id=项目ID`：目标、过程、成果、来源与相关代码。
- **24天知识库** `knowledge.html`：可搜索、可筛选的 Day 01–24 课程索引。
- **互动演示** `demos/csv-lab.html`：本地 CSV 读取、字段分析、预览与统计。
- **示例源码** `examples/`：按课程编号组织的精选学习脚本。

## 预览方式

解压后打开根目录的 `index.html`；主页、详情页、知识库和 CSV 演示无需后端环境。

## 修改姓名 / GitHub 账号

网站内容统一存放在 `assets/data.js`。搜索 `"profile"`，按需修改：

```js
"profile": {
  "name": "Keji Yin",
  "subtitle": "Python · Data · AI Workflows",
  "degree": "Business Information Systems / Business Management",
  "githubUsername": "keji7-prog", 
  "contactEmail": "",
  ...
}
```

GitHub 用户名已核实为 `keji7-prog`，填写账号后，首页底部会显示对应 GitHub 链接。暂未填写时链接自动隐藏，不会指向老师的账号或虚构地址。

> 注意：只修改引号中的值，保留原有 JSON 结构与末尾的 `;`。

## GitHub Pages 发布

详见 [`docs/DEPLOY_GUIDE_CN.md`](docs/DEPLOY_GUIDE_CN.md)。关键点：仓库名必须是 **`你的用户名.github.io`**，公开（Public）仓库；上传本目录**内部的所有文件和文件夹**到仓库根目录；GitHub **Settings → Pages → Deploy from a branch → main / (root)**。

## 内容与出处

**本作品集是课程学习成果的整理版本，不应视为全部项目由本人从零独立开发。** Day 01–22 示例代码来源于 Day 24 课件压缩包内部的课程练习归档；Day 24 桌面工具来自同一对话上传的 Python 练习代码；Day 23 根据之前学习记录整理主题索引。交互 CSV Lab 是本次作品集整合时重新实现的展示页面。完整内容审核见 [`docs/PUBLICATION_AUDIT.md`](docs/PUBLICATION_AUDIT.md)。

本仓库不包含账号 Cookie、API Key、课程 PPT/PDF、付费视频、爬取的完整第三方数据库、老师个人介绍、Windows EXE 或任何虚拟环境。

## 技术

原生 HTML / CSS / JavaScript，无构建步骤、无需 npm，适合学习 GitHub Pages 部署过程。
# GitHub Pages 发布流程（对应 Day 24 课程）

## 第一步：检查本地页面

1. 下载并**解压**整个作品集 ZIP。
2. 双击 `index.html` 预览主页，进入项目详情与知识库，确认展示内容。
3. 打开 `assets/data.js` 修改 `profile.name`、`profile.githubUsername` 等个人字段。尚未确定的邮箱可以保持空白。
4. 核对项目描述是否对应你确实做过的练习，并确认有权公开所选教学代码。

## 第二步：创建 GitHub 仓库

1. 打开 <https://github.com> 并登录**自己的** GitHub 账号。
2. 右上角 `+` → **New repository**。
3. Repository name：`keji7-prog.github.io`（已核实的 GitHub 用户名是 `keji7-prog`）。
4. Visibility 选择 **Public**，点击 **Create repository**。
5. 进入仓库，使用 **Add file → Upload files**。如果新建仓库尚未显示 `Add file`，可点击页面提供的 `uploading an existing file`。
6. **进入解压后的文件夹，选中内部全部内容上传**，确保根目录直接出现 `index.html`、`project.html`、`knowledge.html`、`assets`、`demos`、`examples`、`docs`、`README.md` 等，而不是再套一层文件夹。
7. 点击页面底部 **Commit changes**。如果 GitHub 网页上传文件夹不便，可使用本地 Git 命令（见下文）。

## 第三步：启用 GitHub Pages

1. 打开该仓库的 **Settings → Pages**。
2. 在 **Build and deployment** 中选择 **Deploy from a branch**。
3. 分支 **main**，目录 **/ (root)**，点击 **Save**。
4. 在该页面查看部署状态与站点链接：`https://keji7-prog.github.io/`。
5. 如果首页出现 404，先检查仓库名、根目录是否存在小写的 `index.html`、分支是否选中 `main`，以及 **Actions** 中的部署记录；新站点有时需要短暂传播。

## 本地 Git 方式（可选）

以下命令应在**解压后的作品集文件夹内**执行，且须自行替换用户名。假设已经在 GitHub 建立了对应空仓库：

```bash
git init
git add .
git commit -m "Add Python learning portfolio"
git branch -M main
git remote add origin https://github.com/你的GitHub用户名/你的GitHub用户名.github.io.git
git push -u origin main
```

如已有仓库内容、远程配置或 `git` 身份信息，则需按实际情况处理，不要反复使用 `git init` 覆盖工作流。

## 发布后的核查

- 首页可以访问；在导航中可以打开 **精选项目** 和 **知识库**。
- 24 天均可展开，示例源码链接有对应文件。
- CSV Lab 能加载内置样例及本地 CSV。
- 手机浏览器没有横向溢出。
- GitHub 账号、公开邮箱、个人介绍真实准确，没有误用老师的身份信息。
- **不在仓库中上传任何 Cookie、密码、API Token、验证码服务账号或私人数据。**

> 本次文件制作并不代表已经远程上传。只有当你完成提交并在 Pages 页面看到实际访问地址，才算正式上线。

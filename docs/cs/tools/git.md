# Git 命令汇总

## 1. 基础命令

### 仓库操作
- `git init`：在当前目录初始化一个新的 Git 仓库。
- `git clone <url>`：克隆远程仓库到本地。

### 基础操作
- `git status`：查看工作区、暂存区的状态。
- `git add <file>`：将指定文件的更改添加到暂存区。  
- `git add .`：添加所有更改（包括新文件）。
- `git commit -m "message"`：将暂存区的更改提交到本地仓库。
- `git commit -a -m "message"`：不添加暂存区，直接提交到本地仓库。
- `git log`：查看提交历史。
- `git diff`：查看工作区与暂存区的差异。

### 分支管理
- `git branch`：列出本地分支。
- `git branch <name>`：创建新分支。
- `git checkout <branch>` 或 `git switch <branch>`：切换分支。
- `git checkout -b <branch>` 或 `git switch -c <branch>`：创建并切换分支。
- `git merge <branch>`：将指定分支合并到当前分支。
- `git branch -d <branch>`：删除本地分支。
- `git mergetool` 可视化解决冲突合并工具。

### 远程协作
- `git remote -v`：查看远程仓库地址。
- `git remote add <name> <url>`：添加远程仓库。
- `git fetch <remote>`：从远程获取更新（不自动合并）。
- `git pull <remote> <branch>`：拉取远程更新并合并。
- `git push <remote> <branch>`：推送本地提交到远程。
- `git push -u <remote> <branch>`：推送并建立跟踪关系。

### 撤销与恢复
- `git reset HEAD <file>`：将文件从暂存区撤回到工作区。
- `git checkout -- <file>`：丢弃工作区文件的修改。
- `git reset --hard <commit>`：回退到指定提交，丢弃之后的所有更改。
- `git revert <commit>`：通过新提交撤销某次历史提交。

### 临时保存
- `git stash`：暂存未提交的修改。
- `git stash pop`：恢复最近暂存并删除记录。
- `git stash list`：查看暂存记录列表。

### 标签
- `git tag`：列出所有标签。
- `git tag <tagname>`：创建轻量标签。
- `git push <remote> --tags`：推送所有标签到远程。

### 其他实用命令
- `git rm <file>`：从版本控制中删除文件。
- `git mv <old> <new>`：重命名或移动文件。
- `git rebase <branch>`：将当前分支变基到另一分支。
- `git cherry-pick <commit>`：将指定提交应用到当前分支。
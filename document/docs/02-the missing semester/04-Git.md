
# Git
## git常用命令
- `git init`：初始化一个新的git仓库
- `git help`：查看git命令的帮助
- `git status`：查看当前仓库的状态    
- `git add` 文件名：将文件添加到暂存区
- `git commit -m` "提交信息"：将暂存区的文件提交到本地仓库
- `git log`：查看提交历史记录
- `git cat-file -p commit_id`：查看指定提交的详细信息
- `git checkout 文件名`：切换到其他分支,并丢弃未提交的修改
- `git diff 文件名`：查看相对于HEAD的修改
- `git diff 版本号 文件名`：查看相较于指定版本号的修改
- `git diff branch1 branch2 文件名`：查看两个分支之间的差异
## git分支管理
- `git log --all --graph --decorate\-oneline`：查看提交历史记录的图形化展示
- `git branch`：查看本地分支
- `git branch -vv`：查看本地分支的详细信息
- `git branch 分支名`：创建分支
- `git checkout 分支名`：切换到指定分支
- `git checkout -b 分支名`：创建并切换到指定分支
- `git merge 分支名`：合并指定分支到当前分支
- `git mergetool`：使用外部工具解决合并冲突(默认是vimdiff)
- `git merge --abort`：放弃合并
- `git merge --continue`：继续合并
- 合并冲突解决：
    -`git merge`:合并时发现冲突
    - 手动编辑冲突文件，删除不需要的行
    - `git add 文件名`：将冲突文件标记为已解决
    - `git merge --continue`：继续合并
## git远程仓库管理
- `git remote`：查看远程仓库
- `git remote add <remote_name> <remote_url>`：添加远程仓库
- `git push <remote_name> <local_branch_name>:<remote_branch_name>`：推送本地分支到远程仓库
    - tip:另一种做法：`git branch --set-upstream-to=<remote>/<remote_branch> <local_branch>(创建本地和远端分支的关联关系)`  `git push`
- `git clone <remote_url> <local_path>`：克隆远程仓库到本地
- `git clone --shallow <remote_url> <local_path>`：克隆远程仓库的最近一次提交到本地
- `git fetch <remote_name>`：获取远程仓库的最新信息，但不合并到本地
- `git pull <remote_name> <remote_branch_name>:<local_branch_name>`：拉取远程分支到本地
## 其他常用工具
- git设置文件 `~/.gitconfig`
- `git stash`：暂时保存工作区的修改，等以后恢复（恢复到最后一次提交的状态）
- `git stash pop`：恢复暂存区的修改
- `git reset HEAD 文件名`：取消暂存区文件的修改
- `git bisect`：二分查找，用于定位引入bug的提交
  
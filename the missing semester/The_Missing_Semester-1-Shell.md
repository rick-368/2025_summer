## Shell
### 常用Shell命令
- `echo`：打印字符串
- `cd`：切换目录(`cd..`表示返回上一级目录, `cd /`表示切换到根目录, `cd ~`表示切换到用户主目录, `cd -`表示切换到上一次所在目录)   
- `ls`：列出目录内容
- `tree`：以树状图列出目录内容
- `pwd`：打印当前目录路径
- `mkdir`：创建目录
- `mv`：移动或重命名文件或目录
- `rm`：删除文件或目录（`-r`选项可删除目录及其内容）
- `cp`：复制文件或目录
- `rmdir`：删除空目录
- `man`：查看命令的帮助文档
- `cat`：查看文件内容
- `tail`：查看文件末尾内容
- `env`：查看环境变量
> `tail -n10 filename`：查看文件末尾10行内容

-`sudo`：以超级用户权限运行命令
- `su`：切换用户



### 输入输出重定向
- `>`：输出重定向，将命令的输出保存到文件中
>`echo "Hello, world!" > output.txt`

- `<`：输入重定向，将文件的内容作为命令的输入
>`cat < input.txt > output.txt`

-`>>`：追加重定向，将命令的输出追加到文件末尾
>`echo "Hello, world!" >> output.txt`

- `|`：管道命令，将前一个命令的输出作为后一个命令的输入
>`ls -l | tail -n1`：查看当前目录下的文件列表，并只显示最后一行

>重定向错误流：`2>`表示将错误输出保存到文件中，`2>>`表示追加错误输出到文件末尾。



### 变量
变量定义格式：`变量名=值`
`$变量名`：引用变量的值
note: 变量名和值之间不能有空格，也不能使用特殊字符。
字符串：用单引号或双引号括起来，如`'Hello, world!'`或`"Hello, world!"`
note:在双引号中变量可以被其值替换，而在单引号中则不会。
特殊变量：`$?`：上一条命令的返回值(错误码)，`$0`表示当前脚本的文件名，`$n`表示传递给脚本或函数的参数，`$1`表示第一个参数，`$#`表示参数个数，`$@`表示所有参数，`$_`表示上一个命令的最后一个参数。



### 脚本
脚本文件以`.sh`为扩展名，可使用文本编辑器创建。
脚本文件以`#!/bin/bash`开头，表示使用bash解释器执行。
脚本文件中可以包含多个命令，每个命令占一行。
脚本文件可通过命令行执行，也可以通过`source`命令直接执行。
eg:
```bash
#!/bin/bash
mcd(){
    mkdir "$1"
    cd "$1"
}
```

保存为`mcd.sh`，使用命令`source mcd.sh`即可使用该脚本。

脚本输出可以储存在变量中：
eg：
```bash
#!/fool=$(pwd)
echo $fool
```

脚本也可以接受参数：
eg：
```bash
#!/bin/bash
echo "Hello, $1!"
```


### 其他shell工具
- 通配符：`*`匹配任意字符，`?`匹配单个字符，`[]`匹配字符集，`[!]`匹配不在字符集中的字符。
eg:
```bash
ls *.txt
ls [a-z]*.txt
ls project?.txt
```
- {}:用于扩展列表，如`{1..5}`表示1到5。
eg:
```bash
for i in {1..5}; do
    echo $i
done
```
- shellcheck：检查shell脚本语法错误。
- tldr：查看shell命令的简短用法。
- find：搜索文件。
  具体形式：`find 路径 -name 匹配模式 -type 类型 -size 大小`
  eg:
  ```bash
  find . -name "*.tmp" -exec rm {} \;
  ```
  -exec可以在find的结果上执行命令，如上例删除所有名为`.tmp`的文件。
- grep：搜索文本。
  具体形式：`grep 匹配模式 文件名`
  `grep -R 匹配模式 路径`-R选项可以递归搜索子目录。
  eg:
  ```bash
  grep "hello" file.txt
  ```
- rg: 类似于grep，但速度更快,有一些不错的标志可以用。
- history: 查看历史命令。
- fzf: 交互式命令行搜索工具。


### 命令行环境
- 命令行参数：
    - `SIGINT`：中断信号，按下`Ctrl + C`触发。
    - `SIGQUIT`：退出信号，按下`Ctrl + \`触发。
    - `SIGKILL`：强制退出信号，按下`kill -9 pid`触发(无法被捕获)。
    - `SIGTSTP`：暂停信号，按下`Ctrl + Z`触发。
- 任务控制：
    - `bg`：将任务放入后台运行,命令中的 & 后缀可以让命令在直接在后台运行。
           eg: `bg %1`将任务1放入后台运行。
    - `fg`：将后台任务调至前台运行。
    - `jobs`：查看后台任务。
    - `kill`：杀死进程。
        eg: `kill -9 %1`杀死任务1
    -`nohup`：运行命令不挂断，即使终端关闭也不影响命令的执行。
        eg: `nohup command > output.txt 2>&1 &`运行命令并将输出保存到文件，并将命令放入后台运行。



### 终端复用器`tmux`
- `tmux`是一个终端复用器，可以让多个终端会话共存，并在其中切换。
-`tmux`包含三个层次：会话（session）、窗口（window）、面板(pane)。
-`tmux`的命令：
    -`tmux`/`tmux new-session`/`tmux new -t 名称`：创建新的会话。
    -`tmux ls`：查看当前会话。
    -`tmux a`：进入当前会话。
    -`Ctrl+b d`: 分离当前会话。
    -`Ctrl+b c`: 创建新的窗口。
    -`Ctrl+b n`: 切换到下一个窗口。
    -`Ctrl+b p`: 切换到上一个窗口。
    -`Ctrl+b \"`: 命名当前窗口。
    -`Ctrl+b '`: 切换到指定窗口。
    -`Ctrl+b %`: 垂直分割窗口。
    -`Ctrl+b "`：水平分割窗口。
    -`Ctrl+b arrow`: 切换面板。
    -`Ctrl+b space`: 更换面板布局。
    -`Ctrl+b z`: 使当前面板扩张（再按一次恢复）。



### 别名
- `alias alias_name="command_to_alias arg1 arg2"`：设置别名。
  - eg `alias ll='ls -l'`：设置`ll`命令为`ls -l`命令的别名。
- `unalias alias_name`：取消别名。
- `alias`：查看所有别名。
- 别名配置文件：`.bashrc`或`.zshrc`文件中设置别名。



### Dotflies
-很多程序的配置都是通过纯文本格式的被称作 点文件 的配置文件来完成的（之所以称为点文件，是因为它们的文件名以 . 开头，例如 ~/.vimrc。也正因为此，它们默认是隐藏文件，ls 并不会显示它们）。
- 点文件通常位于用户目录下，例如 ~/.bashrc。
- 点文件通常包含环境变量、命令别名、函数定义等。
- 点文件通常在 shell 启动时被读取，并在当前 shell 会话中生效。
- 许多工具可以通过 点文件 进行配置：
    - bash - ~/.bashrc, ~/.bash_profile
    - git - ~/.gitconfig
    - vim - ~/.vimrc 和 ~/.vim 目录
    - ssh - ~/.ssh/config
    - tmux - ~/.tmux.conf 
### ssh
- `ssh`：远程登录服务器。
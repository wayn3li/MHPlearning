# Git
分布式版本控制系统
# 版本控制系统
跟踪每个文件的变化
高效项目成员的协作

## 集中版本控制系统
* SVN
* CVS
![[Pasted image 20231126154035.png]]
所有文件在中央服务器上
每个客户端上都只有一个副本
当需要修改文件时
要从中央服务器上下载最新版本
在客户端上修改完成在上传到中央服务器
优缺点：
* 使用简单

* 中央服务器上的单点故障问题，网络问题等等 

## 分布式版本控制系统
* Git
![[Pasted image 20231126154642.png]]
每个人电脑上都有一个完整的版本库
可以在本地修改，不考虑网络故障
当需要将修改内容分享给其他人时
只需要同步一下仓库
git存储的是元数据，就是说保存的是不同版本之间的差异，而不是所有文件
所以不会占用太多硬盘 

优缺点：
* 免费
* 开源
* 速度快
* 功能强大
* 支持离线工作
* 分支管理

* 使用复杂


tortoiseGit


# 1.安装git
https://git-scm.com/book/zh/v2/%E8%B5%B7%E6%AD%A5-%E5%AE%89%E8%A3%85-Git
本教学只适用于windows系统
# 2.使用git
1. 命令行（推荐）
2. 图形化界面GUI（略）
3. IDE插件/拓展（略）

# 3.常见命令
git的命令都以git开头（为了和linux命令做区分）
1. 配置用户名和邮箱
`git config --global user.name "wayn3li"`
`git config --global user.email levaain@gmail.com`
`git config --global credentyial.helper store`(此命令用于保存以上信息)
>`--global`全局配置，对所有仓库生效
>`--system`系统配置，对所有用户生效
>省略，本地配置，只对本地仓库有效

`git config --global --list`(此命令用于查看刚才的信息)

# 4.新建版本库
版本库，仓库：
repository，简称repo
方式1：本地创建，在想指定的目录运行以下命令
`git init`
![[Pasted image 20231126170023.png]]
空仓库初始化成功
用git bash 打开仓库目录
![[Pasted image 20231126174728.png]]
![[Pasted image 20231126175131.png]]
列出新建仓库目录（git bash最右侧显示master,即main目录）
切换到`.git`目录（git bash最右侧显示GIT_DIR!）
列出`.git`目录下的所有文件如上图
这些文件和目录都是git仓库的重要组成部分
（不要在这乱搞，否则仓库就炸了，这就是为什么`.git`目录是隐藏目录）


方式2：github/gitee克隆
在选定的目录下打开git bash，
运行 `git clone https://github.com/wayn3li/MHPlearning.git`（这里的地址就是教程地址）
![[Pasted image 20231126181105.png]]
然后就可以本地查看编辑了

# 5.git工作区域和文件状态
git本地数据管理：

* 工作区working directory
在资源管理器中可见的目录，实际操作目录

* 暂存区staging area/index(索引)
临时存储区域，用于临时保存即将提交到仓库的修改内容

* 本地仓库local repository
本地创建的仓库，包含完整的项目历史和元数据
git存储代码和版本信息的主要位置


![[Pasted image 20231126183420.png]]
一个完整的修改上传过程如上
过程中可以用git提供的命令来查看，比较或撤销修改
以保证版本控制的准确和完整

文件状态有如下几种
![[Pasted image 20231126194319.png]]
* 未跟踪：未被git管理的文件
* 未修改：已经被git管理的文件（工作区）
* 已修改：已经修改的文件（工作区）
* 已暂存：已经存在暂存区的文件（暂存区）

查看文件状态：`git status`
![[Pasted image 20231126200613.png]]
把新增文件添入仓库文件夹，再次查看仓库状态
![[Pasted image 20231126202813.png]]
未跟踪文件会以红色显示


添加到暂存区（等待被提交到仓库）：`git add <提交目录/提交文件名>`
![[Pasted image 20231126202932.png]]
已暂存文件会以绿色显示
add命令支持：
`git add *.txt` 上传所有以.txt结尾的的文件
`git add .` 上传当前目录的所有文件

查看暂存区的文件：`git ls-files`
![[Pasted image 20231127135007.png]]

上传到仓库（只会提交暂存区的文件们）：
`git commmit -m "上传附属信息"`
![[Pasted image 20231126205234.png]]
也可以直接运行`git commit`在vim中输入上传附属信息
按i插入信息
按esc退出编辑模式
按`:wq`保存退出

提交后不会显示被上传的已暂存文件
![[Pasted image 20231126202300.png]]
**但是未跟踪文件会被显示**


查看上传日志：`git log`
![[Pasted image 20231127085410.png]]
每次提交都有：
* 唯一的提交ID（commit后的16位字符串）
* 作者姓名与邮箱
* 日期
* 注释信息
在引号后输入q退出日志界面

简洁信息：`git log --oneline`
![[Pasted image 20231127091525.png]]


# 6.版本回滚
`git reset --soft <版本ID>`：保存工作区和暂存区的文件

运行后提交历史已经被删除：
![[Pasted image 20231127092619.png]]
暂存区文件仍然存在，会显示为新文件：
![[Pasted image 20231127092644.png]]
工作区文件仍然存在：
![[Pasted image 20231127092707.png]]

`git reset --hard <版本ID>`：**丢弃**工作区和暂存区的文件

![[Pasted image 20231127093615.png]]
运行后提交历史已经被删除：
暂存区和工作区也被删除
![[Pasted image 20231127093718.png]]

`git reset --mixed <版本ID>`：**保存工作区和丢弃暂存区**
略


`git reset HEAD^`   `git reset HEAD~1` ：回滚到上个版本
`git  reset <指定版本ID>`：回滚到指定版本
以上两个命令与`--mixed`同理

`git reflog` 查看操作历史记录

# 7.查看版本差异
更多情况是使用GUI界面来查看
但有时要在没有gui界面（如服务器上）来使用git
所以了解`git diff`的相关命令很有必要

`git diff`
直接对比工作区和暂存区的文件
![[Pasted image 20231127122222.png]]
红色指删除的内容
绿色指新添加的内容

add文件后就不会做显示
![[Pasted image 20231127122545.png]]

`git diff HEAD`：比较工作区和版本库的文件
![[Pasted image 20231127123206.png]]

`git diff --cached`：比较暂存区和版本库的文件
![[Pasted image 20231127123302.png]]
![[Pasted image 20231127123513.png]]

`git diff <1版本ID> <2版本id>`：比较指定两个版本的文件们的差异

`git diff <1版本ID> <2版本id> <特定文件名>`：比较指定两个版本的特定文件的差异

# 8.从版本库删除文件
* 直接本地删除然后提交（不建议）
![[Pasted image 20231127134648.png]]
![[Pasted image 20231127135134.png]]


* `git rm <file>`：把指定文件从工作区和暂存区同时删除
![[Pasted image 20231127144857.png]]

* `git rm --cached <file>`：把指定文件从暂存区删除，但保存到当前工作区中

* `git rm -r *` ： 递归删除某个目录下的所有文件（慎重）

**删除后记得`git commit`提交**
# 9.分支结构
`git branch`查看 Git 仓库的分支情况
![[Pasted image 20231201133730.png]]
显示仓库中的分支情况，现在仅有一个main分支，
其中main分支前的`*`号表示“当前所在的分支”，
例如 * main就意味所在的位置为demo仓库的主分支。
输入命令`git branch a`，再输入命令`git branch`，结果如下图所示：
![[Pasted image 20231201134014.png]]
创建了一个名为a的分支，并且当前的位置仍然为主分支。

`git checkout`切换分支
![[Pasted image 20231201134345.png]]

可以在创建分支的同时，直接切换到新分支，
命令为`git checkout -b`
![[Pasted image 20231201134550.png]]

`git merge`分支合并
![[Pasted image 20231201134854.png]]
注意：合并分支时，要考虑到两个分支是否有冲突，
如果有冲突，则不能直接合并，需要先解决冲突；
反之，则可以直接合并。

`git branch -d`分支删除
![[Pasted image 20231201135125.png]]
有时，通过git branch -d命令会删除不了，
例如分支a的代码没有合并到主分支等，
如果一定要删除该分支，
可以通过命令`git branch -D`进行强制删除。

`git tag <标签>`分支添加标签
如 git tag v1.0
![[Pasted image 20231201140100.png]]
`git tag`查看当前分支标签

`git checkout <标签>`切换到指定标签的分支
![[Pasted image 20231201140913.png]]

































仔细阅读(25min，16:15-16:40)-
长阅读(18min，16：40-16：58)
-翻译（15min，16：58-17:13)
-选词填空（12min，17：13-17：25）的顺序作答。

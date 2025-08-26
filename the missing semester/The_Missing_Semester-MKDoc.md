### MKDocs
#### 介绍
- MKDocs 是一个快速、简单的静态站点生成器，它仅仅是一个 Python 库，可以轻松的生成文档网站。
- 它使用 Markdown 作为标记语言，并有内置的 LiveReload 功能，可以实时预览修改后的内容。
- 它还支持扩展，可以轻松的添加功能，如搜索、评论、多语言支持等。
#### 安装
- 首先，你需要安装 Python 3.6 或更高版本。
- 然后，你可以使用 pip 安装 MKDocs：
```
pip install mkdocs
```
- 可选的，你可以安装 MkDocs-Material 主题：
```
pip install mkdocs-material
```
#### 创建项目
- 你可以使用如下命令创建一个新的 MKDocs 项目：
```
mkdocs new my-project
```
- 这个命令会创建一个名为 my-project 的目录，里面包含一个初始的配置文件和一个示例文档。
#### 运行项目
- 你可以使用如下命令运行项目：
```
mkdocs serve
```
- 这个命令会启动一个本地服务器，监听 8000 端口，并自动更新文档。
- 在浏览器中访问 http://localhost:8000 就可以看到你的文档了。
#### 部署项目
- 在部署项目之前，你需要先在 GitHub 上创建一个仓库，并将项目上传到这个仓库。
- 你可以使用如下命令将项目部署到 GitHub Pages：
```
mkdocs gh-deploy
```
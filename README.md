# 学习笔记


用于记录各个阶段学习的文档,可以使用以下方法将笔记生成html或者pdf

## 环境准备

### linux
[soruce,bash]
----
bundle install --path vendor/bundle
GEM_HOME=`pwd`/vendor/bundle/ruby/2.4.0
GEM_BIN=$GEM_HOME/bin
export GEM_PATH=$GEM_PATH:$GEM_HOME
export PATH=$PATH:$GEM_BIN
asciidoctor-pdf-cjk-kai_gen_gothic-install
----

### windows
[soruce,consle]
----
bundle install --path vendor/bundle
GEM_HOME=`chdir`/vendor/bundle/ruby/2.4.0
GEM_BIN=$GEM_HOME/bin
set GEM_PATH=%GEM_PATH%:%GEM_HOME%
set PATH=%PATH%:%GEM_BIN%
asciidoctor-pdf-cjk-kai_gen_gothic-install
----

[TIP]
下载字体时需要翻墙

== 生成文档

=== linux

[soruce,bash]
----
sh build.sh
----

使用 `asciidoctor` 和 `asciidoctor-pdf` 项目生成文档。

=== windows

[soruce,consle]
----
$ bundle exec rake book:build
Converting to HTML...
 -- HTML output at yinxin的笔记.html
Converting to PDF... (this one takes a while)
 -- PDF  output at yinxin的笔记.pdf
----

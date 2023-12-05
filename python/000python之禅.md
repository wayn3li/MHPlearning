[Python 之禅](https://link.zhihu.com/?target=https%3A//www.python.org/dev/peps/pep-0020/)(Zen of Python)最早由 Tim Peters 于 1999 年发表于 Python 邮件列表中，它包含了影响 Python 编程语言设计的 19 条软件编写原则。

在最初及后来的一些版本中，一共包含 20 条，其中第 20 条是“这一条留空（...）请 Guido 来填写”。这留空的一条从未公布也可能并不存在。

此外，关于 Python 之禅，还有一件趣事。
在 2001 召开第十届国际 Python 峰会（IPC 10，Pycon 的前身）前夕，会议主办方希望定制一件 T 恤，并绞尽脑汁地从投稿的标语中选择了一条 “import this”。

然后，他们决定将这个语句实现在 Python 解释器中，于是将 Python 之禅的内容进行简单加密后放入到了 Python 2.2.1 中的 `this.py` 库当中。如果你在 Python 的解释器中输入 `import this` ，就会显示出来：

```python
>>>import this
The Zen of Python, by Tim Peters

1.Beautiful is better than ugly.

2.Explicit is better than implicit.

3.Simple is better than complex.

4.Complex is better than complicated.

5.Flat is better than nested.

6.Sparse is better than dense.

7.Readability counts.

8.Special cases aren't special enough to break the rules.
9.Although practicality beats purity.

10.Errors should never pass silently.
11.Unless explicitly silenced.

12.In the face of ambiguity, refuse the temptation to guess.

13.There should be one-- and preferably only one --obvious way to do it.
14.Although that way may not be obvious at first unless you're Dutch.

15.Now is better than never.
16.Although never is often better than *right* now.

17.If the implementation is hard to explain, it's a bad idea.

18.If the implementation is easy to explain, it may be a good idea.

19.Namespaces are one honking great idea -- let's do more of those!
20.
```



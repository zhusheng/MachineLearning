# Tensorflow入门

TensorFlow由谷歌人工智能团队谷歌大脑（Google Brain）开发和维护的一个深度学习框架。

## 入门案例

以下是一个加法运算的示例，我们通过tensorflow构建一个tensorflow graph，然后通过session会话执行该graph，我们通过API sess.run()来指定图的输出。除了最终的结果，参与整个图运算的数据我们都可以输出，如果我们需要用到的话。

```python
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

"""
实现一个加法运算，必须遵循以下的格式
"""

# 创建tensor
a = tf.constant(5.0)
b = tf.constant(6.0)

# 创建op
sum = tf.add(a, b)

# 通过Session执行graph
with tf.Session() as sess:
    # run是图的输出
    print(sess.run(sum))
    print(sess.run([a, sum]))
    print(sum.eval())
```

我们通过sess.run(sum)来输出数据sum，如果输出的数据是多个，我们需要使用元组。
我们也可以通过sum.eval()来输出数据sum，运行结果如下：

```bash
11.0
[5.0, 11.0]
11.0
```

## 核心概念

tensorflow = tensor + flow，也就是有向数据流，我们使用tensorflow就是构建一个数据流图，然后执行该图。

tensorflow数据流图核心要素：

- 张量：tensor，数据就是张量
- 节点：operation(op),所有的运算操作都是一个op
- 图：graph，整个程序的结构就是一个graph，定义了整个程序的框架
- 会话：session，用来运行图

说明：

- tensorflow是一个`计算密集型的框架`，`主要是cpu/gpu计算`；
- django/scrapy等框架是IO密集型框架，主要是磁盘操作；

### tensor(张量)

tensorflow graph中的数据都是张量,示例如下：

```python
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

a = tf.constant(5.0)
b = tf.constant(6.0)
sum = tf.add(a, b)
print(a)
print(sum)
```

输出结果如下：

```bash
Tensor("Const:0", shape=(), dtype=float32)
Tensor("Add:0", shape=(), dtype=float32)
```

我们看到结果都是Tensor对象。

### op(操作)

只要使用tensorflow的API定义的函数都是op，如constant()、add()，tensorflow的op非常丰富。

### graph(图)

tensorflow有一个默认图，如果我们不指定图的话，默认就是在默认图上运行的。

- 默认图

如果我们不指定图的话，我们使用的是Tensorflow的默认图，它会自动调用`graph = tf.get_default_graph()`，相当于给程序分配一段内存，我们所有的Tensor、op都是在这张图上。

```python
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 新建2个tensor
a = tf.constant(1.0)
b = tf.constant(2.0)
# 新建1个op
sum = tf.add(a,b)

print(a.graph)
print(b.graph)
print(sum.graph)

# 默认图
graph = tf.get_default_graph()
print(graph)

with tf.Session() as sess:
    # 查看会话所在图
    print(sess.graph)  
```

运行结果如下：

```bash
<tensorflow.python.framework.ops.Graph object at 0x1114caf98>
<tensorflow.python.framework.ops.Graph object at 0x1114caf98>
<tensorflow.python.framework.ops.Graph object at 0x1114caf98>
<tensorflow.python.framework.ops.Graph object at 0x1114caf98>
<tensorflow.python.framework.ops.Graph object at 0x1114caf98>
```

通过运行结果，我们发现tensor、op和session都在一个图上，也就是系统的默认图。`with tf.Session() as sess:`相当于`with tf.Session(graph=g) as sess:`。

- 自定义图

默认使用的是tensorflow默认图，我们也是可以自定义图。示例：

```python
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# 创建图
g = tf.Graph()

# 使用自定义的图
with g.as_default():
    pass
```

### session(会话)

session是一个会话，tensorflow的graph都必须在Session中执行。

- 会话的作用

1. 运行图的结构
2. 分配资源计算，决定graph在什么设备上运行
3. 掌握资源（变量的资源、队列、线程）

会话对象，我们可以执行创建、运行和关闭等操作。

```python
s = tf.Session()
s.run()
s.close()
```

### 上下文环境

会话就是graph的上下文环境，只要有Session就有上下文环境。

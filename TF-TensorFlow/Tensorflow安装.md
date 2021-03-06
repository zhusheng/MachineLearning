# Tensorflow安装

## 创建隔离环境

创建隔离环境，取名为`tensorflow`

```bash
mkvirtualenv -p python3.6 tensorflow
```

## 类型选择

必须选择以下类型的TensorFlow之一来安装：

- TensorFlow仅支持CPU支持。如果您的系统没有NVIDIA®GPU，则必须安装此版本。请注意，此版本的TensorFlow通常会更容易安装（通常在5或10分钟内），因此即使您有NVIDIA GPU，我们建议先安装此版本。
- TensorFlow支持GPU。TensorFlow程序通常在GPU上比在CPU上运行得更快。因此，如果您的系统具有满足以下所示先决条件的NVIDIA®GPU，并且您需要运行性能关键型应用程序，则应最终安装此版本。

## 安装

### Ubuntu和Linux

如果要安装GPU版本的，需要安装一大堆NVIDIA软件(不推荐)：

- CUDA®Toolkit 8.0。有关详细信息，请参阅 NVIDIA的文档。确保您将相关的Cuda路径名附加到 LD_LIBRARY_PATH环境变量中，如NVIDIA文档中所述。 与CUDA Toolkit 8.0相关的NVIDIA驱动程序。
- cuDNN v5.1。有关详细信息，请参阅 NVIDIA的文档。确保CUDA_HOME按照NVIDIA文档中的描述创建环境变量。
- 具有CUDA Compute Capability 3.0或更高版本的GPU卡。有关支持的GPU卡的列表，请参阅 NVIDIA文档。
- libcupti-dev库，即NVIDIA CUDA Profile Tools界面。此库提供高级分析支持。要安装此库，请发出以下命令：

使用pip安装,分别有2.7和3.6版本的

```python
# 仅使用 CPU 的版本
$  pip install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp27-none-linux_x86_64.whl

$  pip3 install https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-1.0.1-cp36-cp36m-linux_x86_64.whl
```

### Mac

#### 安装方式1

macX下也可以安装2.7和3.4、3.5的CPU版本

```python
# 2.7
$ pip install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.1-py2-none-any.whl

# 3.4、3.5
$ pip3 install https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.0.1-py3-none-any.whl
```

#### 安装方式2

```bash
# 安装最新版本
pip install --upgrade tensorflow

# 安装指定版本
pip install tensorflow==1.12.0
```

#### 验证安装指令

```bash
python -c "import tensorflow as tf; tf.enable_eager_execution(); print(tf.reduce_sum(tf.random_normal([1000, 1000])))"
```

#### 补充：安装tensorboard

tensorboard是tensorflow提供的可视化界面，建议和tensorflow安装一样的版本。

```bash
# 安装指定版本
pip install tensorboard==1.12.0
```


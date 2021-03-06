import tensorflow as tf
import os

"""
从TFRecord中读取数据
"""

# 定义cifar的数据等命令行参数
FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_string("cifar_dir", "/Users/zhusheng/WorkSpace/Dataset/3-cifar-10/cifar-10-batches-bin", "文件的目录")
tf.app.flags.DEFINE_string("cifar_tfrecords", "/Users/zhusheng/WorkSpace/Dataset/3-cifar-10/tmp/cifar.tfrecords", "存进tfrecords的文件")

def read_from_tfrecords(file_path):
    """
    读取tfrecords
    :return: None
    """

    file_queue = tf.train.string_input_producer([file_path, ])

    # 1、构造TFRecords阅读器
    reader = tf.TFRecordReader()
    key, value = reader.read(file_queue)

    # 2、解析Example
    features = tf.parse_single_example(value, features={
        "image": tf.FixedLenFeature([], tf.string),
        "label": tf.FixedLenFeature([], tf.int64),
    })

    # 3、转换格式，bytes解码
    image = tf.decode_raw(features["image"], tf.uint8)

    # 设置静态形状
    image.set_shape([32 * 32 * 3])
    #print("image:",image)
    # image: Tensor("DecodeRaw:0", shape=(3072,), dtype=uint8)

    # 可用于转换动态形状
    image_tensor = tf.reshape(image, [32, 32, 3])
    #print("image_tensor:",image_tensor)
    # image_tensor: Tensor("Reshape:0", shape=(32, 32, 3), dtype=uint8)

    label = tf.cast(features["label"], tf.int32)
    #print("label:",label)
    # label: Tensor("Cast:0", shape=(), dtype=int32)

    # 批处理
    image_batch, label_batch = tf.train.batch([image_tensor, label], batch_size=10, num_threads=1, capacity=10)
    #print("image_batch:",image_batch)
    #print("label_batch:",label_batch)
    # image_batch: Tensor("batch:0", shape=(10, 32, 32, 3), dtype=uint8)
    # label_batch: Tensor("batch:1", shape=(10,), dtype=int32)

    return image_batch, label_batch


if __name__=="__main__":

    # 从TFRecord文件中读取数据，首先得有这个文件。
    image_batch, label_batch = read_from_tfrecords(FLAGS.cifar_tfrecords)

    with tf.Session() as sess:
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        # 打印读取的结果
        print(sess.run([image_batch, label_batch]))

        coord.request_stop()
        coord.join(threads)
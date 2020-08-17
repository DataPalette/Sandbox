import os # system env info 라이브러리
import tensorflow as tf # tf 호출

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # avx/avx2 지원 오류 경고 무시
test_words = tf.constant('test for my py, pycharm with git')
sess = tf.Session()
print('version : ', tf.__version__)
print(sess.run(test_words))


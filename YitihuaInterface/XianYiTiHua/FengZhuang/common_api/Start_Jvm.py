
import jpype
import os


#开启虚拟机

def start_jvm():

    jarpath = os.path.join(os.path.abspath("../.."), "E://zxepay-security-sdk-1.0-SNAPSHOT-jar-with-dependencies.jar")

    # 获取jvm.dll 的文件路径
    jvmPath = jpype.getDefaultJVMPath()

    # 开启jvm
    jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % (jarpath))




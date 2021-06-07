
import jpype
import os


#开启虚拟机

def start_jvm():

    # 利用绝对路径找到jar包
    # jarpath = os.path.join(os.path.abspath("../.."), "E://zxepay-security-sdk-1.0-SNAPSHOT-jar-with-dependencies.jar")

    # 我自己写的，返回当前路径，系统会返回： F:\python\zxepay_Interface_Auto\zxepay
    jarpath = os.path.abspath(os.getcwd())

    aa =jarpath + "\zxepay-security-sdk-1.0-SNAPSHOT-jar-with-dependencies.jar"


    # 获取jvm.dll 的文件路径
    jvmPath = jpype.getDefaultJVMPath()

    # 开启jvm
    jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % (aa))



if __name__ == '__main__':
    start_jvm()



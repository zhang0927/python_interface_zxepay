import jpype


def jia_mi(data):

    javaClass = jpype.JClass("com.zxepay.security.sdk.JmeterCrypto")
    reqstr = javaClass.signAndEncrypt(str(data))

    da = str(reqstr)

    return da








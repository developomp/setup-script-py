from src.util import paru_install

name = "JDK"


def setup():
    """
    Java development kit


      jdk-openjdk: latest jdk (17 as of writing)
     jdk8-openjdk: jdk8
    jdk11-openjdk: jdk11
    """

    paru_install(["jdk-openjdk", "jdk8-openjdk", "jdk11-openjdk"])

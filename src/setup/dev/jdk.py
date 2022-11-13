from src.util import paru_install

desc = "Java development kit"


def setup():
    paru_install(
        [
            "jdk-openjdk",  # latest jdk (17 as of writing)
            "jdk8-openjdk",  # jdk8
            "jdk11-openjdk",  # jdk11
        ]
    )

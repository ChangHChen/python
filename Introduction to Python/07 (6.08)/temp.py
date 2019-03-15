class Computer (object):
    def __init__(self, os, memory, storage):
        self.os = os
        self.memory = memory
        self.storage = storage

    def __str__(self):
        return f"[Computer] {self.os}, Memory: {self.memory}GB, Storage: {self.storage}TB"


com1 = Computer("macOS", 32, 3)
com2 = Computer("Window 10", 16, 4)

print(f""""instanceを生成した
    #1:{com1}
    #2:{com2}
    """)

print(f"""{com1.os}のメモリは{com1.memory:d}GB
メモリを増やした""")
com1.memory += 32
print(f"""com1
""")

print(f"{com2.os}のストレージを10TBにする")
com2.storage = 10
print(f"{com2.storage:d}TBになった")

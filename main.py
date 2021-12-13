from threading import Thread


class Thread1(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(9999999):
            string = "thread initialized" + self.name

            print(string)


def init():
    for i in range(999999):
        name = "Thread #%s" % (i + 1)
        theThread = Thread1(name)
        theThread.start()


if __name__ == "__main__":
    init()

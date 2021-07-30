from libs.motor import Motor


class testMotor(Motor):
    def __init__(self):
        Motor.__init__(self)
        self.init_motor("main_motor")
        self.set_debug(True)

    def test(self):
        self.control(1, 1000)


test = testMotor()
test.test()

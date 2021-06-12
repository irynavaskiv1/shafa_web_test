from helpers.base_pytest import Base


class BaseSeleniumToAndroidTestCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.width = 480
        cls.height = 800
        super(BaseSeleniumToAndroidTestCase, cls).setUp()

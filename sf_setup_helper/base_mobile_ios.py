from sf_setup_helper.base_pytest import Base


class BaseSeleniumToIOSTestCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.width = 380
        cls.height = 700
        super(BaseSeleniumToIOSTestCase, cls).setUp()

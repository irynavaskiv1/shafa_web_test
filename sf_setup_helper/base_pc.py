from sf_setup_helper.base_pytest import Base


class BaseSeleniumToPCTestCase(Base):

    @classmethod
    def setUpClass(cls):
        cls.width = 1366
        cls.height = 768
        super(BaseSeleniumToPCTestCase, cls).setUp()

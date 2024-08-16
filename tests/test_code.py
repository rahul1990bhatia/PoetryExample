from simple_poetry_package.hello_world import HelloWorld

class TestPoetryPackage:

    def test_hello_world(self):
        hw = HelloWorld('pytest')
        assert hw.get_name() == 'pytest'
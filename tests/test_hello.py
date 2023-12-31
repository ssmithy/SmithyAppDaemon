from appdaemon_testing.pytest import automation_fixture
from apps.hello import HelloWorld

@automation_fixture(
    HelloWorld
)
def hello_fixture() -> HelloWorld:
    pass

def test_init(hass_driver, hello_fixture: HelloWorld):
    alloAllo = hello_fixture.sayHello()
    assert alloAllo == "Hello!"
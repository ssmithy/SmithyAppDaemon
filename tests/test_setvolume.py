from unittest import mock
from appdaemon_testing.pytest import automation_fixture
from apps.setvolume import SetVolume

@automation_fixture(
    SetVolume,
    args={
        "speaker": "media_player.speaker",
        "normalVolume": 70,
        "nightVolume": 35,
        "enforce": True
    }
)
def app_fixture() -> SetVolume:
    pass

def test_init(hass_driver, app_fixture: SetVolume):
    # Test initilization and default values
    assert app_fixture.speaker == "media_player.speaker"
    assert app_fixture.normalVolume == 70
    assert app_fixture.nightVolume == 35
    assert app_fixture.enforce == True


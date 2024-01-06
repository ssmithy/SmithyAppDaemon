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

from freezegun import freeze_time
import datetime

@freeze_time("2012-01-14")
def test():
    assert datetime.datetime.now() == datetime.datetime(2012, 1, 14)

def test_manual_tick():
    initial_datetime = datetime.datetime(year=1, month=7, day=12,
                                        hour=15, minute=6, second=3)
    with freeze_time(initial_datetime) as frozen_datetime:
        assert frozen_datetime() == initial_datetime

        frozen_datetime.tick()
        initial_datetime += datetime.timedelta(seconds=1)
        assert frozen_datetime() == initial_datetime

        frozen_datetime.tick(delta=datetime.timedelta(seconds=10))
        initial_datetime += datetime.timedelta(seconds=10)
        assert frozen_datetime() == initial_datetime

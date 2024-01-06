from appdaemon_testing.pytest import automation_fixture
from unittest.mock import MagicMock, call
from appdaemon.plugins.hass import hassapi as hass
from apps.timerapp import TimerApp
from freezegun import freeze_time
import datetime

@automation_fixture(
    TimerApp
)
def test_fixture() -> TimerApp:
    pass


@freeze_time("2024-01-06 08:00:00")
def test_daytime(hass_driver, test_fixture: TimerApp):
    assert datetime.datetime.now().hour == 8

@freeze_time("2024-01-06 21:00:00")
def test_nighttime(hass_driver, test_fixture: TimerApp):
    assert datetime.datetime.now().hour == 21



def test_init(hass_driver, test_fixture: TimerApp):
    initial_datetime = datetime.datetime(year=1, month=7, day=12,
                                        hour=15, minute=6, second=3)
    
    with freeze_time(initial_datetime) as frozen_datetime:
        assert frozen_datetime() == initial_datetime
        assert test_fixture.event_flag == 1
        frozen_datetime.tick()
        initial_datetime += datetime.timedelta(seconds=1)
        assert frozen_datetime() == initial_datetime
        assert test_fixture.event_flag == 1

        frozen_datetime.tick(delta=datetime.timedelta(seconds=10))
        initial_datetime += datetime.timedelta(seconds=10)
        assert frozen_datetime() == initial_datetime


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
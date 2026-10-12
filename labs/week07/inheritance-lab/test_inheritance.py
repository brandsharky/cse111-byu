from byu_pytest_utils import with_import, dialog, this_folder, test_files
import pytest


@with_import("instruments", "Instrument")
def test_Q2_instrument(Instrument, capfd):
    trumpet = Instrument(0, "trumpet", "Bb", "brass")
    assert trumpet.subtype == "Bb"
    trumpet.play_sound()
    out, _ = capfd.readouterr()
    assert out == "trumpet played a sound\n"

    with pytest.raises(ValueError):
        Instrument(1, "oboe", "oboe", "double reed")


@with_import("instruments", "Instrument")
@with_import("instruments", "Percussion")
def test_Q2_percussion(Percussion, Instrument, capfd):
    timpani = Percussion(3, "timpani", "timpani")
    assert isinstance(timpani, Instrument)
    assert timpani.family == "percussion"
    timpani.play_sound()
    out, _ = capfd.readouterr()
    assert out == "timpani played a sound\n"

    with pytest.raises(ValueError):
        Percussion(4, "siren", "whistle")


@with_import("instruments", "Instrument")
@with_import("instruments", "Percussion")
@with_import("instruments", "Xylophone")
def test_Q2_xylophone(Xylophone, Percussion, Instrument, capfd):
    xylo = Xylophone(4)
    assert isinstance(xylo, Percussion)
    assert isinstance(xylo, Instrument)
    assert xylo.subtype == "mallet percussion"
    xylo.play_sound()
    out, _ = capfd.readouterr()
    assert out == "xylophone played 'Clink!'\n"


@with_import("drone", "Drone")
@with_import("drone", "SurveyDrone")
@with_import("drone", "DeliveryDrone")
@with_import("drone", "RacingDrone")
def test_Q3_drone(RacingDrone, DeliveryDrone, SurveyDrone, Drone):
    scout = Drone("Scout", "survey")
    assert not scout.inspected
    assert str(scout) == "Scout is a survey drone"
    scout.inspect()
    assert scout.inspected

    assert issubclass(SurveyDrone, Drone)
    assert issubclass(DeliveryDrone, Drone)
    assert issubclass(RacingDrone, Drone)

    survey_drone = SurveyDrone("Maple")
    delivery_drone = DeliveryDrone("Parcel-1")
    racing_drone = RacingDrone("Comet")
    assert isinstance(survey_drone, Drone)
    assert isinstance(delivery_drone, Drone)
    assert isinstance(racing_drone, Drone)
    assert survey_drone.drone_type == "survey"
    assert delivery_drone.drone_type == "delivery"
    assert racing_drone.drone_type == "racing"


@with_import("drone", "Drone")
@with_import("hangar", "Hangar")
def test_Q3_hangar(Hangar, Drone):
    hangar = Hangar("Sky Lab")
    assert hangar.drones == []
    hangar.add_drone(Drone("Maple", "survey"))
    hangar.add_drone(Drone("Parcel-1", "delivery"))
    hangar.add_drone(Drone("Comet", "racing"))
    assert str(hangar) == "Sky Lab has 3 drones"
    assert len(hangar.need_to_inspect()) == 3
    hangar.drones[0].inspect()
    assert len(hangar.need_to_inspect()) == 2


@dialog(test_files / "test_Q3_launch_day.dialog.txt", this_folder / "launch_day.py")
def test_Q3_launch_day():
    ...


@with_import("content", "ContentItem")
@with_import("content", "Livestream")
@with_import("content", "Tutorial")
def test_Q4_content_item(Tutorial, Livestream, ContentItem):
    clip = ContentItem("Loops in 5", "clip", 12, 3)
    assert clip.minutes_per_segment() == 4

    live = Livestream("Late Night Debug", 60, 4, "Nova")
    assert issubclass(Livestream, ContentItem)
    assert isinstance(live, ContentItem)
    assert live.content_type == "livestream"
    assert live.host == "Nova"
    assert live.minutes_per_segment() == 15

    guide = Tutorial("Intro to Git", 45, 5, 1)
    assert issubclass(Tutorial, ContentItem)
    assert isinstance(guide, ContentItem)
    assert guide.content_type == "tutorial"
    assert guide.level == 1
    guide.level_up(2)
    assert guide.level == 3


@with_import("content", "ContentItem")
@with_import("content", "Tutorial")
@with_import("content_platform", "Platform")
def test_Q4_platform(Platform, Tutorial, ContentItem):
    platform = Platform("Creator Hub")
    assert platform.content_items == []

    guide = Tutorial("Testing Basics", 40, 4, 2)
    platform.publish(guide)
    short = ContentItem("Daily Update", "clip", 5, 1)
    platform.publish(short)
    assert len(platform.content_items) == 2
    assert platform.is_published(short)

    platform.archive(guide)
    assert len(platform.content_items) == 1

    with pytest.raises(ValueError):
        platform.archive(ContentItem("Missing Episode", "clip", 6, 2))

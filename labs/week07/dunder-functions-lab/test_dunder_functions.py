from byu_pytest_utils import with_import


@with_import('dragon_zoo', 'Dragon')
def test_Q2_dragon(Dragon):
    smaug = Dragon("Smaug", "Fire Dragon", 100)
    assert str(smaug) == "Smaug is a 100-year-old Fire Dragon. They still need to be fed today."
    smaug2 = Dragon("Smaug", "Fire Dragon", 100)
    assert smaug == smaug2

    smaug.feed()
    assert smaug != smaug2
    smaug.birthday()
    assert str(smaug) == "Smaug is a 101-year-old Fire Dragon. They have already been fed today."
    assert repr(smaug) == "Dragon('Smaug', 'Fire Dragon', 101)"


@with_import('dragon_zoo', 'Dragon')
@with_import('dragon_zoo', 'Zoo')
def test_Q2_zoo(Zoo, Dragon):
    toothless = Dragon("Toothless", "Night Fury", 30)
    stormfly = Dragon("Stormfly", "Deadly Nadder", 25)
    zoo = Zoo([toothless])

    zoo.add_dragon(stormfly)
    assert zoo.dragons == [toothless, stormfly]

    zoo.add_enclosure("1")
    zoo.move_dragon(toothless, "1")
    zoo.move_dragon(stormfly, "1")
    assert str(zoo) == "Zoo: {'1': [Dragon('Toothless', 'Night Fury', 30), Dragon('Stormfly', 'Deadly Nadder', 25)]}"

    zoo.add_enclosure("2")
    zoo.move_dragon(stormfly, "2")
    assert str(zoo) == "Zoo: {'1': [Dragon('Toothless', 'Night Fury', 30)], '2': [Dragon('Stormfly', 'Deadly Nadder', 25)]}"

    assert str(toothless) == "Toothless is a 30-year-old Night Fury. They still need to be fed today."
    assert str(stormfly) == "Stormfly is a 25-year-old Deadly Nadder. They still need to be fed today."
    zoo.feed_all_dragons()
    assert str(toothless) == "Toothless is a 30-year-old Night Fury. They have already been fed today."
    assert str(stormfly) == "Stormfly is a 25-year-old Deadly Nadder. They have already been fed today."


@with_import('library', 'Book')
def test_Q3_book_str_and_repr(Book):
    b1 = Book(0, 'A Tale of Two Cities', 'Charles Dickens')
    assert repr(b1) == "Book(0, 'A Tale of Two Cities', 'Charles Dickens')"
    assert str(b1) == "A Tale of Two Cities by Charles Dickens"


@with_import('library', 'Library')
@with_import('library', 'Book')
def test_Q3_library_str_and_repr(Book, Library):
    b1 = Book(0, "A Tale of Two Cities", "Charles Dickens")
    b2 = Book(1, "The Hobbit", "J.R.R. Tolkien")
    l = Library([b1, b2])

    assert repr(l) == "Library([Book(0, 'A Tale of Two Cities', 'Charles Dickens'), Book(1, 'The Hobbit', 'J.R.R. Tolkien')])"
    assert str(l) == 'A Tale of Two Cities by Charles Dickens | The Hobbit by J.R.R. Tolkien'


@with_import('animal', 'Animal')
def test_Q4_animal(Animal):
    larry = Animal('Larry', 'dolphin')
    fred = Animal('Fred', 'penguin')
    assert str(larry) == "Larry is a dolphin"
    assert str(fred) == "Fred is a penguin"
    assert repr(larry) == "Animal('Larry', 'dolphin')"
    assert repr(fred) == "Animal('Fred', 'penguin')"

    assert larry != fred
    fred2 = Animal('Fred', 'penguin')
    assert fred2 == fred

    assert not larry.make_sound()


@with_import('animal', 'Animal')
@with_import('animal', 'Lion')
def test_Q4_lion(Lion, Animal):
    simba = Lion('Simba')
    nala = Lion('Nala')
    assert isinstance(simba, Animal)

    assert str(simba) == "Simba is a lion"
    assert str(nala) == "Nala is a lion"
    assert repr(simba) == "Lion('Simba')"
    assert repr(nala) == "Lion('Nala')"

    assert simba != nala
    simba2 = Lion('Simba')
    assert simba2 == simba

    assert simba.make_sound() == "Roar"


@with_import('astronomical_object', 'AstronomicalObject')
def test_Q5_atronomical_object(AstronomicalObject):
    messier_87 = AstronomicalObject('Messier 87', 'elliptical galaxy', 53490000)
    assert str(messier_87) == "Messier 87 is a elliptical galaxy located 53490000 light-years away from Earth."
    assert repr(messier_87) == "AstronomicalObject('Messier 87', 'elliptical galaxy', 53490000)"

    sagittarius_A = AstronomicalObject('Sagittarius A', 'supermassive black hole', 26670)
    assert str(sagittarius_A) == "Sagittarius A is a supermassive black hole located 26670 light-years away from Earth."
    assert repr(sagittarius_A) == "AstronomicalObject('Sagittarius A', 'supermassive black hole', 26670)"

    assert messier_87 != sagittarius_A
    messier_87_copy = AstronomicalObject('Messier 87', 'elliptical galaxy', 53490000)
    assert messier_87 == messier_87_copy


@with_import('astronomical_object', 'Planet')
def test_Q5_planet(Planet):
    neptune = Planet('Neptune', 0.0005, True)
    assert str(neptune) == "Neptune is a planet located 0.0005 light-years away from Earth. It is in our solar system."
    assert repr(neptune) == "Planet('Neptune', 0.0005, True)"

    proxima_centauri_b = Planet('Proxima Centauri b', 4.24, False)
    assert str(proxima_centauri_b) == "Proxima Centauri b is a planet located 4.24 light-years away from Earth. It is outside of our solar system."
    assert repr(proxima_centauri_b) == "Planet('Proxima Centauri b', 4.24, False)"


@with_import('astronomical_object', 'Star')
def test_Q5_star(Star):
    proxima_centauri = Star('Proxima Centauri', 4.25, 3042)
    assert str(proxima_centauri) == "Proxima Centauri is a star located 4.25 light-years away from Earth. It has a surface temperature of 3042 K."
    assert repr(proxima_centauri) == "Star('Proxima Centauri', 4.25, 3042)"

    sirius_a = Star('Sirius A', 8.61, 9940)
    assert str(sirius_a) == "Sirius A is a star located 8.61 light-years away from Earth. It has a surface temperature of 9940 K."
    assert repr(sirius_a) == "Star('Sirius A', 8.61, 9940)"

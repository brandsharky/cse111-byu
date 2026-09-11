from byu_pytest_utils import dialog, test_files, this_folder, ensure_missing, tier, visibility


core = tier('Core', 1)
advanced = tier('Advanced', 2)
excellent = tier('Excellent', 3)

alt_const_values = {"COST_LARGE":15.78, "COST_MEDIUM":13.25, "COST_SMALL":8.39,
                    "DIAMETER_LARGE":24, "DIAMETER_MEDIUM":18, "DIAMETER_SMALL":15,
                    "PEOPLE_PER_LARGE":9, "PEOPLE_PER_MEDIUM":5, "PEOPLE_PER_SMALL":2}

def create_alternative_constants_file(source_file, output_file):
    """Reads the source file, changes constants based on alt_const_values, and saves the result to output_file."""
    with open(source_file, "r") as src:
        lines = src.readlines()

    constants_not_found = set(alt_const_values.keys())

    with open(output_file, "w") as dest:
        for line in lines:
            if '=' not in line:
                dest.write(line)
                continue

            var, val = line.split("=", 1)
            var, val = var.split(':')[0].strip(), val.strip()
            if var not in alt_const_values:
                dest.write(line)
                continue

            constants_not_found.remove(var)
            dest.write(f"{var} = {alt_const_values[var]}\n")
    
    assert len(constants_not_found) == 0, f"Some constant(s) not found: {constants_not_found}.\nMake sure constants are named exactly as specified and capitalized"

    return output_file

def run_test_alternative(test_dialog_name):
    changed_file_name = create_alternative_constants_file(this_folder / "homework0.py", this_folder / "homework0-alternative.py")
    
    @ensure_missing(this_folder / 'homework0-alternative.py')
    @dialog(test_files / test_dialog_name, changed_file_name)
    def inner_function(group_name):
        ...
    group_names = inner_function._group_stats.keys()
    for group_name in group_names:
        inner_function(group_name)


@core
@dialog(test_files / "test_CORE_1_person.txt", this_folder / "homework0.py")
def test_CORE_1_person():
    ...


@core
@dialog(test_files / "test_CORE_3_person.txt", this_folder / "homework0.py")
def test_CORE_3_person():
    ...


@core
@dialog(test_files / "test_CORE_4_person.txt", this_folder / "homework0.py")
def test_CORE_4_person():
    ...


@core
@dialog(test_files / "test_CORE_7_person.txt", this_folder / "homework0.py")
def test_CORE_7_person():
    ...


@core
@dialog(test_files / "test_CORE_8_person.txt", this_folder / "homework0.py")
def test_CORE_8_person():
    ...


@core
@dialog(test_files / "test_CORE_10_person.txt", this_folder / "homework0.py")
def test_CORE_10_person():
    ...


@core
@dialog(test_files / "test_CORE_11_person.txt", this_folder / "homework0.py")
def test_CORE_11_person():
    ...


@core
@dialog(test_files / "test_CORE_12_person.txt", this_folder / "homework0.py")
def test_CORE_12_person():
    ...


@core
@dialog(test_files / "test_CORE_13_person.txt", this_folder / "homework0.py")
def test_CORE_13_person():
    ...


@core
@dialog(test_files / "test_CORE_14_person.txt", this_folder / "homework0.py")
def test_CORE_14_person():
    ...

@core
@dialog(test_files / "test_CORE_15_person.txt", this_folder / "homework0.py")
def test_CORE_15_person():
    ...

@core
@dialog(test_files / "test_CORE_16_person.txt", this_folder / "homework0.py")
def test_CORE_16_person():
    ...

@core
@dialog(test_files / "test_CORE_17_person.txt", this_folder / "homework0.py")
def test_CORE_17_person():
    ...

@core
@dialog(test_files / "test_CORE_100_person.txt", this_folder / "homework0.py")
def test_CORE_100_person():
    ...


@core
@ensure_missing(this_folder / 'homework0-alternative.py')
def test_constants_named_correctly():
    create_alternative_constants_file(this_folder / "homework0.py", this_folder / "homework0-alternative.py")


@advanced
@dialog(test_files / "test_ADVANCED_1_person.txt", this_folder / "homework0.py")
def test_ADVANCED_1_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_3_person.txt", this_folder / "homework0.py")
def test_ADVANCED_3_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_4_person.txt", this_folder / "homework0.py")
def test_ADVANCED_4_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_7_person.txt", this_folder / "homework0.py")
def test_ADVANCED_7_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_8_person.txt", this_folder / "homework0.py")
def test_ADVANCED_8_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_10_person.txt", this_folder / "homework0.py")
def test_ADVANCED_10_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_11_person.txt", this_folder / "homework0.py")
def test_ADVANCED_11_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_12_person.txt", this_folder / "homework0.py")
def test_ADVANCED_12_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_13_person.txt", this_folder / "homework0.py")
def test_ADVANCED_13_person():
    ...


@advanced
@dialog(test_files / "test_ADVANCED_14_person.txt", this_folder / "homework0.py")
def test_ADVANCED_14_person():
    ...


@advanced
def test_ADVANCED_alternative_15_person():
    run_test_alternative("test_ADVANCED_alternative_15_person.txt")

@advanced
def test_ADVANCED_alternative_16_person():
    run_test_alternative("test_ADVANCED_alternative_16_person.txt")

@advanced
def test_ADVANCED_alternative_17_person():
    run_test_alternative("test_ADVANCED_alternative_17_person.txt")


@advanced
def test_ADVANCED_alternative_100_person():
    run_test_alternative("test_ADVANCED_alternative_100_person.txt")


@excellent
@dialog(test_files / "test_EXCELLENT_1_person_35_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_1_person_35_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_3_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_3_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_4_person_35_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_4_person_35_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_7_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_7_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_8_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_8_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_10_person_35_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_10_person_35_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_11_person_10_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_11_person_10_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_12_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_12_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_13_person_80_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_13_person_80_tip():
    ...


@excellent
@dialog(test_files / "test_EXCELLENT_14_person_10_tip.txt", this_folder / "homework0.py")
def test_EXCELLENT_14_person_10_tip():
    ...


@excellent
def test_EXCELLENT_alternative_15_person_35_tip():
    run_test_alternative("test_EXCELLENT_alternative_15_person_35_tip.txt")


@excellent
def test_EXCELLENT_alternative_16_person_80_tip():
    run_test_alternative("test_EXCELLENT_alternative_16_person_80_tip.txt")


@excellent
def test_EXCELLENT_alternative_17_person_10_tip():
    run_test_alternative("test_EXCELLENT_alternative_17_person_10_tip.txt")


@excellent
def test_EXCELLENT_alternative_100_person_80_tip():
    run_test_alternative("test_EXCELLENT_alternative_100_person_80_tip.txt")

@core
@ensure_missing(this_folder / 'homework0-alternative.py')
@visibility('hidden')
def test_alternative_clean():
    ...

from RandomSentenceGenerator import RandomSentenceGenerator
from SortedSentenceGenerator import SortedSentenceGenerator
from OrderedSentenceGenerator import OrderedSentenceGenerator


def print_menu():
    print("Choose from below")
    options = [
        "rsg",
        "ssg",
        "osg",
        "input into rsg",
        "input into ssg",
        "input into osg",
    ]

    for i, option in enumerate(options):
        print(i + 1, option)
    return int(input().strip())


if __name__ == "__main__":
    rsg = RandomSentenceGenerator()
    ssg = SortedSentenceGenerator()
    osg = OrderedSentenceGenerator()
    functions = [
        rsg.show_sentence,
        ssg.show_sentence,
        osg.show_sentence,
        rsg.add,
        ssg.add,
        osg.add,
    ]
    while True:
        choice = print_menu()
        functions[choice - 1]()

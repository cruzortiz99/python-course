# from pathlib import Path
# ASSETS_FOLDER = Path(__file__).parent.parent.joinpath("assets")
from matplotlib import pyplot as pt


def main():
    pt.plot(range(-15, 16), list(map(lambda x: x**3, range(-15, 16))))
    pt.show()


if __name__ == "__main__":
    main()

import random
import collections

# import webbrowser


class Revolver:
    def __init__(self) -> None:
        self.chambers: int = 6
        self.bullet_position: int = self.insert_round()
        self.chambers_no: tuple = (1, 2, 3, 4, 5, 6)
        self.cylinder: list = list(self.chambers_no)  # Default state of the cylinder.

    def insert_round(self):
        """Ask user in which place of the cylinder to place the bullet/round."""
        while True:
            try:
                bullet_posn = input(
                    "Bullet position in the cylinder, or press enter to randomize: "
                )

                if not bullet_posn:
                    # Randomize if the user pressed enter.
                    bullet_posn = random.randint(1, self.chambers)
                else:
                    # Cast
                    bullet_posn = int(bullet_posn)

                if bullet_posn not in range(1, self.chambers + 1):
                    raise IndexError
            except ValueError:
                print("It must be an integer")
            except IndexError:
                print("The integer must be between 1 and 6")
            except KeyboardInterrupt:
                print("\nBye! But it must be a positive integer within 1 and 6")
                exit(1)
            else:
                return bullet_posn

    def roll_cylinder(self) -> tuple:
        roll_or_not = input("Roll the cylinder or not? Default y/N: ")
        if roll_or_not == "y" or roll_or_not == "Y":
            cylinder = collections.deque(self.chambers_no)
            cylinder.rotate(random.randint(1, self.chambers + 1))
            self.cylinder = list(cylinder)
            print("Rolled the cylinder\n")
            return self.cylinder

    def pull_trigger(self):
        for chamber_no in self.cylinder:
            if chamber_no == self.bullet_position:
                # webbrowser.open('https://www.youtube.com/watch?v=QslJYDX3o8s')
                print("BANG!")
            else:
                print(chamber_no)

    def print_stats(self):
        print("\nStats:")
        print("  Bullet position", self.bullet_position)
        print("  Position of the cylinder after rotating it", self.cylinder)


def main():
    russian_roulette = Revolver()
    russian_roulette.roll_cylinder()
    russian_roulette.pull_trigger()
    russian_roulette.print_stats()


if __name__ == "__main__":
    main()

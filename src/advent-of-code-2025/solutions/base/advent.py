from abc import ABC, abstractmethod
from pathlib import Path
from pprint import pprint
from typing import final
import inspect
from aocd import submit


class AoCException(Exception):
    pass


# Abstract Solution
class BaseSolution(ABC):
    _year: int
    _day: int
    _is_debugging: bool = False

    def __init__(
        cls,
        lines=False,
        csv=False,
        two_dimensional=False,
        int_csvline=False,
        block=False,
        separator=",",
        to_int=False,
    ):
        if lines:
            if to_int:
                lines = cls.read_input().splitlines()
                cls.input = [int(d) for d in lines]
            if block:
                cls.input = cls.read_input().split("\n\n")
            else:
                cls.input = cls.read_input().splitlines()
        else:
            if csv:
                lines = cls.read_input().splitlines()

                if to_int:
                    cls.input = [
                        [int(d) for d in line.split(separator)] for line in lines
                    ]
                else:
                    cls.input = [line.split(separator) for line in lines]
            else:
                if two_dimensional:
                    lines = cls.read_input().splitlines()

                    cls.input = [list(line) for line in lines]
                else:
                    if int_csvline:  # single line
                        line = cls.read_input().strip()

                        cls.input = [int(d) for d in line.split(separator)]
                    else:
                        if block:  # blocks separated by newline
                            lines = cls.read_input()
                            blocks = lines.split("\n\n")
                            arr = []
                            for i in range(len(blocks)):
                                blocks[i] = blocks[i].strip().split("\n")
                                arr.append(blocks[i])

                            cls.input = arr

                        else:  # if string:
                            if to_int:
                                cls.input = int(cls.read_input())
                            else:
                                cls.input = cls.read_input()

    @property
    def year(self):
        if not hasattr(self, "_year"):
            raise NotImplementedError("explicitly define Solution._year")
        return self._year

    @property
    def day(self):
        if not hasattr(self, "_day"):
            raise NotImplementedError("explicitly define Solution._day")
        return self._day

    @abstractmethod
    def dummy(self):  # prevent usage of BaseSolution
        pass

    @final
    def read_input(self) -> str:
        """
        handles locating, reading, and parsing input files
        """
        
        input_file = Path(
            Path(str(Path(__file__).parent.parent) + "/day" + str(self._day).zfill(2)),
            "input.txt",
        )
        if not input_file.exists():
            raise AoCException(
                f'Failed to find an input file at path "./{input_file.relative_to(Path.cwd())}". You can run `./start --year {self.year} {self.day}` to create it.'
            )

        data = input_file.read_text().strip("\n")

        if not data:
            raise AoCException(
                f'Found a file at path "./{input_file.relative_to(Path.cwd())}", but it was empty. Make sure to paste some input!'
            )
        return data

    @final
    def save(self, part, res, tm):
        answer_path = Path(
            Path(__file__).parent.parent.parent,
            f"ans{part}.txt",
        )

        if Path.exists(answer_path):
            Path.open(answer_path, "w").close()  # always overwrite

        with answer_path.open("a") as f:
            f.write(res + "\n")
            f.write(int(tm * 1000).__str__() + " msecs")

    @final
    def submit_puzzle(self, part, res):
        submit(res, part=part, day=self.day, year=self.year)

    @final
    def debug(self, *objects, trailing_newline=False):
        if not self._is_debugging:
            return

        for o in objects:
            pprint(o)

        if trailing_newline:
            print()

    def solve(self, part, res, tm, submit_to_aocd=True):
        print(f"Part {part} :: {res}")

        if self._is_debugging:
            print("********** Debug mode, skipping submission **********")
        else:
            self.save(part, str(res), tm)

            if submit_to_aocd:
                self.submit_puzzle(part="a" if part == "1" else "b", res=res)


# Concrete Solutions
class InputAsStringSolution(BaseSolution):
    def __init__(self, to_int=False):
        super().__init__(
            lines=False,
            csv=False,
            two_dimensional=False,
            int_csvline=False,
            block=False,
            separator=",",
            to_int=to_int,
        )

    def dummy(self):
        pass


class InputAsLinesSolution(BaseSolution):
    def __init__(self, to_int=False, block=False):
        super().__init__(
            lines=True,
            csv=False,
            two_dimensional=False,
            int_csvline=False,
            block=block,
            separator=",",
            to_int=to_int,
        )

    def dummy(self):
        pass


class InputAsCSVSolution(BaseSolution):
    def __init__(self, separator=",", to_int=False):
        super().__init__(
            lines=False,
            csv=True,
            two_dimensional=False,
            int_csvline=False,
            block=False,
            separator=separator,
            to_int=to_int,
        )

    def dummy(self):
        pass


class InputAsIntCSVLineSolution(BaseSolution):
    def __init__(self, separator=","):
        super().__init__(
            lines=False,
            csv=False,
            two_dimensional=False,
            int_csvline=True,
            block=False,
            separator=separator,
            to_int=False,
        )

    def dummy(self):
        pass


class InputAs2DSolution(BaseSolution):
    def __init__(self):
        super().__init__(
            lines=False,
            csv=False,
            two_dimensional=True,
            int_csvline=False,
            block=False,
            separator=",",
            to_int=False,
        )

    def dummy(self):
        pass


class InputAsBlockSolution(BaseSolution):
    def __init__(self):
        super().__init__(
            lines=False,
            csv=False,
            two_dimensional=False,
            int_csvline=False,
            block=True,
            separator=",",
            to_int=False,
        )

    def dummy(self):
        pass

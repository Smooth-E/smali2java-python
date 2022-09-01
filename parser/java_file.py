from java import literals as java_literals
import smali
from typing import List, Tuple

class Line(List[str]):
    def string(self) -> str:
        join = ' '.join(self)
        replace = join.replace('  ', ' ', -1)
        trim_space = replace.rstrip()
        no_space_after_dot = trim_space.replace('. ', ' ', -1)
        no_space_before_semicolon = no_space_after_dot.replace(' ;', ';', -1)
        return no_space_before_semicolon


class JavaFile:
    lines :List[Line]
    imports :List[str]
    extends :str
    implements : List[str]
    class_name : str
    indent :int
    smali_lines :int

    def indentate(self, line :str) -> str:
        pass

    def add_line(self, line :Line) -> None:
        self.lines.append(self.indentate(line))

    def first(self) -> Line:
        return self.lines[0]
    
    def last(self) -> Line:
        return self.lines[len(self.lines) - 1]
    
    def last_class_declaration(self) -> Tuple[Line, int]:
        for i in range(len(self.lines) - 1, -1, -1):
            line = self.lines[i]
            for word in line:
                if word == java_literals._class:
                    return line, i
        return None, -1


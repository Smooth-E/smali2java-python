import os
import typing
import java_literals
import java_types
import smali_literals
from typing import List, Tuple

def get_class_name(jvm_name :str) -> str:
    split_jvm_name = jvm_name.split('/')
    class_name = split_jvm_name[len(split_jvm_name) - 1]
    if len(class_name) == 1:
        if class_name == 'I': return java_types.integer
        elif class_name == 'Z': return java_types.boolean
        elif class_name == 'J': return java_types.long
        elif class_name == 'F': return java_types.float
        elif class_name == 'D': return java_types.double
        elif class_name == 'V': return java_types.void
        else: return java_types.object
    else:
        # if starts with array, drop it
        if split_jvm_name[0][0] == '[':
            split_jvm_name[0] = split_jvm_name[0][1:]
        joined_name = '.'.join(split_jvm_name)
        # if ends with semicolon, drop it
        if joined_name[len(joined_name) - 1] == ';':
            joined_name = joined_name[:len(joined_name) - 1]
        if joined_name[0] == 'L':
            joined_name = joined_name[1:]
        return joined_name

def get_method_name(method_and_type: str) -> str:
    type_index = method_and_type.index(':')
    return method_and_type[:type_index]

class Line(List[str]):
    def string(self) -> str:
        join = ' '.join(self)
        replace = join.replace('  ', ' ', -1)
        trim_space = replace.rstrip()
        no_space_after_dot = trim_space.replace('. ', ' ', -1)
        no_space_before_semicolon = no_space_after_dot.replace(' ;', ';', -1)
        return no_space_before_semicolon

class JavaFile:
    def __init__(self) -> None:
        self.lines       :list[Line] = []
        self.imports     :List[str]  = []
        self.extends     :str        = ''
        self.implements  : List[str] = []
        self.class_name  : str       = ''
        self.indent      :int        = 0
        self.smali_lines :int        = 0

    def indentate(self, line :str) -> str:
        if self.indent < 1: return line
        line = '\t' * self.indent + line
        return line

    def add_line(self, line :list[str]) -> None:
        converted_line = Line()
        for word in line: converted_line.append(word)
        self.lines.append(self.indentate(converted_line))

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

    def replace_last(self, line :Line) -> None:
        self.lines[len(self.lines) - 1] = self.indentate(line)
    
    def replace(self, index :int, line :Line) -> None:
        self.lines[index] = line
    
    def print(self) -> None:
        for line in self.lines: print(line)
    
    def save(self, directory :str) -> None:
        class_name_parts = self.class_name.split('.')
        class_name = class_name_parts[len(class_name_parts) - 1]
        with open(os.path.join(directory, class_name + '.java'), 'w+') as file:
            file.writelines(self.lines)
    
    def parse_line(self, line :str) -> typing.Any:
        split_line = line.split()
        self.smali_lines += 1
        if len(split_line) != 0:
            opcode = split_line[0]
            if opcode == smali_literals._class:
                pass

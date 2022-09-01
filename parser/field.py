from pydoc import classname
import java_file
from java_file import JavaFile
from java_file import Line
import java_modifiers
import java_literals
import smali_literals

class FieldParser:
    def __init__(self) -> None:
        self.accessor = ''
        self.static = False
        self.synthetic = False
        self.final = False
        self.volatile = False
        self.transient = False
    
    def parse(self, file :JavaFile, current_line :Line) -> None:
        member_and_class_index = 1
        member_and_class :list[str] = []
        # Read the accessor (public/private/protected) if present
        if java_modifiers.modifiers.get(current_line[member_and_class_index]):
            self.accessor = current_line[member_and_class_index]
            member_and_class_index += 1
        if member_and_class_index >= len(current_line):
            print(current_line)
        if current_line[member_and_class_index] == java_literals.static:
            self.static = True
            member_and_class_index += 1
        if current_line[member_and_class_index] == smali_literals.final:
            self.final = True
            member_and_class_index += 1
        if current_line[member_and_class_index] == smali_literals.volatile:
            self.volatile = True
            member_and_class_index += 1
        # For java enum fields is just another class
        if current_line[member_and_class_index] == smali_literals.enum:
            member_and_class_index += 1
        if current_line[member_and_class_index] == smali_literals.synthetic:
            self.synthetic = True
            member_and_class_index += 1
        if current_line[member_and_class_index] == smali_literals.transient:
            self.transient = True
            member_and_class_index += 1
        member_and_class = current_line[member_and_class_index].split(':')
        if len(member_and_class) < 2: print(current_line)
        class_name = java_file.get_class_name(member_and_class[1])
        member_name = member_and_class[0]
        line :list[str] = []
        if self.accessor != '': line.append(self.accessor)
        if self.static: line.append(java_literals.static)
        if self.final: line.append(java_modifiers.final)
        if self.volatile: line.append(java_modifiers.volatile)
        if self.transient: line.append(java_modifiers.transient)
        line.append(class_name)
        line.append(member_name)
        line.append(';')
        if self.synthetic: line.append('//synthetic')
        file.add_line(line)

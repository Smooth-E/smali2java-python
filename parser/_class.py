import java_file
from java_file import JavaFile
from java_file import Line
import java_modifiers
import java_literals
import typing
from typing import List

class ClassParser:
    def parse(self, file :JavaFile, current_line :Line) -> typing.Any:
        accessor = ''
        class_name_index = 1
        if java_modifiers.modifiers.get(current_line[class_name_index]):
            accessor = current_line[class_name_index]
            class_name_index += 1
        interface_or_abstract = ''
        if  current_line[class_name_index] == java_literals.interface:
            interface_or_abstract = java_literals.interface
            class_name_index += 1
        # Note: 'interface abstract' is a valid declaration
        if current_line[class_name_index] == java_literals.abstract:
            interface_or_abstract = java_literals.abstract
            class_name_index += 1
        name = java_file.get_class_name(current_line[class_name_index])
        line :List[str] = []
        if accessor != '': line.append(accessor)
        if interface_or_abstract != '': line.append(interface_or_abstract)
        line.append(java_literals._class)
        line.append(name)
        line.append('{')
        file.add_line(line)
        file.class_name = name

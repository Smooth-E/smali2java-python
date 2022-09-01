from field import FieldParser
from java_file import JavaFile
import java_file

def test(input :str, expected_output :str) -> None:
    file = JavaFile()
    FieldParser().parse(file, input.split())
    print(file.first().string())
    print(expected_output)
    print(file.first().string() == expected_output)
    print()

if __name__ == '__main__':
    test('.field public static id:I', \
        'public static Integer id;')
    test('.field public volatile id:I', \
        'public volatile Integer id;')
    test('.field final synthetic a:Lcom/lifx/app/MainActivity;', \
        'final com.lifx.app.MainActivity a; //synthetic')
    test('.field public static final a:Lcom/lifx/app/DiagnosticsActivity$Companion$queryWANState$2$1;', \
        'public static final com.lifx.app.DiagnosticsActivity$Companion$queryWANState$2$1 a;')
    test('.field a:Lcom/lifx/app/controller/ControlTab;', \
        'com.lifx.app.controller.ControlTab a;')
    test('.field public static final enum a:Lcom/lifx/app/controller/ControlTab;', \
        'public static final com.lifx.app.controller.ControlTab a;')

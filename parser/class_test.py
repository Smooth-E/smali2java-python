from _class import ClassParser
from java_file import JavaFile
import java_file

def test_class(input :str, expected_output :str) -> None:
    parser = ClassParser()
    file = JavaFile()
    parser.parse(file, java_file.line_from_list(input.split()))
    print(expected_output == file.first().string())

def main() -> None:
    test_class('.class Lcom/example/app/MainActivity$4', \
        'class com.example.app.MainActivity$4 {' )
    test_class('.class public Lcom/example/app/MainActivity$4', \
        'public class com.example.app.MainActivity$4 {' )
    test_class('.class public interface abstract Lcom/example/app/MainActivity$4', \
        'public abstract class com.example.app.MainActivity$4 {' )

if __name__ == '__main__':
    main()

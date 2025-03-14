import caesarSagte;
import io;
import pytest;

def test_hello(capsys):
    caesarSagte.main() 
    captured = capsys.readouterr()
    expected_output = 'Caesar sagte: "Veni, vidi, vici."'
    expected_output = expected_output.replace('\r\n', '\n').strip()
    output = '\n'.join(line.strip() for line in captured.out.splitlines()).replace('\r\n', '\n').strip()

    assert  output == expected_output
 

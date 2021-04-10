from click.testing import CliRunner
from What.what import main
import re


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(main, ["1981328391THM{this is a flag}asdasda"])
    assert result.exit_code == 0
    assert "THM{" in result.output


def test_file_fixture():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("web", str(result.output))
    assert re.findall("thm", str(result.output))
    assert re.findall("Ethereum", str(result.output))
    assert "Dogecoin" in result.output


def test_file_fixture2():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("web", str(result.output))
    assert "Dogecoin" in result.output


def test_file_fixture3():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("thm", str(result.output))


def test_file_fixture4():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("Ethereum", str(result.output))


def test_file_fixture5():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("thm{", str(result.output))


def test_file_fixture7():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall('thm{"', str(result.output))


def test_file_fixture8():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("URL", str(result.output))


def test_file_fixture9():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("etherscan", str(result.output))


def test_file_fixture10():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("dogechain", str(result.output))


def test_file_fixture11():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("Dogecoin", str(result.output))


def test_file_fixture12():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("blockchain", str(result.output))


def test_file_fixture13():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("Bitcoin", str(result.output))


def test_arg_parsing():
    runner = CliRunner()
    result = runner.invoke(main, ["1KFHE7w8BhaENAswwryaoccDb6qcT6DbYY"])
    assert result.exit_code == 0
    assert re.findall("blockchain", str(result.output))


def test_arg_parsing2():
    runner = CliRunner()
    result = runner.invoke(main, ["http://10.1.1.1"])
    assert result.exit_code == 0
    assert re.findall("URL", str(result.output))


def test_file_fixture_visa():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("Visa", str(result.output))


def test_file_fixture_master_card():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("MasterCard", str(result.output))


def test_file_fixture_master_amex():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("American Express", str(result.output))


def test_file_fixture_master_diners():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("Diners Club Card", str(result.output))


def test_file_fixture_discover():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("Discover", str(result.output))

def test_file_fixture_usernamepassword():
    runner = CliRunner()
    result = runner.invoke(main, ["fixtures/file"])
    assert result.exit_code == 0
    assert re.findall("Username", str(result.output))
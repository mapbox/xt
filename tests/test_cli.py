from click.testing import CliRunner

from xt.scripts.cli import cli


def test_cli_parse():
    runner = CliRunner()
    result = runner.invoke(cli, [], input='[10, 100, 1000]')
    assert result.output == '1000/10/100\n'
    assert result.exit_code == 0


def test_cli_parse_dash_out():
    runner = CliRunner()
    result = runner.invoke(cli, ['-d', '-'], input='[10, 100, 1000]')
    assert result.output == '1000-10-100\n'
    assert result.exit_code == 0


def test_cli_parse_dash():
    runner = CliRunner()
    result = runner.invoke(cli, [], input='10-100-1000')
    assert result.output == '[100, 1000, 10]\n'
    assert result.exit_code == 0


def test_cli_parse_slash():
    runner = CliRunner()
    result = runner.invoke(cli, [], input='10/100/1000')
    assert result.output == '[100, 1000, 10]\n'
    assert result.exit_code == 0


def test_cli_parse_slash_more():
    runner = CliRunner()
    result = runner.invoke(cli, [], input='hi hi 10/100/1000')
    assert result.output == '[100, 1000, 10]\n'
    assert result.exit_code == 0


def test_cli_parse_slash_lines():
    runner = CliRunner()
    result = runner.invoke(cli, [], input='10/100/1000\n20/200/2000')
    # print(result.output)
    assert result.output == '[100, 1000, 10]\n[200, 2000, 20]\n'
    assert result.exit_code == 0

"""
Parse Tiles Both Ways
"""
import click
import xt


@click.command("xt")
@click.argument("inputtiles", default="-", required=False)
@click.option("--delimiter", "-d", type=str, default="/")
def cli(inputtiles, delimiter):
    """
    Automatically onvert a stream of tiles to another format\n
    \tz/x/y | z-x-y ==> [x, y, z]\n
    \t[x, y, z] ==> z/x/y | z-x-y | z?x?y -d ?\n


    NOTES
    ------
    Will always match the last pattern, eg:
        10-10-10 hi hi 20/20/20.png
    will return [20, 20, 20]
    """
    try:
        inputtiles = click.open_file(inputtiles).readlines()
    except IOError:
        inputtiles = [inputtiles]

    for x in xt.xvert(inputtiles, delimiter):
        click.echo(x)

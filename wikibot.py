from mylib.bot import scrape
import click


@click.command()
@click.option(
    "--name", prompt="Wkipedia page to scrape", help="Web page we want to scrape"
)
@click.option("--length", help="lenght of the output from wikipedia")
def cli(name, length):
    result = scrape(name, length)
    click.echo(click.style(f"{result}:", bg="black", fg="blue"))


if __name__ == "__main__":
    cli()

"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """\Sdf."""


if __name__ == "__main__":
    main(prog_name="\sdf")  # pragma: no cover

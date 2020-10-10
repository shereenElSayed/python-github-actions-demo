#!/usr/bin/python3
import click
from src import calculations as calc


@click.command()
@click.option('--name', prompt='Enter your name',
              help='The person to greet.')
def welcome(name):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo(f'Hello {name}')


@click.command()
@click.argument('vals', type=int, nargs=-1, required=True)
@click.option('--operation', '-o', required=True,
              type=click.Choice(['sum', 'multiply']))
def calculate(vals, operation):
    "Calculate the sum or the multiplication of numbers"

    if operation == "sum":
        result = calc.summation(vals)
    elif operation == "multiply":
        result = calc.multiply(vals)

    calc.print_result(operation, result)


@click.group()
def main():
    pass


main.add_command(calculate)
main.add_command(welcome)

if __name__ == '__main__':
    main()

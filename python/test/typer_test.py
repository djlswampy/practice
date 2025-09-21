import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """이름을 입력 받아 인사를 출력합니다."""
    typer.echo(f"Hello {name}!")


@app.command()
def bye(name: str):
    """이름을 입력 받아 인사를 출력합니다."""
    typer.echo(f"bye {name}!")

if __name__ == "__main__":
    app()
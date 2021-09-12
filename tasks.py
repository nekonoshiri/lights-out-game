import invoke


@invoke.task
def lint(c):
    """ソースコードのフォーマット及び静的解析を行います。"""
    c.run("isort lights_out_game test")
    c.run("black lights_out_game test")
    c.run("flake8 lights_out_game test")
    c.run("mypy lights_out_game test")


@invoke.task
def test(c):
    """全てのユニットテストを実行します。"""
    c.run("pytest test")

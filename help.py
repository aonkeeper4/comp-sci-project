class _console:
    def __init__(self):
        self.log = print


console = _console()


class Javascript:
    def __init__(this, a, b):
        this.a = a
        this.b = b

    def print_vals(this):
        console.log(this.a, this.b)


js = Javascript(1, "two")
js.print_vals()

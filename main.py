import sys


class REPL(object):

    def __init__(self, reader, evaluator, printer):
        self.reader = reader
        self.evaluator = evaluator
        self.printer = printer

    def mainloop(self):
        while True:
            self.printer.print_out(self.evaluator.eval(self.reader.read()))


class Reader(object):

    def __init__(self):
        self.bye = 'bye'

    def read(self, prompt='repl > '):
        try:
            s = raw_input(prompt)
        except KeyboardInterrupt:
            self.exit()
        return s

    def exit(self):
        sys.stdout.write('%s\n' % self.bye)
        sys.exit()


class Evaluator(object):

    def __init__(self, tokenizer, parser):
        self.tokenizer = tokenizer
        self.parser = parser

    def eval(self, s):
        tokens = self.parse(self.tokenize(s))
        return 'eval'

    def tokenize(self, s):
        return self.tokenizer.tokenize(s)

    def parse(self, tokens):
        return self.parser.parse(tokens)


class Tokenizer(object):

    def tokenize(self, codes):
        tokens = codes
        #token = (typeid, type, value, line)
        return tokens


class Parser(object):

    def parse(self, tokens):
        return tokens


class Printer(object):

    def print_out(self, s):
        sys.stdout.write('%s\n' % s)

if __name__ == '__main__':
    repl = REPL(Reader(), Evaluator(Tokenizer(), Parser()), Printer())
    repl.mainloop()

import sys


class REPL(object):

    def __init__(self, reader, evaluator, printer):
        self.reader = reader
        self.evaluator = evaluator
        self.printer = printer

    def mainloop(self):
        while True:
            self.printer.printOut(self.evaluator.eval(self.reader.read()))


class Reader(object):

    def __init__(self):
        self.bye = 'bye'
        self.prompt = 'repl> '

    def read(self, prompt=None):
        prompt = prompt if prompt else self.prompt
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
        return tokens

    def tokenize(self, s):
        return self.tokenizer.tokenize(s)

    def parse(self, tokens):
        return self.parser.parse(tokens)


class Tokenizer(object):

    YES = 1 #'y'
    NO = 2  #'n'
    NUMBER = 3

    def tokenize(self, s):
        src = s.strip().split()
        tokens = []
        while len(src):
            t = src.pop(0)
            if t.isdigit():
                tokens.append((Tokenizer.NUMBER, int(t)))
            elif t == 'y':
                tokens.append((Tokenizer.YES, t))
            elif t == 'n':
                tokens.append((Tokenizer.NO, t))
            else:
                pass
        return tokens


class Parser(object):

    def parse(self, tokens):
        if len(tokens) == 0:
            pass
        return tokens


class Printer(object):

    def printOut(self, s):
        sys.stdout.write('%s\n' % s)
        pass

if __name__ == '__main__':
    repl = REPL(Reader(), Evaluator(Tokenizer(), Parser()), Printer())
    repl.mainloop()

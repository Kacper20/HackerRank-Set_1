import re
for _ in range (input()):
    str = raw_input()
    match = re.match(r'^(\d+)\s(?:C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC){1,1}$', str)
    if  match:
        id = int(match.group(1))
        if id >= 10 ** 4 and id < 10** 5:
            print 'VALID'
        else:
            print 'INVALID'
    else:
        print 'INVALID'
    
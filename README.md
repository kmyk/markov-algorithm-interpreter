# Markov Algorithm Interpreter

for Markov Algorithm Online: <https://mao.snuke.org/>

## How to install

``` console
$ pip3 install git+https://github.com/kmyk/markov-algorithm-interpreter
```

Also, you can just download `markov_algorithm.py` and use it directly.

## Usage

``` console
$ echo INPUT | markov FILE
```

For example,

``` console
$ cat append-s.txt
#!/usr/bin/env markov
sb:bs
s::
:s

$ echo bb | markov append-s.txt
ops = [('sb', False, 'bs'), ('s', True, ''), ('', False, 's')]
0: bb
1: sbb
2: bsb
3: bbs
3: bb
bb
```

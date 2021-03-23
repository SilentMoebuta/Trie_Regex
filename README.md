# trie_regex
Speed up regex searching by trans regex pattern to trie form.
Code from stackoverflow [Speed up millions of regex replacements in Python 3](https://stackoverflow.com/questions/42742810/speed-up-millions-of-regex-replacements-in-python-3)

# 简介
利用前缀树形式的正则pattern来加速匹配。虽比不上AC算法效率，但胜在方便，遂取随用。

# benchmark test
Serch some most common words in a wiki page.
```
         1004 function calls in 1.398 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    1.398    1.398 <string>:1(<module>)
        1    0.002    0.002    1.398    1.398 bench.py:20(normal_reg_search)
        1    0.000    0.000    1.398    1.398 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1000    1.396    0.001    1.396    0.001 {method 'findall' of 're.Pattern' objects}


         1004 function calls in 0.363 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.363    0.363 <string>:1(<module>)
        1    0.001    0.001    0.363    0.363 bench.py:25(trie_reg_search)
        1    0.000    0.000    0.363    0.363 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1000    0.362    0.000    0.362    0.000 {method 'findall' of 're.Pattern' objects}

```

# usage
```
import re
from triereg import *

words = ["abc", "acd", "adc"]
pattern = trie_regex_from_words(words)
```

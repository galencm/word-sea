# Word Sea

_visual word count_

## Installation

using pip:

```
pip3 install git+https://github.com/galencm/word-sea --user
```

Clone / download
```
git clone https://github.com/galencm/word-sea
```

## Examples
Examples use text of _A chronology of paper and paper-making_ by Joel Munsell, published in 1857, available from [https://archive.org/details/chronologyofpape01muns](https://archive.org/details/chronologyofpape01muns)

To get the text used:
```
wget https://archive.org/stream/chronologyofpape01muns/chronologyofpape01muns_djvu.txt
```

Run `ws` without any arguments:
```
ws chronologyofpape01muns_djvu.txt  | less -R
```

Show only the key for word counts >= 10 and word length >= 10
```
 ws chronologyofpape01muns_djvu.txt --count-threshold 10 --length-threshold 10 --key-only | less -R
```

Page through the beiged-out text:
```
 ws chronologyofpape01muns_djvu.txt --count-threshold 10 --length-threshold 10 | less -R
```

Run directly:
```
python3 visual_word_count.py
```

## Contributing
This project uses the C4 process

[https://rfc.zeromq.org/spec:42/C4/](https://rfc.zeromq.org/spec:42/C4/
)

## License
Mozilla Public License, v. 2.0

[http://mozilla.org/MPL/2.0/](http://mozilla.org/MPL/2.0/)
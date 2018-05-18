# Word Sea

_visual word count_

## Installation

using pip:

```
pip3 install https://github.com/galencm/word-sea --user
```

Clone / download
```
git clone https://github.com/galencm/word-sea
```

## Examples
Examples using text from _The history of silk, cotton, linen, wool, and other fibrous substances_ from [https://archive.org/details/historyofsilkcot01gilr](https://archive.org/details/historyofsilkcot01gilr)

```
wget https://archive.org/stream/historyofsilkcot01gilr/historyofsilkcot01gilr_djvu.txt
```

Run without any arguments:
```
ws historyofsilkcot01gilr_djvu.txt  | less -R
```

Show only the key for word counts >= 10 and word length >= 10
```
 ws historyofsilkcot01gilr_djvu.txt --count-threshold 10 --length-threshold 10 --key-only | less -R
```

Page through the beiged-out text:
```
 ws historyofsilkcot01gilr_djvu.txt --count-threshold 10 --length-threshold 10 | less -R
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
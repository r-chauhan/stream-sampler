# Introduction
Repository for stream sampler for implementing sampling technique to get a fixed-sized sample from a dataset with unknown size, using [fast reservior sampling techinque](https://erikerlandson.github.io/blog/2015/11/20/very-fast-reservoir-sampling/).


## Dependencies
- Python 3.7.4
- Unix/Linux 
- Pytest

## Execution instructions
Executing tests:
```bash
pytest tests
```
Executing from within Python on a sample string `"THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"`:
```bash
python3 run.py
```
Executing stream-sampler for values piped from a file:
```bash
cat line_letters.txt | ./stream-sampler.py 5
```

## Assumptions
- Environment path is assumed to be `/usr/local/bin/python3`.
- Encoding is set to `UTF-8`.
- Files are assumed to have strings seperated by line-break.
- Character/word spaces in the same line aren't trimmed or ignored.


## References
- [alexprengere/reservoir](https://github.com/alexprengere/reservoir)
- [erikerlandson blog](https://erikerlandson.github.io/blog/2015/11/20/very-fast-reservoir-sampling/)

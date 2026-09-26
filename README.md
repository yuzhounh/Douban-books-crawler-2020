# Douban Books Crawler 2020

[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-D4A017.svg)](LICENSE)

Historical Python and MATLAB workflow for collecting Douban book information from doulists and tags.

Copyright (C) 2020 Jing Wang  

## Historical workflow

Run the stages from the repository root:

1. Review [Notes](Notes) (Douban note IDs used to discover doulists) and [Tags_raw](Tags_raw) (raw tag input).
2. Run `python main.py` to prepare the source lists and collect book information. This stage generates inputs such as `Doulists_ID` and `Tags_unique` and writes the collected results.
3. Open MATLAB in the repository directory and run `main` to import, sort, and organize the collected results using [main.m](main.m).

Published results: [Douban-books-2020](https://github.com/yuzhounh/Douban-books-2020).

These historical scripts document the original workflow. Compatibility with current Douban pages has not been verified; the newer implementation is linked below.

## Original environment

- Python 3.7.
- MATLAB R2018a.

These versions document the original environment, rather than a current compatibility guarantee.

## Related projects

- [Douban-books-2020](https://github.com/yuzhounh/Douban-books-2020): Historical 2020 results distributed as UTF-8 BOM CSV files.
- [douban-books-ranking](https://github.com/yuzhounh/douban-books-ranking): Newer standalone Python implementation with an online ranking and published JSON data.

## License

See [LICENSE](LICENSE) for the GNU General Public License v3.0.

## Contact

Jing Wang  
wangjing@xynu.edu.cn  
yuzhounh@163.com  
2020-7-5 18:25:16

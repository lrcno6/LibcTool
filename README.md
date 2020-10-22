# LibcTool

A class to use *LibcSearcher* more conveniently

license: *LGPL-2.1*

*GitHub* address: https://github.com/lrcno6/LibcTool

## Introduction

A class tool to calculate the address automatically when using [*LibcSearcher*](https://github.com/lieanu/LibcSearcher)

## Installation

<!-- For Chinese users, you can use the *Gitee* image to accelerate -->

<!-- 对于中国用户，可以使用*Gitee*镜像来加速下载 -->

Before installing *LibcTool*, you should install [*LibcSearcher*](https://github.com/lieanu/LibcSearcher) first ([*Gitee* image](https://gitee.com/north_walker/LibcSearcher) for Chinese users)

And then install *LibcTool*:

```sh
git clone https://github.com/lrcno6/LibcTool.git
cd LibcTool
python setup.py develop
```

## Example

Almost the same as *LibcSearcher*:

```py
from LibcTool import *

# The 2nd param should be the actual address of the function
libc=LibcTool("fgets",0x7ff39014bd90)

libc.dump("system")     # The actual address of system
libc.dump("str_bin_sh") # The actual address of the string "/bin/sh"
libc.dump("__libc_start_main_ret")
```

---

Welcome to contribute to [*LibcTool*](https://github.com/lrcno6/LibcTool), and also [*LibcSearcher*](https://github.com/lieanu/LibcSearcher) and [*libc-database*](https://github.com/niklasb/libc-database)!

By [*lrcno6*](https://github.com/lrcno6)
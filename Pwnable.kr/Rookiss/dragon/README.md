## 思路解析
首次调用 FightDragon 必定遇到 babe dragon -> 打不过, 用 Knight 一键自杀(按下 2) -> 第二次调用 FightDragon 肯定遇到 mama dragon -> 听说你血多 -> 用 Priest 一直 holyshield 防御, 并让其回血(按两次 3 进行防御, MP 归零后用 2 进行补充, 这样一轮可以给龙妈奶 12 点血, 因为她初始值为 80, 因此至少需要 4 轮, 这里你会发现牧师的初始血量刚好是 42 点, 嗯... 提示来的), 直到超过 byte 的最大正值 (128) -> 龙死了, 进入留名(实际是一个 UAF 漏洞), 填写 system 所在地址 0x08048DBF -> get shell! 

## Writeup
见 exploit.py 文件

**如果你有任何疑问, 欢迎到我的 [blog](https://www.qmsharing.space/2018/12/04/pwnablekr-dragon/) 中进行留言讨论 : )**


```sh
./build/mmap

100MBのメモリ割当に成功している
*** succeeded to allocate memory: address = 0x7f935dfa2000; size = 0x6400000 ***
*** memory map after memory allocation ***
7f935dfa2000-7f93643a2000 rw-p 00000000 00:00 0
```

```sh
python -c "print(0x7f93643a2000 - 0x7f935dfa20
00)"
104857600
```

 
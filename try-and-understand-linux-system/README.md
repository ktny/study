# 試して理解 Linuxの仕組み

## straceでシステムコール呼び出しの様子を確認する

```sh
cc -o ./build/hello hello.c
strace -o hello.log ./build/hello
cat ./hello.log
```

```sh
strace -o hello.py.log python hello.py
cat ./hello.py.log
```

putsは最終的にはwriteシステムコールによって実現されている。
cでもpythonでも同様。ただし、pythonの方がプログラム起動に呼び出すシステムコールが多い。

## CPU使用率を確認する

```sh
cc -o ./build/loop loop.c
./loop &

# %userのCPU使用率が上がっている
sar -P ALL 1 1
```

```sh
cc -o ./build/ppidloop ppidloop.c
./ppidloop &

# %systemのCPU使用率が上がっている
sar -P ALL 1 1
```

%systemが数十%のような大きな値になっているときはシステムコールを発行しすぎていたり、システム負荷が高すぎる状態であることが多い。

tail -f /dev/ttyusb0 | tee -a foo.txt
strace tail -f /dev/ttyusb0
strace screen /dev/ttyusb0
ps aux | grep screen
strace -p 8185
sudo ls -lh /proc/8185/fds
tail -f /dev/pts/0
strace cat /dev/ttyusb0

openat(AT_FDCWD, "/dev/ttyUSB0", O_RDONLY) = -1 EBUSY (Device or resource busy)


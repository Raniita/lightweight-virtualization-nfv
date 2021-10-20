## https://www.nginx.com/blog/what-are-namespaces-cgroups-how-do-they-work/
## https://wiki.archlinux.org/title/cgroups#With_the_cgroup_virtual_filesystem
## https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_monitoring_and_updating_the_kernel/setting-limits-for-applications_managing-monitoring-and-updating-the-kernel

# Create cgroup (v1)
mkdir -p /sys/fs/cgroup/memory/<name>
echo 50000000 > /sys/fs/cgroup/memory/<name>/memory.limit_in_bytes		# 50 MB

# Create a shell script that go in loop [test.sh] {PID 2428}
./test.sh & 					# Usando el & nos da el PID
echo <PID test.sh> > /sys/fs/cgroup/memory/<name>/cgroup.procs

# Check cgroup <name>
ps -o cgroup <PID test.sh> 

# Default: System terminates process when it exceeds resource limited


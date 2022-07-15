[Running docker containers in proxmox containers | Proxmox Support Forum](https://forum.proxmox.com/threads/running-docker-containers-in-proxmox-containers.81660/)

> For anybody coming here later and seeing this, if the container is unprivileged just goto Options from the container menu (main UI), click on Features then select keyctl and nesting, save, voila!



```
docker: Error response from daemon: OCI runtime create failed: container_linux.go:349: starting container process caused "process_linux.go:449: container init caused \"rootfs_linux.go:58: mounting \\\"proc\\\" to rootfs \\\"/var/lib/docker/overlay2/f9b1c95f723519652c87162a208e7fcb8817d68e13f9e082fbeaf8370e6b79c9/merged\\\" at \\\"/proc\\\" caused \\\"permission denied\\\"\"": unknown.
```
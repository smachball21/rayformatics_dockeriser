# PACKAGES USAGES

## ***Manage users*** :

### --- docker_adduser.py:
`This script add user in localDB, send email & start container`

___Usage:___
```
-u   {USERNAME} = Specify the sftp username
-em  {EMAIL}    = Specify email of client for send credentials
-i   {IMAGE}    = OPTIONNAL - Specify image name (default: secureftp)
-vol {VOLUME}   = OPTIONNAL - Specify volname (default: {username})
-p   {PORT}     = OPTIONNAL - Specify port number (default: incremential with other containers)

Example:
python docker_adduser.py -u example -em example@example.com -i image -vol volume -p 2955

```

### --- docker_removeuser.py :
`This script remove user in localDB, kill, remove, container & volume`

___Usage:___
```
python docker_removeuser.py {USERNAME}
```

## ***Manage users*** :

### --- reinstall:
`This file recreate all volumes, images & restart all container with localDB`

___Usage:___
```
bash {FOLDER}/reinstall
```

### --- volumes_create :
`This script create volume and set permissions to folder`

___Usage:___
```
bash volume_create {volname}
```

### --- volumes_remove :
`This script remove volume`

___Usage:___
```
bash volume_remove {volname}
```

### --- chroot_config :
`This script configure chroot in specific container`

___Usage:___
```
bash chroot_config {container_name}
```

### --- docker_start.py :
`This script start all container in localDB`

___Usage:___
```
-u {USERNAME} = OPTIONNAL - Specify one container to start (default: all containers start)

Example:

- Start all containers :
python docker_start.py

- Start specific container :
python docker_start.py -u {USERNAME}

```

### --- docker_kill
`This script kill all container in localDB`

___Usage:___
```

- Kill all containers :
python docker_kill

- Start specific container :
python docker_kill {USERNAME}

```


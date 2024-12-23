# CONTAINERAZATION

what is the cloud native ?

 - applications are designed to be dynamic, scalable, and resilient taking advantage of cloud infrastructure services, APIs.
 - key characeteristic for Cloud Native : Microservis, Containers, Dynamic Orchestration, Devops and CI/CD API-Driven, Resilience and 
   elasticity, 

WHAT IS THE PROBLEM WITH VIRTUAL MACHINES? 

 - Seperated virtual machines cannot use of all of thier capacity , also they can need more capacity this could be heavy lost 
   for organizations. Containeraziton can solve this problem.
 - they will effectively use virtual machines capacity.

WHAT IS THE MAKE CONTAINERS GOOD ?

 - The containers are very lightweight in nature, they dont have complete operating system, they use resource from base operating system.
 - Container has base image, container is package or bundle which is combination of your application libraries that means your application dependencies plus system dependencies.

 FILES AND FOLDER THAT BASE IMAGES INCLUDES

    /bin: contains binary executable files, such as the ls, cp, and ps commands.

    /sbin: contains system binary executable files, such as the init and shutdown commands.

    /etc: contains configuration files for various system services.

    /lib: contains library files that are used by the binary executables.

    /usr: contains user-related files and utilities, such as applications, libraries, and documentation.

    /var: contains variable data, such as log files, spool files, and temporary files.

    /root: is the home directory of the root user


FILES AND FOLDERS THAT CONTAINERS USE FROM HOST OPERATING SYSTEM

    The host's file system: Docker containers can access the host file system using bind mounts, which allow the container to read and write files in the host file system.

    Networking stack: The host's networking stack is used to provide network connectivity to the container. Docker containers can be connected to the host's network directly or through a virtual network.

    System calls: The host's kernel handles system calls from the container, which is how the container accesses the host's resources, such as CPU, memory, and I/O.

    Namespaces: Docker containers use Linux namespaces to create isolated environments for the container's processes. Namespaces provide isolation for resources such as the file system, process ID, and network.

    Control groups (cgroups): Docker containers use cgroups to limit and control the amount of resources, such as CPU, memory, and I/O, that a container can access.


What is Docker ?

Docker is a containerization platform that provides easy way to containerize your applications, which means, using Docker you can build container images, run the images to create containers and also push these containers to container regestries such as DockerHub, Quay.io and so on.
Important thing Docker solves is the complexity so it is reduces our workflow a lot of instead of user doing manual 100 actions one person writes a Dockerfile, it can contain application, it can contain your testing platform it can contain anything so anybody who executes this Docker image everthing is created out of the box that means your Docker container is also helping you in efficiency.

Docker daemon
The Docker daemon (dockerd) listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. A daemon can also communicate with other daemons to manage Docker services. Hearth of the docker, if docker daemon down containers will be down.

Dockerfile
Dockerfile is a file where you provide the steps to build your Docker Image.
FROM: Must begin with FROM instruction, that specifies the parent image from which you are building.
RUN : Runs commands specified as an image build state,
WORKDIR : Sets the working directory for any RUN, CMD, ENTRYPOINT, COPY and ADD instructions that follow in the Dockerfile if the WORKDIR doesnt exist it will be created.
COPY : Copies files or directories from the host machine to the container.
ADD : Similar to COPY, but also supports : Downloading files from a URL, Extracting compressed files automatically.
CMD : Specifies the default command that runs when a container starts. 
ENTRYPOINT : Similar to CMD but allows passing additional arguments when running a container. 
ENV: Sets environment variables inside the container.
EXPOSE : Informs Docker that the container will listen on the specified port.
VOLUME : Creates a mount point to persist data outside the container.
LABEL : Adds metadata to the image
ARG :  Defines build-time variables.
HEALTHCHECK : Checks if the container is healthy.

WHAT IS THE DIFFERENCE BETWEEN ENTRYPOINT AND CMD

  - Both ENTRYPOINT and CMD can be used to execute as your start command or you know they can whenever somebody runs Docker run both ENTRYPOINT and ACM can serve as your starting command but the the only difference is ENTRYPOINT is something that you cannot change, CMD is something that is configurable 


WHAT IF OUR IMAGES SIZE IS TOO BIG ?

  We can use multistage builds. We install as part of the stages these are only require to build your application. So these are two stages build is different running your application is required. There are countless stages ı can add. Also We can use DISTROYLESS IMAGE for having more small size images. 

  DISTROYLESS IMAGES : is basically minimalistic image that will have only the runtime environments, biggest advantages of this is security, other than reducing your container image size you will have highest security with distroyless images.


  WHAT IS THE MAJOR PROBLEM WITH THE CONTAINERS ?
  
   It is a very common requirement to persist the data in a Docker container beyond the lifetime of the container. However, the file system of a Docker container is deleted/removed when the container dies.

   Volumes
   Volumes aims to solve the same problem by providing a way to store data on the host file system, separate from the container's file system, so that the data can persist even if the container is deleted and recreated.

   Volumes can be created and managed using the docker volume command. You can create a new volume using the following command:
   docker volume create <volume_name>

   Once a volume is created, you can mount it to a container using the -v or --mount option when running a docker run command.


   Bind Directory on a host as a Mount: 
    Bind mounts also aims to solve the same problem but in a complete different way. Using this way, user can mount a directory from the host file system into a container. Bind mounts have the same behavior as volumes, but are specified using a host path instead of a volume name.


Key Differences between Volumes and Bind Directory on a host as a Mount

  Volumes are managed, created, mounted and deleted using the Docker API. However, Volumes are more flexible than bind mounts, as they can be managed and backed up separately from the host file system, and can be moved between containers and hosts.

  In a nutshell, Bind Directory on a host as a Mount are appropriate for simple use cases where you need to mount a directory from the host file system into a container, while volumes are better suited for more complex use cases where you need more control over the data being persisted in the container.


  DOCKER NETWORK 

Network allows containers to communicate each other and the host system. 
There can be reason one container has to talk to another container or there can also be scenario where container should be completly isolated from another container.
Networking allows containers to communicate with each other and with the host system. Containers run isolated from the host system and need a way to communicate with each other and with the host system.

By default, Docker provides two network drivers for you, the bridge and the overlay drivers.

docker network ls
NETWORK ID          NAME                DRIVER
xxxxxxxxxxxx        none                null
xxxxxxxxxxxx        host                host
xxxxxxxxxxxx        bridge              bridge
Bridge Networking
The default network mode in Docker. It creates a private network between the host and containers, allowing containers to communicate with each other and with the host system.


If you want to secure your containers and isolate them from the default bridge network you can also create your own bridge network.

docker network create -d bridge my_bridge
Now, if you list the docker networks, you will see a new network.

docker network ls

NETWORK ID          NAME                DRIVER
xxxxxxxxxxxx        bridge              bridge
xxxxxxxxxxxx        my_bridge           bridge
xxxxxxxxxxxx        none                null
xxxxxxxxxxxx        host                host
This new network can be attached to the containers, when you run these containers.

docker run -d --net=my_bridge --name db training/postgres
This way, you can run multiple containers on a single host platform where one container is attached to the default network and the other is attached to the my_bridge network.

These containers are completely isolated with their private networks and cannot talk to each other.

However, you can at any point of time, attach the first container to my_bridge network and enable communication

docker network connect my_bridge web
image

Host Networking
This mode allows containers to share the host system's network stack, providing direct access to the host system's network.

To attach a host network to a Docker container, you can use the --network="host" option when running a docker run command. When you use this option, the container has access to the host's network stack, and shares the host's network namespace. This means that the container will use the same IP address and network configuration as the host.

Here's an example of how to run a Docker container with the host network:

docker run --network="host" <image_name> <command>
Keep in mind that when you use the host network, the container is less isolated from the host system, and has access to all of the host's network resources. This can be a security risk, so use the host network with caution.

Additionally, not all Docker image and command combinations are compatible with the host network, so it's important to check the image documentation or run the image with the --network="bridge" option (the default network mode) first to see if there are any compatibility issues.

Overlay Networking
This mode enables communication between containers across multiple Docker host machines, allowing containers to be connected to a single network even when they are running on different hosts.

Macvlan Networking
This mode allows a container to appear on the network as a physical host rather than as a container.



We can also create an image for multiarchictures like amd, arm, ıbmz, ıbmp, windows etc.. with commands.
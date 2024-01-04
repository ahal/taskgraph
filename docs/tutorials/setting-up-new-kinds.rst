Setting up Builds and Tests
===========================

In this tutorial we will create real build and test tasks for a Rust project.

Pre-requisites
--------------

This tutorial assumes you have followed the :doc:`getting-started` tutorial.
You should have a working Taskcluster setup with a functioning ``hello-world``
task. If not, please follow this tutorial now.

This tutorial uses a Rust project as an example. So please also ensure you have
`Rust and Cargo installed`_.

.. note::
   You may follow along using another language if you wish. But it will be up
   to you to come up with your own build and test commands!

.. _Rust and Cargo installed: https://www.rust-lang.org/tools/install

Repository Setup
----------------

Before we begin, let's prepare our repository. First, remove the ``hello-world`` task
that was generated in the previous tutorial:

.. code-block:: bash

   $ rm taskcluster/kinds/hello/kind.yml
   $ rm taskcluster/*_taskgraph/transforms/hello.py

Next, let's create an empty Rust project:

.. code-block:: bash

   $ cargo init

This should generate a simple crate that prints out "Hello, world!". Test that you
can compile it by running:

.. code-block:: bash

   $ cargo run

Create a New Docker Image
-------------------------

Taskgraph supports :doc:`in-repo Docker images </howto/docker>`. This means that the
image is defined in your repository and built within your CI. Future tasks can then
download and use the Docker image artifact these tasks produced.

This is super useful because you can update the image alongside the changes
that depend on those updates! But the best part is that the tasks that build the
image are "cached tasks". This means they only need to run once and don't need
to be re-built for each push. They only need to be re-built if you change the image in
some way or the initial "cached task" expires (usually after a year).

The :doc:`getting-started` tutorial already created a ``docker-image`` task for
us, so open up ``taskcluster/kinds/docker-image/kind.yml``. You should see a
single task called ``linux`` that has no configuration. Let's create a second
docker-image task called ``rust``. The ``tasks`` key in the ``kind.yml`` file
should look like:

.. code-block:: bash

   tasks:
     linux: {}
     rust: {}

In Taskgraph, the Dockerfiles for these images live under the
``taskcluster/docker/<name>`` directory, where ``<name>`` corresponds to the
name of the ``docker-image`` task. In our case, this is "rust" so let's create
the ``Dockerfile``:

.. code-block:: bash

   $ mkdir taskcluster/docker/rust
   $ touch taskcluster/docker/rust/Dockerfile

We should add the following to this file:

1. A reference to a base image, in this case let's use the official Rust image:

   .. code-block:: dockerfile

      FROM rust:latest

   .. note::
      For the purposes of this tutorial we're using the ``latest`` tag. But in actual
      CI, it's *strongly* recommended to pin the image to a specific version and manage
      your own updates.

   .. note::
      If you are using a language other than Rust, you'll need to use an
      appropriate base image for it. 


2. Commands to setup the task user and artifacts directory. By convention, the
   user is called ``worker`` and its home directory is ``/builds/worker``

   .. code-block:: dockerfile

      # Add worker user
      RUN mkdir /builds && \
          adduser -h /builds/worker -s /bin/bash -D worker && \
          mkdir /builds/worker/artifacts && \
          chown worker:worker /builds/worker/artifacts

   .. note::
      Taskgraph currently has some hardcoded paths that assume ``/builds/worker``, so
      using a different home directory is not recommended at this time.

3. The ``# % include-run-task`` snippet. In Taskgraph, Dockerfiles are
   pre-processed to allow injecting context from tasks into the image. See
   :doc:`this page </howto/docker>` for more details. For now, you only need to
   understand that this snippet will add Taskgraph's ``run-task`` and
   ``fetch-content`` scripts to a known location in the image. These scripts
   are commonly needed by tasks to run.

4. Optionally setup environment variables that might be needed. What is necessary depends
   on your task, but it's usually a good idea to at least set something like:

   .. code-block:: dockerfile

      ENV SHELL=/bin/bash \
          HOME=/builds/worker \
          PATH=/builds/worker/.local/bin:$PATH

5. Optionally setup volumes to support caching. It's common to mount volumes on
   the host machine so workers can cache things between task runs. Which caches
   are used again depends on your specific task, but it's common to have a
   checkout cache and a dot-file cache:

   .. code-block:: dockerfile
   
      VOLUME /builds/worker/checkouts
      VOLUME /builds/worker/.cache

6. Optionally add a default command in case you want to spin up a container
   manually. This is not needed to run your task, but can be handy for
   debugging:

   .. code-block:: dockerfile

      # Set a default command useful for debugging
      CMD ["/bin/bash"]

All together, your new ``Dockerfile`` should look like:

.. code-block:: dockerfile

   FROM rust:latest
   
   # Add worker user
   RUN mkdir /builds && \
       adduser -h /builds/worker -s /bin/bash -D worker && \
       mkdir /builds/worker/artifacts && \
       chown worker:worker /builds/worker/artifacts
   
   # %include-run-task
   
   ENV SHELL=/bin/bash \
       HOME=/builds/worker \
       PATH=/builds/worker/.local/bin:$PATH
   
   VOLUME /builds/worker/checkouts
   VOLUME /builds/worker/.cache
   
   # Set a default command useful for debugging
   CMD ["/bin/bash"]

Verify that Taskgraph can generate your new task by running:

.. code-block:: bash

   $ taskgraph full

You should see a task called ``docker-image-rust``.

Create a Build Task
-------------------

Create a Test Task
------------------

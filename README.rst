SSHecret
========

.. image:: https://github.com/thcipriani/sshecret/workflows/Python%20application/badge.svg
   :alt: Github workflow badge

.. image:: https://photos.tylercipriani.com/thumbs/2f/ad8870548f45148167f0b41d6e0539/medium.jpg
   :alt: Don't worry, I can keep a sshecret (photo credit: the Nationaal Archief, the Dutch National Archives, and Spaarnestad Photo, via Wikimedia Commons)

If you have an encrypted ssh key for each domain you access (you should), and
you keep your unlocked keys in a single ssh-agent (you maybe shouldn't),
**AND** you've ever decided you need to forward your ssh-agent, then you should
feel bad.

If you forward an ssh-agent with all your unique keys for every domain to a ssh
server that is compromised - all those unique keys for all those unique domains
you access?  **Kablooie!** Done. Have fun rotating them all.

``sshecret`` is a tool that creates an ssh-agent for each identity file found
in your ``ssh_config(5)`` and executes ssh commands for a particular host using
an environment that has access to **only the key for that one host**.

If a server to which you've forwarded your ssh-agent is compromised, then only
the key used for that domain will be affected.

``sshecret`` is a wrapper around ssh that automatically manages multiple
``ssh-agent(1)`` sockets each containing only a single unlocked ssh key.
``sshecret`` accepts the same parameters as ``ssh(1)`` - fundamentally
``sshecret`` uses ``execve(2)`` to wrap ssh, modifying the environment to
ensure that each key in your ``ssh_config(5)`` uses its own ssh-agent.

Install
-------

Install via pip::

    pip install --user sshecret

Wherever ssh is accepted
------------------------

To use ``sshecret`` with git, point ``GIT_SSH`` to use ``sshecret`` by adding
this to your shell initialization file (``~/.bashrc`` or the like)::

    if command -v sshecret > /dev/null 2>&1; then
        export GIT_SSH=sshecret
    fi

To use ``sshecret`` with scp add this alias to your shell initialization file::

    if command -v sshecret > /dev/null 2>&1; then
        alias scp='scp -S sshecret'
    fi

Limitations
-----------

``sshecret`` obviously won't help you if you're using the same ssh key for
multiple domains. You are clearly beyond help.

``sshecret`` depends on a correct ``ssh_config(5)`` for your user (found at
``~/.ssh/config`` or wherever ``$SSH_CONF`` is pointing), so it'll get weird if
that file is weird or nonexistent. Sorry, I guess.

**Requirements**:

* Paramiko_

.. _Paramiko: http://www.paramiko.org/

**Usage**::

  usage: sshecret [whatever you want to pass to ssh]

  sshecret is a wrapper around ssh that automatically manages multiple
  ssh-agent(1)s each containing only a single ssh key.

      EXAMPLE: sshecret -A -L8080:localhost:80 -l johndoe -p2222 example.com

  sshecret accepts the same parameters as ssh(1) - fundamentally sshecret uses
  execve(2) to wrap ssh, modifying the environment to ensure that each key in
  your ssh_config(5) uses its own ssh- agent.

  optional arguments:
    -h, --help  show this help message and exit
    -v          Increase verbosity of output


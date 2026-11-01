# Phase 1 — Foundation (Weeks 1–4)

**Outcome:** become comfortable with a Linux terminal, understand basic network communication, and manage a GitHub repository from the command line.

**Environment:** Android users can begin with Termux for shell/Git practice; a Linux VM or computer is recommended for system administration and SSH labs. Commands differ between Linux distributions. Do not assume Android Termux is identical to a full Linux server.

## Week 1 — Linux orientation and navigation

### Lesson 1.1: What Linux is
Learn kernel vs distribution, shell vs terminal emulator, user space, filesystem hierarchy, package manager, and why Linux is common on servers. Compare Ubuntu, Debian and Fedora at a high level.

### Lesson 1.2: First commands
Practise `pwd`, `whoami`, `uname -a`, `date`, `clear`, `history`, `man COMMAND` and `COMMAND --help`. Understand command, option, argument, standard input, standard output and error output.

### Lesson 1.3: Files and directories
Practise `ls -la`, `cd`, `mkdir`, `touch`, `file`, `stat`, `cp`, `mv`, `cat`, `less`, `head`, `tail` and `wc` inside a dedicated practice folder. Learn absolute vs relative paths, `.`, `..`, and home directory `~`.

### Lesson 1.4: Search and text processing
Learn `find` for locating files, `grep` for matching text, and introductory `sort`, `uniq`, `cut` and pipes. Practise only on sample files you created.

**Lab:** create `~/devops-lab/week1/{notes,logs,scripts}`; create a sample log; display its first and last lines; count lines; search for the word ERROR. Record the commands and outputs.

## Week 2 — Permissions, users, processes and packages

### Lesson 2.1: Permissions
Understand owner, group and others; read/write/execute; symbolic notation such as `rwxr-xr--`; numeric modes such as 755 and 644; directory execute permission; and the principle of least privilege. Inspect with `ls -l` and `stat`. Practise permission changes only on your own sample files.

### Lesson 2.2: Users and groups
Learn user identity, groups, home directories, root, and why daily work should use a normal account. Inspect with `id`, `whoami`, `groups` and `getent passwd` where available. User creation and privilege changes are optional VM-only topics and require administrator permission.

### Lesson 2.3: Processes and services
Learn PID, parent process, foreground/background, signal, daemon and service. Inspect with `ps`, `top` or `htop`, `pgrep` and `systemctl status NAME` on systems using systemd. Understand that a process is a running program while a service is a managed background function.

### Lesson 2.4: Packages and updates
Understand repositories, package indexes, dependencies and package managers. Compare `apt` (Debian/Ubuntu) with `dnf` (Fedora). Learn how to search for a package and inspect its information before installing. Update only a lab system with permission.

### Lesson 2.5: Disk, memory and logs
Inspect with `df -h`, `du -sh`, `free -h`, `uptime`, `journalctl` (where available) and files under `/var/log`. Learn the difference between disk capacity and memory.

**Lab:** create a sample file, inspect its permissions, explain each permission bit, view current processes, and produce a small system-information report. Do not experiment with root permissions on a shared device.

## Week 3 — Networking essentials

### Lesson 3.1: Network vocabulary
Learn host, client, server, router, switch, interface, MAC address, IPv4, IPv6, public/private address, loopback and default gateway.

### Lesson 3.2: IP and subnet concepts
Understand that an IP address identifies a network interface and a subnet mask/prefix separates network and host portions. Practise reading examples such as `192.168.1.10/24`; do not scan unrelated networks.

### Lesson 3.3: DNS
Learn resolver, recursive lookup, authoritative nameserver, A, AAAA, CNAME and MX records. Inspect a public example domain using `nslookup` or `dig` if installed.

### Lesson 3.4: Ports and transport
Understand TCP vs UDP, source/destination ports, listening sockets and common service ports: 22 SSH, 53 DNS, 80 HTTP, 443 HTTPS. A port number alone does not prove which service is running.

### Lesson 3.5: HTTP and HTTPS
Learn request/response, method, status code, headers, body, TLS certificate and encryption in transit. Inspect response headers with `curl -I https://example.com`.

### Lesson 3.6: Firewalls and SSH concepts
Understand allow/deny rules, inbound/outbound traffic, key-based authentication and host-key verification. Use SSH only with a VM/server you own or are authorized to access. Never disable host-key checking as a shortcut.

**Lab:** run `ip addr` or `ipconfig` as available, `ip route`, `nslookup example.com`, `ping -c 4 example.com` (if supported) and `curl -I https://example.com`. Explain what each command tells you.

## Week 4 — Git and GitHub workflow

### Lesson 4.1: Git mental model
Understand repository, working tree, staging area, commit, branch, remote and HEAD. Learn why Git records snapshots rather than simply storing a folder history.

### Lesson 4.2: Start a repository
Practise `git init`, `git status`, `git add`, `git commit`, `git log --oneline` and `git diff`. Configure a display name/email appropriate for your Git commits; do not place credentials in Git config.

### Lesson 4.3: Branches
Learn why branches isolate work. Practise `git switch -c feature/notes`, inspect with `git branch`, and switch back to the main branch.

### Lesson 4.4: Remotes and synchronization
Understand remote, origin, clone, fetch, pull and push. Learn that fetch downloads remote history while pull fetches and integrates it. Use a repository you own.

### Lesson 4.5: Merge and conflicts
Create two branches that edit the same line in a practice file. Read conflict markers, choose the intended final content, remove markers, test the file, stage and commit the resolution. Never resolve a conflict by blindly deleting one side.

### Lesson 4.6: Pull requests
Open a PR, describe the reason for the change, review the diff, respond to feedback and merge. Learn branch protection and why review helps quality.

**Mini project:** from the terminal, clone your own practice repository, create a feature branch, add a useful Linux notes page, commit, push, open a pull request on GitHub, review it and merge. Save the PR link in your notes.

## Phase 1 exit test
- Explain Linux kernel, shell, terminal and distribution.
- Navigate and manage files without a command cheat sheet.
- Explain owner/group/other permissions and least privilege.
- Inspect processes, disk, memory and logs.
- Explain IP, DNS, ports, TCP/UDP, HTTP/HTTPS and SSH.
- Complete a branch → commit → push → PR → merge workflow.
- Demonstrate the mini-project and explain one problem you solved.

**Proof of work:** `16-Projects/phase-1-foundation/README.md` with goals, commands, screenshots or terminal output, what you learned, and cleanup notes.


## Where to learn this phase
Use the curated links in [Resources Directory](RESOURCES.md): Linux → Ubuntu command-line tutorial and Linux Journey; Networking → Cloudflare DNS, MDN HTTP/HTTPS and OpenSSH manual; Git → Pro Git, GitHub Hello World and GitHub Skills. Prefer official references when commands or product behavior matter.

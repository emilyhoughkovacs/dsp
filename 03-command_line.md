# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.


---

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

`>>` | takes output of command on left and *appends* it to file on right
`pushd directoryname` | pushes pwd to stack and moves you to `directoryname`
`pushd` | switches between current directory and last pushed directory
`popd` | pops directory from stack and moves you to it
`find` | `find STARTDIR -name "WILDCARD" -print` (with `| less` if large output) will find files with `WILDCARD` in title, recursively from STARTDIR.
`cat > FILENAME` | You can write text directly to FILENAME. Press `command+D` when done.
`grep` | grep "text to search" files_or_files_to_search (e.g. can do *.txt to search all txt files). only works for files within the pwd I believe
`apropos` | Essentially searches for the keyword within man pages so you can choose which command you want, e.g. `apropos remove`. It also searches git commands.
`env` | Shows what's in your current environment. It's like settings for your bash shell.
`export` | set an environment variable. They are all caps. e.g. `export TESTING="blah"`
`echo $VAR` | print environment variable. you have to use the $
`unset` | sets an environment variable to ""

---


---

What does `ls` do? What do `ls -a`, `ls -l`, and `ls -lh` do? What combinations of those flags are meaningful?

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---


---

What does `xargs` do? Give an example of how to use it.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---


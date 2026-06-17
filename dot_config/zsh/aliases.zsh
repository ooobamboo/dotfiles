# .config/zsh/aliases.zsh

alias vim="nvim" vimdiff="nvim -d"
alias vi="nvim"

alias rr="dbus-run-session -- river"
alias rv="dbus-run-session -- river -c $XDG_CONFIG_HOME/river-classic/init"
alias dl="dbus-run-session -- $HOME/.local/bin/startw"
alias st="exec /usr/bin/gamescope -W 2560 -H 1600 -r 165 -f -m 1 -e -- steam"

alias yarn="yarn --use-yarnrc $XDG_CONFIG_HOME/yarn/config"
alias ff="fastfetch"
alias ns="newsboat"

# git related
alias g="git status"
alias ga="git add"
alias gb="git branch"
alias gc="git commit"
alias gd="git diff"
alias gf="git fetch"
alias gl="git log"
alias gco="git checkout"
alias gp="git push"
alias gr="git rebase"
alias gs="git stash"
alias gu="git pull"

alias n="nnn"
alias v="nvim"

alias wshowkeys="$HOME/wsp/mywm/wshowkeys/build/wshowkeys -a bottom -F 'monospace 20'"

#!/bin/sh

# ディレクトリを取得
current_directory=$(pwd)
alias_command="python3 $current_directory/mario4cmd.py"
echo "set alias"

# エイリアスを設定
alias_list=(
  "ls"
  "cd"
#   "pwd"
  "mkdir"
  "rm"
  "cp"
  "mv"
  "touch"
  "cat"
  "grep"
  "sed"
  "awk"
  "find"
  "chmod"
  "chown"
  "chgrp"
  "tar"
  "gzip"
  "gunzip"
  "zip"
  "unzip"
  "ssh"
  "scp"
  "rsync"
  "ping"
  "traceroute"
  "curl"
  "wget"
  "ps"
  "top"
  "kill"
  "uname"
  "df"
  "du"
)

echo "List of common Linux commands:"

for command in "${alias_list[@]}"; do
    echo "alias $command=$alias_command"
    alias $command=$alias_command
done

# clearコマンドを実行すると良いと思います
echo 'You can blank the terminal with the "clear" command.'
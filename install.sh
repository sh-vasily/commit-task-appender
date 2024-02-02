#!/bin/sh

target_repository_dir=$1
installation_dir="$target_repository_dir/.git/hooks/"
script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Installing hook for ${target_repository_dir}"

cp -r "$script_dir/hook/commit-msg" "$installation_dir"
cp -r "$script_dir/hook/commit_processor.py" "$installation_dir"

strategy="insert_branch_name"

if [ -n "$2" ]; then
    strategy="$2"
    echo "${strategy}" > "$installation_dir/processor.conf"
fi

echo "Hook installed in ${target_repository_dir}. Strategy - ${strategy} will be used."

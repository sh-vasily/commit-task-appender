#!/bin/sh

target_repository_dir=$1
installation_dir="$target_repository_dir/.git/hooks/"
script_dir=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo "Installing hook for ${target_repository_dir}"


cp -r "$script_dir/hook/commit-msg" "$installation_dir"
cp -r "$script_dir/hook/commit_processor.py" "installation_dir"

echo "Hook installed in ${target_repository_dir}"

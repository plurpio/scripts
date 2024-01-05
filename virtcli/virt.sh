#! /bin/bash

# Virtual machine creator
choice=$(echo -e "Add\n$(virsh list --all --name)" | wofi --dmenu --prompt="Select a virtual machine: ")

case "$choice" in
  Add)
    kitty -e ~/scripts/virtcli/virtAdd.sh
    remote-viewer spice://127.0.0.1:5900 -f -r
    ;;
  *)
    virsh -q start $choice
    remote-viewer spice://127.0.0.1:5900 -f -r
    ;;
esac

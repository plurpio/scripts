#! /bin/bash

sudo virsh start $(virsh list --all --name | wofi -i --dmenu)

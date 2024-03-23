#!/bin/bash
echo "Backup Started" > /$HOME/Videos/Logs/"backup_$(date '+%Y-%m-%d').txt"
rclone sync -v --create-empty-src-dirs /$HOME/Videos/Logs gdrive:/Videos/Logs
rclone sync -v --create-empty-src-dirs /$HOME/Videos gdrive:/Videos
echo "Backup Complete" >> /$HOME/Videos/Logs/"backup_$(date '+%Y-%m-%d').txt"
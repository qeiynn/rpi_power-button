#! /bin/sh

case "$1" in
  start)
    echo "Activating Power-Button script"
    /usr/local/bin/shutdown-button.py &
    ;;
  stop)
    echo "Deactivating Power-Button script"
    pkill -f /usr/local/bin/shutdown-button.py
    ;;
  *)
    echo "Usage: /etc/init.d/shutdown-button.sh {start|stop}"
    exit 1
    ;;
esac

exit 0

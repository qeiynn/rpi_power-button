#!/bin/sh

### BEGIN INIT INFO
# Provides:          shutdown-button.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start Power-Button script at boot time
# Description:       Power-Button script activates safe shutdown by 2-3 secs button press.
### END INIT INFO

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

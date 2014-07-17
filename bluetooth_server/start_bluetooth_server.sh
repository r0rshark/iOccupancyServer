./start_bluetooth
RESULT=$?
if [ $RESULT -eq 0 ]; then
  . venv/bin/activate
  python bluetooth_server.py
else
  echo "Problem in starting the bluetooth server"
fi


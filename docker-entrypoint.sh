#!/bin/bash

if [ -f "/usr/local/bin/docker-pre-entrypoint.sh" ]; then
    echo "=> found pre-entrypoint script"
	/usr/local/bin/docker-pre-entrypoint.sh
fi

exec "$@"
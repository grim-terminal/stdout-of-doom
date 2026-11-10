# stdout-of-doom

Summarise a log file from the terminal.

```sh
python -m doom.cli app.log
tail -n 5000 app.log | python -m doom.cli -
```

Lines look like `2026-11-09T21:43:48Z ERROR payment gateway timeout`.
Levels: DEBUG, INFO, WARN, ERROR. Anything else is skipped.

Run the tests with `python -m pytest`.

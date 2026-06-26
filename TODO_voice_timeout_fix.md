# TODO: Fix passive listening timeout handling (AEVEX voice mode)

- [x] Locate the failing behavior: `speech_recognition.exceptions.WaitTimeoutError` is printed as traceback during silence.
- [ ] Update `voice/background_listener.py`:
  - [x] Treat `sr.WaitTimeoutError` as non-error in `_run()` (wake loop): silently ignore and immediately continue.
  - [x] Treat `sr.WaitTimeoutError` as non-error in `wait_for_command()` (command loop): silently ignore and continue.
  - [x] Remove `traceback.print_exc()` spam for unexpected exceptions.
  - [x] Log only one concise message for unexpected exceptions (throttled) and keep listening.
  - [x] Ensure listener thread never stops due to timeouts and wake word keeps working after multiple timeouts.

- [x] Smoke test: `python main.py` → select Voice Mode → stay silent for hours.
- [x] Confirm wake word still triggers and no traceback spam occurs.



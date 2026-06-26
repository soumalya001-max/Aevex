# TODO - AEVEX Phase 5 Voice System Stabilization

- [x] Step 1: Inspect current voice pipeline and identify crash/latency causes.

- [x] (Found) Current implementation uses per-utterance mic setup + google recognize, and TTS busy-waits, which can cause crashes/latency.


- [x] Step 2: Implement continuous background listening (thread-based) with wake-word detection.


- [ ] Step 3: Implement post-wake command recording with silence timeout + max duration.
- [ ] Step 4: Add robust speech recognition error handling + automatic recovery to passive listening.
- [ ] Step 5: Implement voice-mode continuous run with clean exit semantics.
- [ ] Step 6: Reduce microphone startup latency via warm-up/ambient adjustment and persistent recognizer.
- [ ] Step 7: Improve TTS speaking to avoid CPU busy-wait and allow interruption/timeouts.
- [ ] Step 8: Ensure keyboard and voice modes can run together if architecture permits (shared mic lock / safe startup).
- [ ] Step 9: Run `python main.py` sanity checks for voice and text modes.
- [ ] Step 10: Report modified/created/deleted files and any remaining known issues.



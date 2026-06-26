WAKE_WORDS = [
    "aevex",
    "hey aevex",
]

# Background listening tuning
SAMPLE_RATE = 16000

# Wake-word stage: stop/trim to reduce latency
WAKE_POLL_INTERVAL_SEC = 0.15

# Command recording stage
MAX_RECORDING_SEC = 12
SILENCE_TIMEOUT_SEC = 1.2

# If speech recognition keeps failing, throttle retries
RECOGNITION_FAILURE_BACKOFF_SEC = 1.0

# Hard cap to prevent indefinite hang
MAX_WAKE_LISTEN_ITERATIONS = 1000000

# If True, will print wake/command diagnostics.
DEBUG_VOICE = False



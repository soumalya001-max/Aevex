import threading

# Shared across voice modules to avoid concurrent microphone usage.
MIC_LOCK = threading.Lock()


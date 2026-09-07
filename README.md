# ⚔️ Focus Guillotine

A native, zero-dependency macOS background productivity application designed to break cognitive doomscrolling habits via automated operating system-level process management.

## 💡 The Pain Point
Traditional browser extensions are too easy to bypass; when focus wavers, clicking "disable extension" takes two seconds. I built this script to remove my own administrative choice. The millisecond a blacklisted window profile enters focus, the system intervenes instantly.

## 🛠️ How It Works
- Runs an infinite monitoring event loop checking the OS window manager state via `osascript`.
- Intercepts system events to parse the frontmost process signature natively.
- Evaluates active window handles against an immutable blocklist array (`google chrome`, `safari`, etc.).
- Triggers a secure, absolute termination signal (`pkill -9`) directly to the target browser application.
- Wipes the active terminal environment to drop a persistent, flashing macro warning alert.

## 🚀 Setup & Execution
Run natively on macOS without any external third-party software package layers:
```bash
python3 guillotine.py
```

# onedir contents-directory rename repro

Reproduction for a PyInstaller issue: while an onedir application is running on Windows,
its contents directory (`.runtime` here, set via `--contents-directory`) cannot be renamed —
the app appears to hold a handle on `<contents-dir>/base_library.zip`.

Observed on Windows 11 (10.0.26100) with Python 3.11.12:

- `pyinstaller==6.21.0` / `6.22.3` / develop → rename fails (`WinError 5` for the directory,
  `WinError 32` for `base_library.zip` itself)
- `pyinstaller==6.7.0` → rename works

This repository runs the build + probe on GitHub Actions (`windows-latest`) to check whether
the behavior is intrinsic to the build or specific to a local machine.

`toy.py` is the minimal app; `probe.py` does the renames. Results are printed in the workflow
log and uploaded as an artifact.

# Repository Change Workflow

Follow this workflow for every feature, bug fix, configuration change, or release.

## Before Editing

1. Inspect the owning implementation, nearby tests, and the relevant documentation.
2. Identify every corresponding surface before changing code:
   - `source/`: application behavior and version metadata
   - `tests/`: regression and behavior coverage
   - `README.md`: user-facing features and usage
   - `CHANGELOG.md`: change notes, with newest releases first
   - `PROJECT_STATUS.md`: current version, status, and release summary
   - `CONTRIBUTING.md`: development or release process changes
   - `.github/workflows/`: CI/build behavior
   - `Game.ini` and `GameUserSettings.ini`: sample configuration changes, when applicable
3. Keep unrelated files unchanged. A corresponding file is updated when the change affects its content, not merely because it exists.

## While Editing

1. Fix the owning behavior and preserve existing project conventions.
2. Add or update focused tests for behavior changes.
3. Update every affected documentation, sample configuration, dependency, build, and workflow surface in the same change.
4. For a numbered release, update `__version__` and `VERSION_INFO` together.
5. Keep `CHANGELOG.md` in newest-to-oldest order. Move released notes into a dated version heading and keep future ideas outside released sections.

## Validation Before Commit

1. Run `pytest tests -v`.
2. For release or build changes, run the documented PyInstaller build and verify the executable is produced.
3. Check `git diff --check`.
4. Search for stale version numbers, feature names, paths, and configuration keys across tracked source and documentation.
5. Review `git diff` and `git status` to confirm that only intended files changed.

## Commit and Push

1. Use a clear, imperative commit message describing the synchronized change.
2. Commit implementation, tests, documentation, metadata, and workflow updates together when they belong to the same change.
3. Push the branch after validation when requested by the user.
4. Report the commit, push result, tests, build result, and any remaining unrelated worktree changes.

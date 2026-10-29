# Microsoft Visual C++ 6.0 SP6 (Enterprise)

Toolchain tree for reproducible builds with the original compiler, laid out like the
`archaic-msvc` 5.0 repositories (all paths lower case) so it can be pinned by the
ReproBit `msvc_6_0_sp6` profile.

| Tool | Version |
|---|---|
| `bin/cl.exe` | 12.00.8804 |
| `bin/c1.dll`, `bin/c1xx.dll`, `bin/c2.dll` | 12.00.9782 |
| `bin/link.exe` | 6.00.8447 |
| `bin/mspdb60.dll`, `bin/lib.exe` | 6.00.8168 |
| `bin/rc.exe`, `bin/rcdll.dll` | 5.00.1641.1 |
| `bin/cvtres.exe` | 5.00.1736.1 |

## Provenance

- Base: `VC98` from Visual Studio 6.0 Enterprise CD 1 (`VS98ECD1`), plus
  `mspdb60.dll`, `rc.exe`, `rcdll.dll`, `msdis110.dll` from `COMMON/MSDEV98/BIN`.
- The CD stores some files under 8.3 names; they are renamed exactly as the
  setup does (`SETUP/VS98ENT.INF`, see `tools/installer-renames.json`), and
  `MFC/SRC/PLATFORM` is installed as `mfc/src/intel`.
- Overlay: `vc98/*` from `Vs6sp6.exe` (`VS6sp61..4.cab`). SP6 ships the
  code generator per edition; the Enterprise/Professional one
  (`os/system/msvcep.dll`) is installed as `bin/c2.dll`.
- `Vs6sp6.exe` SHA-256: `7fa1d1778824b55a5fceb02f45c399b5d4e4dce7403661e67e587b5f455edbf3`

`tools/assemble.py` is the script that produced this tree.

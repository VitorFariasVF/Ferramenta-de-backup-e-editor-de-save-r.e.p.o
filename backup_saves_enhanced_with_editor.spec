# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\program\\backup_saves_enhanced_with_editor.py'],
    pathex=[],
    binaries=[],
    datas=[('src/translations', 'translations'), ('src/program/save_editor_core.py', 'program')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='backup_saves_enhanced_with_editor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['repo_icon.ico'],
)

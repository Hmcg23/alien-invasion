# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['alien_invasion.py'],
    pathex=[],
    binaries=[],
    datas=[('/Users/hudsonmcgough/Desktop/Loyola - School/Computer Programming/alien_invasion/sounds', './sounds'), ('/Users/hudsonmcgough/Desktop/Loyola - School/Computer Programming/alien_invasion/images', './images'), ('/Users/hudsonmcgough/Desktop/Loyola - School/Computer Programming/alien_invasion/fonts', './fonts')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='alien_invasion',
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
    icon=['CFE.icns'],
)
app = BUNDLE(
    exe,
    name='alien_invasion.app',
    icon='CFE.icns',
    bundle_identifier=None,
)

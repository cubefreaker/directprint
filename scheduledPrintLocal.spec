# -*- mode: python -*-

block_cipher = None


a = Analysis(['scheduledPrintLocal.py'],
             pathex=['E:\\AutoprintFix\\repo\\dist'],
             binaries=[],
             datas=[],
             hiddenimports=['schedule','win32api','win32print','urllib','threading','requests','win32timezone'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='scheduledPrintLocal',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
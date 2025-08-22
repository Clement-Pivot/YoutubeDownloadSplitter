from kivy.deps import sdl2, glew

# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['C:\\Users\\Malfeisoif\\AppData\\Local\\Packages\\TheDebianProject.DebianGNULinux_76v4gfsz19hv4\\LocalState\\rootfs\\home\\malfeisoif\\dev\\YouTubeDownLoader'],
             binaries=None,
             datas=None,
             hiddenimports=['win32timezone'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
		  *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
          name='main',
          debug=False,
          strip=False,
          upx=True,
          console=True )
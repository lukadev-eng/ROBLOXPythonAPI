from distutils.core import setup
setup(
  name = 'robloxapi',
  packages = ['robloxapi', 'robloxapi.utils'],
  version = '4.7',
  license='MIT',       
  description = 'A Python wrapper for roblox',
  long_description = '''
  ''',
  url = 'https://github.com/lukadev-eng/ROBLOXPythonAPI',
  author = 'Lukadev-eng',                
  author_email = 'lukadevpersonal@gmail.com',
  keywords = ['python_roblox', 'roblox', 'robloxapi'],
  install_requires=[            
          'httpx',
          'beautifulsoup4',
          'requests',
          'http3'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      

    'Intended Audience :: Developers',     
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.6',
  ],
)

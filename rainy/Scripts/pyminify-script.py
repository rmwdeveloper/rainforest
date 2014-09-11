#!C:\Users\robert\rainforest\rainy\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'django-htmlmin==0.7.0','console_scripts','pyminify'
__requires__ = 'django-htmlmin==0.7.0'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('django-htmlmin==0.7.0', 'console_scripts', 'pyminify')()
    )

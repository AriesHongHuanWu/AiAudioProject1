from setuptools import setup, find_packages

setup(
    name='ai_music_tool',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-SocketIO',
        'spleeter',
        'pydub',
        'magenta',
    ],
    entry_points={
        'console_scripts': [
            'ai_music_tool=app:main',
        ],
    },
)

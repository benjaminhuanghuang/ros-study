
Modify setup.py
```
    (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    (os.path.join('share', package_name, 'urdf'), glob('urdf/**')),
    (os.path.join('share', package_name, 'world'), glob('world/**')),
```
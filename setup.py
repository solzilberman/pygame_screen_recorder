from setuptools import setup, find_packages
 
classifiers = [
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='pygame_screen_recorder',
  version='1.3',
  description='Util for taking screenshots and recording videos of pygame simulations.',
  long_description="See the full documentation on github.",
  url='https://github.com/solzilberman/pygame_screen_recorder',  
  author='Sol Zilberman',
  author_email='sol.zilberman@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='pygame', 
  packages=find_packages(),
  install_requires=['pygame', 'imageio'] 
)


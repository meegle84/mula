from setuptools import find_packages, setup


def get_readme():
    readme = ''
    try:
        import pypandoc
        readme = pypandoc.convert('README.md', 'rst')
    except (ImportError, IOError):
        with open('README.md', 'r') as file_data:
            readme = file_data.read()
    return readme


setup(
    name='twitter-cam-bot',
    version='0.1',
    author='Miguel Angel Blanco Muñoz',
    author_email='meegle84@gmail.com',
    description=('A simple bot that takes photos from cam, '
                 'makes a gif and upload it to twitter'),
    long_description=get_readme(),
    license='BSD',
    keywords='twitter cam bot gif',
    url='https://github.com/meegle84/twitter-cam-bot',
    packages=find_packages(),
    install_requires=['cv2',
                      'twython'],
)

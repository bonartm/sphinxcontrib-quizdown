import pathlib
from setuptools import setup, find_namespace_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='sphinxcontrib-quizdown',
    version='0.3',
    description='Use markdown-like syntax to create interactive quizzes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/bonartm/sphinxcontrib-quizdown',
    author='Malte Bonart',
    author_email='malte@spiced-academy.com',
    classifiers=[
        'Environment :: Console',
        'Environment :: Web Environment',
        'Framework :: Sphinx :: Extension',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Utilities'
    ],
    keywords='quiz, markdown, quizdown, sphinx',
    packages=find_namespace_packages(include=['sphinxcontrib.*']),
    python_requires='>=3.6, <4',
    install_requires=['sphinx', 'docutils'],
    project_urls={
        'quizdown-js': 'https://github.com/bonartm/quizdown-js',
        'Live Editor': 'https://bonartm.github.io/quizdown-live-editor/',
        'Source': 'https://github.com/bonartm/sphinxcontrib-quizdown',
    },
)

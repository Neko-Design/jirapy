from setuptools import setup

setup(
    name='jirapy',
    packages=['jirapy'],
    install_requires=[
        'requests'
    ],
    version='0.1',
    description='JIRA Data Wrapper for Easy WebHook Handling',
    author='Ewen McCahon',
    author_email='ewen.m.mccahon@student.uts.edu.au',
    url='https://github.com/Neko-Design/jirapy',
    keywords=['jira', 'api', 'wrapper', 'interface', 'webhooks', 'comments'],
    classifiers=[],
    license='APACHE2'
)

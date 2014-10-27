from __future__ import with_statement
import openravepy
import tempfile

def load(source, content_type='application/zip'):

    # determine content type
    suffix = ''
    if content_type == 'application/xml':
        suffix = '.xml'
    if content_type == 'application/zip':
        suffix = '.zae'

    # write source into a file, then load it in openrave
    env = openravepy.Environment()
    with tempfile.NamedTemporaryFile(suffix=suffix) as f:
        f.write(source)
        f.flush()

        if not env.Load(f.name):
            raise ValueError('Failed to parse the file.')

    # extract information from the robot
    data = {}
    with env:
        robot = env.GetRobots()[0]
        data = {
            'name': robot.GetName(),
            'dof': robot.GetDOF(),
        }

    return data


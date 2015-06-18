 A simple function to load .pts files with python. Once the file is on your path, you simply use it as follows:

    from pts_loader import load

    path = 'path to your .pts file'
    points = load(path)

The test pts data comes from [this](http://ibug.doc.ic.ac.uk/resources/300-W/) public dataset.
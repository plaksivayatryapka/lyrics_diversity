import subprocess
import pickle
def load_vars(**kwargs):
    if 'filename' in kwargs:
        filename = kwargs['filename']
        with open(filename, 'rb') as dumpfile:
            return pickle.load(dumpfile)
        
    elif 'path' in kwargs:
        path = kwargs['path']
        with open(path, 'rb') as dumpfile:
            return pickle.load(dumpfile)
        

def save_vars(**kwargs):
    variable = kwargs['variable']
    if 'filename' in kwargs:
        filename = kwargs['filename']
        with open(filename, 'wb') as dumpfile:
            pickle.dump(variable, dumpfile, protocol=2)
    
    elif 'path' in kwargs:
        path = kwargs['path']
        with open(path, 'rb') as dumpfile:
            return pickle.load(dumpfile)


def average(lst):
    if len(lst) == 0:
        return None
    return sum(lst) / float(len(lst))
    


def launch_file(**kwargs):
    path = kwargs['path']
    subprocess.call(('xdg-open', path))


def notify(**kwargs):
    text=kwargs['text']
    subprocess.call(('notify-send', text))
    subprocess.call(('play', '~/coding/beep-3.wav'))

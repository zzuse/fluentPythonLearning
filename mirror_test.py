with open('foo.csv') as fp:
    src = fp.read(60)

print("len(src) {}\n----------".format(len(src)))
print("fp {}\n----------".format(fp))
print("fp.closed, fp.encoding {} {}\n----------".format(fp.closed, fp.encoding))


from mirror import LookingGlass
with LookingGlass() as what:
    print('Alice, Kitty and Snowdrop')
    print(what)

print("what {}\n----------".format(what))
print('Back to normal.')


from mirror import LookingGlass
manager = LookingGlass()
print("manager {}\n----------".format(manager))
monster = manager.__enter__()
monster == 'JABBERWOCKY'
print("monster {}\n----------".format(monster))
print("manager {}\n----------".format(manager))
manager.__exit__(None, None, None)
print("monster {}\n----------".format(monster))


from mirror_gen import looking_glass
with looking_glass() as what:
    print('Alice, kitty and Snowdrop')
    print(what)

print("what {}\n----------".format(what))


# bit.ly/1MM96aR Martijin's
from contextlib import contextmanager
import io
import os


@contextmanager
def inplace(filename, mode='r', buffering=-1, encoding=None, errors=None,
            newline=None, backup_extension=None):
    """Allow for a file to be replaced with new content.

    yields a tuple of (readable, writable) file objects, where writable
    replaces readable.

    If an exception occurs, the old file is restored, removing the
    written data.

    mode should *not* use 'w', 'a' or '+'; only read-only-modes are supported.

    """

    # move existing file to backup, create new file with same permissions
    # borrowed extensively from the fileinput module
    if set(mode).intersection('wa+'):
        raise ValueError('Only read-only file modes can be used')

    backupfilename = filename + (backup_extension or os.extsep + 'bak')
    try:
        os.unlink(backupfilename)
    except os.error:
        pass
    os.rename(filename, backupfilename)
    readable = io.open(backupfilename, mode, buffering=buffering,
                       encoding=encoding, errors=errors, newline=newline)
    try:
        perm = os.fstat(readable.fileno()).st_mode
    except OSError:
        writable = open(filename, 'w' + mode.replace('r', ''),
                        buffering=buffering, encoding=encoding, errors=errors,
                        newline=newline)
    else:
        os_mode = os.O_CREAT | os.O_WRONLY | os.O_TRUNC
        if hasattr(os, 'O_BINARY'):
            os_mode |= os.O_BINARY
        fd = os.open(filename, os_mode, perm)
        writable = io.open(fd, "w" + mode.replace('r', ''), buffering=buffering,
                           encoding=encoding, errors=errors, newline=newline)
        try:
            if hasattr(os, 'chmod'):
                os.chmod(filename, perm)
        except OSError:
            pass
    try:
        yield readable, writable
    except Exception:
        # move backup back
        try:
            os.unlink(filename)
        except os.error:
            pass
        os.rename(backupfilename, filename)
        raise
    finally:
        readable.close()
        writable.close()
        try:
            os.unlink(backupfilename)
        except os.error:
            pass


import csv
with inplace("a.csv", 'r', newline='') as (infh, outfh):
    reader = csv.reader(infh)
    writer = csv.writer(outfh)

    for row in reader:
        row += ['new', 'columns']
        writer.writerow(row)


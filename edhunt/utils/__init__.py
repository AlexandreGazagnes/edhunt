import os
import secrets
import PyPDF2
from PIL import Image
from pdf2image import convert_from_path, convert_from_bytes


def give_default_password():
    return "********"


def give_default_email():
    return "no_email@email.com"


def manage_txt_form(txt):
    txt = txt.split(",")
    txt = [i.strip().replace("  ", " ").replace("  ", " ").replace("-", " ")
           for i in txt if i]
    txt = [i for i in txt if i]
    return ", ".join(txt)


def cut_1_px(path, fmt="png"):

    if path[0] == "/":
        path = path[1:]

    img = Image.open(path)

    if img.size == (1920, 1080):
        box = (1, 1, 1919, 1079)
        area = img.crop(box)
        area.save(path, fmt)


def rename_resize_images(folder, force=False, fmt='png', root="edhunt/static/"):

    if folder[0] == "/":
        folder = folder[1:]

    if folder[-1] != "/":
        folder += "/"

    files = sorted(os.listdir(root + folder))
    changes = [(root + folder + f, root + folder + f"slide{str(i).rjust(2, '0')}.png") for i, f in enumerate(files)]

    _ = [print(f"{old}\t: {new}") for old, new in changes]

    if force:
        ans = True
    else:
        ans = input("accept changes? - y for Yes\n")
        ans = True if ans.lower() == "y" else False

    if ans:
        for old, new in changes:
            os.rename(old, new)
            cut_1_px(new, fmt=fmt)
        print("done")
    else:
        print("aborted")


def rename_resize_all(force=True, fmt='png', root="edhunt/static/"):

    folders = ["suis", "peux", "soyez", "allez", "allezplus", "saviez", "cest"]
    for folder in folders:
        path = f'images/main/carousel/{folder}'
        rename_resize_images(path, force=force, fmt=fmt, root=root)


def touch(fname, times=None):
    with open(fname, 'a'):
        os.utime(fname, times)


def load_img(x):
    return Image.open(x)


def compute_I(x, fact):
    return [int(i / fact) for i in x.size]


def resize(x, I):
    return x.resize(I, Image.ANTIALIAS)


def truncate_image(x, w, h):
    return x.crop((0, 0, w, h))


def save_img(x, name):
    x.save(name, optimize=True)


def transform_img(x, fact=9.8, w=494, h=272):
    im = load_img(x)
    print(str(im.size))
    _I = compute_I(im, fact)
    im = resize(im, _I)
    print(str(im.size))
    im = truncate_image(im, w, h)
    print(str(im.size))
    save_img(im, 'small_' + x)

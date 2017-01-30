import numpy as np
import os
import csv
from PIL import Image


def overlap(a, b):
    if (a[0][0] <= b[0][0] <= a[0][1] <= b[0][1]
        and a[1][0] <= b[1][0] <= a[1][1] <= b[1][1] or
                            b[0][0] <= a[0][0] <= b[0][1] <= a[0][1]
            and a[1][0] <= b[1][0] <= a[1][1] <= b[1][1] or
                            b[0][0] <= a[0][0] <= b[0][1] <= a[0][1]
            and b[1][0] <= a[1][0] <= b[1][1] <= a[1][1] or
                            a[0][0] <= b[0][0] <= a[0][1] <= b[0][1]
            and b[1][0] <= a[1][0] <= b[1][1] <= a[1][1]):
        return True
    else:
        return False


def extract_patches(row, directory, image, image_x, image_y, dim_patch=(48, 48), overlap_allowed=False, patchN=100):
    width = image.shape[0]
    height = image.shape[1]

    active = image
    active_x = image_x
    active_y = image_y

    n = 0
    destination = []

    while n < patchN:
        row_start = int(np.random.randint(width - dim_patch[0]))
        col_start = int(np.random.randint(height - dim_patch[1]))

        region = (slice(row_start, row_start + dim_patch[0]),
                  slice(col_start, col_start + dim_patch[1]))

        index = [[row_start, row_start + dim_patch[0]],
                 [col_start, col_start + dim_patch[1]]]

        if any(overlap(index, dest) for dest in destination):
            continue
        else:
            if row[4] == "CCD":
                patch = active[region]
                patch_x = active_x[region]
                patch_y = active_y[region]

                directory_img = os.path.join(directory, 'IMG', 'CCD', row[1], row[2])
                directory_x = os.path.join(directory, 'X', 'CCD', row[1], row[2])
                directory_y = os.path.join(directory, 'Y', 'CCD', row[1], row[2])
                directory_index = os.path.join(directory, 'INDEX', 'CCD', row[1], row[2])
                if not os.path.exists(directory_img):
                    os.makedirs(directory_img)
                if not os.path.exists(directory_x):
                    os.makedirs(directory_x)
                if not os.path.exists(directory_y):
                    os.makedirs(directory_y)
                if not os.path.exists(directory_index):
                    os.makedirs(directory_index)

                np.save(os.path.join(directory_img, "%d" % n), patch)
                np.save(os.path.join(directory_x, "%d" % n), patch_x)
                np.save(os.path.join(directory_y, "%d" % n), patch_y)
                np.save(os.path.join(directory_index, "%d" % n), index)
                n += 1
            else:
                patch = active[region]
                patch_x = active_x[region]
                patch_y = active_y[region]

                directory_img = os.path.join(directory, 'IMG', 'CMOS', row[1], row[2])
                directory_x = os.path.join(directory, 'X', 'CMOS', row[1], row[2])
                directory_y = os.path.join(directory, 'Y', 'CMOS', row[1], row[2])
                directory_index = os.path.join(directory, 'INDEX', 'CMOS', row[1], row[2])
                if not os.path.exists(directory_img):
                    os.makedirs(directory_img)
                if not os.path.exists(directory_x):
                    os.makedirs(directory_x)
                if not os.path.exists(directory_y):
                    os.makedirs(directory_y)
                if not os.path.exists(directory_index):
                    os.makedirs(directory_index)

                np.save(os.path.join(directory_img, "%d" % n), patch)
                np.save(os.path.join(directory_x, "%d" % n), patch_x)
                np.save(os.path.join(directory_y, "%d" % n), patch_y)
                np.save(os.path.join(directory_index, "%d" % n), index)
                n += 1


file_csv = input("Directory of the database: ")
f = open(file_csv)
csv_f = csv.reader(f)
directory = input("Directory to save: ")

for row in csv_f:
    if row[3] == "Path":
        continue
    else:
        img_x = np.asarray(Image.open(row[3]))#Insert row of the Image Path
        gr_x = np.asarray(Image.open(row[3])) # Insert row of the Gradient_x Path
        gr_y = np.asarray(Image.open(row[3])) #Insert row of the Gradient_y path

        extract_patches(row, directory, gr_x, gr_z, gr_y, dim_patch=(48, 48), overlap_allowed=False, patchN=100)

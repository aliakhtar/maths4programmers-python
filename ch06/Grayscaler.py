from ch06.ImageVector import *


class Grayscaler():
    def __init__(self, img_rows=500, img_cols=500,
                 square_width=10, square_count=50):
        self.img_rows = img_rows
        self.img_cols = img_cols
        self.sq_width = square_width
        self.sq_count = square_count
        self.total_img_pixels = img_rows * img_cols

    def locate_block(self, pixel_index):
        # Each row has 500 columns, and at each 500th column we start the next row. So, by diving the pixel index / rows
        # we determine which row it belongs to. E.g 0 // 500 = row 0, 500 // 500 = row 1, 1000 // 500 = row 2, etc
        block_row = pixel_index // self.img_rows

        # This one is harder to wrap your mind around. Still don't fully understand it.
        # Some examples though: 0 % 500 = col 0, obviously. 1 % 500 = 1 (because it won't go into decimals). Same goes
        # for all digits < 500, it'll return them all as is.

        # Once you go >= 500, the remainder happens to be the same as the column index. Eg 501 / 500 = 1, and so on.
        # Trippy but it works.
        block_col = pixel_index % self.img_cols

        # print("Pixel: {}, row: {}, col: {}".format(pixel_index, block_row, block_col))
        return (block_row, block_col)

    # Expects a matrix of the dimensions square_count * square_count. Each element of the matrix represents a square
    # block in the original image of the dimensions square_width * square_width.

    # This method maps each element of the matrix into squares of their original size and returns them.
    def img_from_lowres(self, lowres_matrix):
        new_pixels = []
        for i in range(self.total_img_pixels):
            matrix_row, matrix_col = self.locate_block(i)
            brightness_avg = lowres_matrix[matrix_row // self.sq_width][matrix_col // self.sq_width]
            new_pixels.append((brightness_avg, brightness_avg, brightness_avg))

        return ImageVector(new_pixels)

    def to_lowres(self, img):
        lowres = [
            [0 for _ in range(self.sq_count)]  # cols
            for _ in range(self.sq_count)  # rows
        ]

        weight = 1 / (3.0 * self.sq_width * self.sq_width)

        for index, pixel_coords in enumerate(img.pixels):
            pixel_avg = sum(pixel_coords) * weight
            row, col = self.locate_block(index)
            lowres[row // self.sq_width][col // self.sq_width] += pixel_avg

        return lowres

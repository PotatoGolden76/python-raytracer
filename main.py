from Utils.color import Color
from Utils.image import Image

TEST_WIDTH = 800
TEST_HEIGHT = 600

if __name__ == "__main__":
    img = Image("test", TEST_HEIGHT, TEST_WIDTH)
    for i in range(TEST_HEIGHT):
        for j in range(TEST_WIDTH):
            img.set_pixel(j, i, Color.from_tuple(
                (int((float(j) / float(TEST_WIDTH)) * 256), int((float(i) / float(TEST_HEIGHT)) * 256),
                 int((float(i * j) / float(TEST_WIDTH * TEST_HEIGHT)) * 256))))

    # print(img.get_file_data())
    with open("test.ppm", "w") as g:
        g.writelines(img.get_file_data())

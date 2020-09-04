def main():


    ratio_to_add_on_longer_side = 5 / 100

    width_input = 3483
    height_input = 1000

    target_aspect_ratio = 1 / 1  # Breite / Hoehe

    if height_input > width_input:



        new_height = height_input * (1 + ratio_to_add_on_longer_side)
        new_width = target_aspect_ratio * new_height




    else:

        new_width = width_input * (1 + ratio_to_add_on_longer_side)
        new_height = target_aspect_ratio * new_width

    print("Endwert Skalierung Höhe [1/2]: %i" % ((height_input + new_height) / 2))
    print("Endwert Skalierung Höhe [2/2]: %i" % (new_height))
    print("Endwert Skalierung Breite [1/2]: %i" % ((width_input + new_width) / 2))
    print("Endwert Skalierung Breite [3/2]: %i" % (new_width))


if __name__ == '__main__':
    main()

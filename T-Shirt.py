def make_shirt(size, text):
    print('Shirt size: {0} text on shirt: "{1}"'.format(size, text))


# positional
make_shirt("M", "Cool Shirt")
# keyword
make_shirt(text="Cool shirt", size="M")

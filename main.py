from bitcoin import BTCSegwit, green, yellow


btcsegwit = BTCSegwit()


if __name__ == '__main__':
    btcsegwit.document()

    print(green("\nSegwit Bitcoin Address: "), yellow(btcsegwit.SADDRESS))
    print(green("Segwit Private Key WIF: "), yellow(btcsegwit.SWIF))

    btcsegwit.answer()

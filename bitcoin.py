import hashlib
import base58
import bech32
import binascii
import ecdsa


def green(text):
    """
    ANSI Code to turn strings green.
    """
    return f"\033[92m{text}\033[0m"


def yellow(text):
    """
    ANSI Code to turn strings yellow.
    """
    return f"\033[93m{text}\033[0m"


class BTCSegwit():
    def __init__(self):
        """
        SPVKEY: Private Key
        SPUKEY: Public Key
        SSHA256PUKEY: SHA256 Encoded Public Key
        SRIDEMP160PUKEY: RIDEMP160 Encoded SSHA256PUKEY
        SIG: Unhexlified '0014' added to SRIDEMP160PUKEY
        SVERSION: version from SIG
        SPROGRAM: Program from SIG
        SNBPVKEY: '80' added to the end of SPVKEY
        SDOUSHA256PV: Double SHA256 Encoded SNBPVKEY
        SCHECKSUMPV: SDOUSHA256PV first 4 bytes
        SPREWIF: SCHECKSUMPV added to SNBPVKEY
        SADDRESS: Bech32 Encoded ('bc' added to SVERSION addet to SPROGRAM)
        SWIF: Base58 Encoded SPREWIF
        """
        curve = ecdsa.SECP256k1
        self.SPVKEY = ecdsa.SigningKey.generate(curve=curve).to_string().hex()
        self.SPUKEY = f"04{self.SPVKEY}"
        self.SSHA256PUKEY = hashlib.sha256(
            binascii.unhexlify(self.SPUKEY)).hexdigest()
        self.SRIDEMP160PUKEY = hashlib.new(
            "ripemd160", binascii.unhexlify(self.SSHA256PUKEY)).hexdigest()
        self.SIG = binascii.unhexlify(f"0014{self.SRIDEMP160PUKEY}")
        self.SVERSION = self.SIG[0] - 0x50 if self.SIG[0] else 0
        self.SPROGRAM = self.SIG[2:]
        self.SNBPVKEY = f"80{self.SPVKEY}"
        self.SDOUSHA256PV = self.DouSHA256(self.SNBPVKEY)
        self.SCHECKSUMPV = self.SDOUSHA256PV[:8]
        self.SPREWIF = self.SNBPVKEY + self.SCHECKSUMPV
        self.SADDRESS = bech32.encode("bc", self.SVERSION, self.SPROGRAM)
        self.SWIF = base58.b58encode(
            binascii.unhexlify(self.SPREWIF)).decode("UTF-8")

    def DouSHA256(self, str):
        DOUSHA256PU = str
        for i in range(1, 3):
            DOUSHA256PU = hashlib.sha256(
                binascii.unhexlify(DOUSHA256PU)).hexdigest()
        return DOUSHA256PU

    def document(self):
        docs = """
        Libraries:
        hashlib
            Hash Encodings Library
            --> Usage: Encoding
        base58
            Base58 Encodings Library
            --> Usage: Encoding
        bech32
            Bech32 Encoding Library
            --> Usage: Encoding
        binascii
            binary and ASCII Library
            --> Usage: Convertion between Binary and ASCII values
        ecdsa
            Ellicptic Curve Digital Signature Algorithm 
            --> Usage: Generate Private Key

        Step 1:
        Creating Private Key with SECP256k1 curve

        Step 2:
        Creating Public Key based on previuos Private Key

        Step 3:
        Applying SHA256 Encoding to previous Public Key

        Step 4:
        Applying RIDEMP160 Encoding to previous SHA256 Encoded Public Key

        Step 5:
        Prepending "0014" as Segwit Signature to previous RIDEMP160 Encoded Public Key then unhexlify it

        Step 6:
        Getting the 0 index as Version from previous Unhexlified Segwit Address

        Step 7:
        Getting the [2:] indexes as Program from previous Unhexlified Segwit Address

        Step 8:
        Applying Bech32 Encoding to sum of 'bc', Version, and Program

        Step 9:
        Adding "80" as Network Byte to Private Key

        Step 10:
        Applying Double SHA256 to previous Network Byte Private Key

        Step 11:
        Getting a Checksum from previous Double SHA256 Encoded Private Key
        First 4 bytes are the Checksum

        Step 12:
        Adding Checksum to Network Byte Private Key

        Step 13:
        Applying Base58 Encoding to previous Pre WIF\n\n"""

        print(docs)

    def answer(self):
        str = """
        Advantages:
        1. Bitcoin Segwit is supported from version 2.25 which allows people can save 
        more on transaction fee using Bitcoin Segwit because the transaction size is reduced.

        2. BTC Segwit transactions can also be processed faster by compressing transactions 
        and increasing the amount of data that can be written on 1 Block.

        Disadvantage
        1. Not all wallets and exchanges support Bitcoin Segwit. 
        So if you want to send Bitcoin to a user of these platforms, 
        you can only send to their Bitcoin Legacy address
        """
        print(str)

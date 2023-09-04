# Bitcoin SegWit Address Generator

This Python project provides a Bitcoin Segregated Witness (SegWit) address generator. It consists of two main files:

## Files

1. **bitcoin.py**: Contains the `BTCSegwit` class for generating Bitcoin SegWit addresses.
2. **main.py**: The main script that uses the `BTCSegwit` class to generate and display SegWit addresses.

## Getting Started

To use the Bitcoin SegWit address generator, follow these steps:

1. Ensure you have Python installed on your system.

2. Clone this repository to your local machine or download the source code.

3. Open a terminal or command prompt and navigate to the project directory.

4. Run `main.py` to generate a Bitcoin SegWit address.

## Code Structure

### `bitcoin.py`

- Defines the `BTCSegwit` class responsible for Bitcoin SegWit address generation.
- Includes methods for key generation, encoding, and documentation.

### `main.py`

- Imports the `BTCSegwit` class and uses it to generate Bitcoin SegWit addresses.
- Provides colored console output for clarity.
- Calls the `document` and `answer` methods for documentation and additional information.

## Usage

- Running `main.py` will generate a Bitcoin SegWit address and display it, along with the associated private key in Wallet Import Format (WIF).
- The address is displayed in green text, and the private key is displayed in yellow text.

## Advantages and Disadvantages

- The provided `answer` method in `bitcoin.py` explains the advantages and disadvantages of Bitcoin SegWit addresses.

## Important Notes

- This code is for educational purposes and demonstrates basic Bitcoin SegWit address generation.
- It's essential to understand that Bitcoin address generation is a complex topic, and this code is a simplified example.

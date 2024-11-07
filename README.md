# guess-nationality

This project uses the `nationalize.io` API to predict the nationality of a given name. Users can input a name and a country ID, and the program will respond with the probability that the name is from the specified country. If the specified country is not among the predicted nationalities, the program will list the probabilities for all nationalities that were found.

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This project requires Python and the `requests` library

#### Installation

1. Clone the repo
`git clone https://github.com/umutulay/guessNationality.git`
2. Install Python packages
`pip install -r requirements.txt`

## Usage

Run the script from the command line. You will be prompted to enter a name and a country ID (e.g., 'US' for United States):

`python guess_nationality.py`

Follow the prompts to input the name and country ID.

## Authors

* Umut Tulay - [umutulay](https://github.com/umutulay)

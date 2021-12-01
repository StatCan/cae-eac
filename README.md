### Prerequisites

The following software needs to be available on your system. Our scripts won't
install these for you because they generally require super-user and we don't
want that much responsibility. :wink:

- GNU Make (e.g. `apt install make`)
- [Node.js][] (e.g. see [`nvm-sh/nvm`][nvm-installation])
- npm (comes with Node.js)
- Yarn (e.g. `npm install --global yarn`)
- Python 3.x (e.g. `apt install python3`)
- Python venv module (e.g. `apt install python3-venv`)

### Get Started

1. Ensure you have the above prerequisites
2. Clone this repository
3. Change directory to project root
4. Install remaining dependencies: `make install`
5. <!-- markdownlint-disable no-inline-html -->
   Start a docs server in the language of your choice: `make serve-en` or
   `make serve-fr` (<kbd>CTRL</kbd>+<kbd>C</kbd> to quit)
   <!-- markdownlint-enable -->

You can now see your rendered documentation at `http://localhost:8000` and it
should automatically update when you edit/save your files.
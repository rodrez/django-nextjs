# Django & Next.js Template Example

This repository provides a basic setup that integrates Django as the backend and Next.js as the frontend for your web application.

## Getting Started

### Prerequisites

* Python 3.x
* Node.js 12.x or later
* pipenv or pip
* Yarn or npm

### Installation

#### Backend setup:

Navigate to the Django project directory:

```bash
cd backend
```

Install the dependencies:

```bash
py -3.11 -m venv env
# activate env then
pip install django && django-cors-headers
```

Start the development server:

```bash
python manage.py makemigrations &&
python manage.py migrate &&
python manage.py runserver
```

### Frontend setup:

Navigate to the Next.js project directory:

```bash
cd frontend
```

Install the dependencies:

```bash
yarn install
# or
npm install
# or
pnpm i
```

Start the development server:

```bash
yarn dev
# or
npm run dev
# or
pnpm run dev
```
## Features

Pre-configured connection settings between Django and Next.js.

## Contribution

If you find any issues or have suggestions, please open an issue. Pull requests are always welcome!

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Note: This is a basic example, and you might need to adapt it according to the 
features and configurations of your project. The main goal is to help you get 
started quickly with the integration of Django and Next.js.

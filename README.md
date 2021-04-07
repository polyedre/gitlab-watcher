<h1 align="center">
  Gitlab Watcher
</h1>

<h4 align="center">A utility to list activities assigned to an user on Gitlab (Issues, Merge Requests, TODOs).</h4>

<p align="center">
  <a href="#install">How To Use</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#license">License</a>
</p>

## Install

1. Clone the repository and cd to it.
1. Install the requirements:

   ```sh
   pip install -r requirements.txt
   ```

1. Install the package:

   ```sh
   python3 setup.py install
   ```

## How To Use

1. First, [generate an access token](https://gitlab.com/-/profile/personal_access_tokens)
1. Then list your assigned issues, merge request and todos:

   ```sh
   gitlab-watcher --url https://gitlab.com --access-token <ACCESS-TOKEN>
   ```

## License

GNU GPL 3.0 License

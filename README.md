# Hil Sample App

1. Clone the repository:

	```console
	$ git clone --recursive git@github.com:fvioz/hil-sample.git
	$ cd hil-sample
    ```

2. Install the requirements:

	```console
	$ pip3 install -r hil/requirements.txt
    ```

3. Run the sample app:

	```console
	python3 `main.py`
    ```

4. Run `Bell` app

	```console
	$ curl -X POST --data "component=Bell&event=play" http://localhost:8000
    ```

5. Run `Dialog` app

	```console
	$ curl -X POST --data "component=Dialog&event=show" http://localhost:8000
    ```

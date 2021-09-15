
# The test of sending emails using Yandex.Mail

## Prepare files & libraries

1. Download selenium standalone server from: https://is.gd/AkvDcr (Used server-standalone-3.141.59.jar).
Create local folder at ~/<WORKDIR_SELENIUM_STANDALONE> and copy or move jar to that path:

```bash
$ mkdir ~/<WORKDIR_SELENIUM_STANDALONE>
$ cd ~/<WORKDIR_SELENIUM_STANDALONE>
$ wget https://is.gd/AkvDcr
$ mv selenium-server-standalone-3.141.59.jar ~/<WORKDIR_SELENIUM_STANDALONE>/
```

2. Install selenium WebDriver and other modules from <TEST_DIR> in your shell 

```bash
$ pip install -r requirements.txt.
```

3. Download chrome driver from https://is.gd/klvycm for your operating system and copy it to <WORKDIR_SELENIUM_STANDALONE>.

4. Install the Allure according to the instructions on the link (https://is.gd/FMeobj) for your operating system.

##Set up environment:

Run the standalone server in a hub mode (open new terminal first):

```bash
$ cd ~/selenium
$ java -jar selenium-server-standalone-3.141.59.jar -role hub -host localhost
```
After that we will see where our nodes should register themselves. 
Nodes should register to http://localhost:4444/grid/register/.Let's register the node in another terminal:

```bash
$ cd ~/selenium
$ java -jar selenium-server-standalone-3.141.59.jar -role node -hub http://localhost:4444/grid/register/ -port 3456
```

## Run test

To start the test, you need from the <TEST_DIR> in new terminal:

```bash
$ pytest --alluredir=./allure_reports
```

To get the report using the Allure, you need to run the command:

```bash
$ allure serve ./allure_reports
```